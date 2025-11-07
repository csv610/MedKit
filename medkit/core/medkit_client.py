"""medkit_client - Medical Content Generation with Gemini and Pydantic Schema Support.

A specialized wrapper around Google's Gemini API that provides domain-specific
functionality for generating medical content with guaranteed structured output.
This client extends GeminiClient with medical expertise context and integrates
PydanticPromptGenerator for sophisticated schema-aware prompt engineering.

Provides high-level methods for generating medical documentation, clinical decision
trees, procedure guides, and medical knowledge bases. All outputs are validated
against Pydantic schemas, ensuring data integrity and type safety. Includes
automatic retry logic, temperature optimization for factual medical content,
and support for both text generation and medical image analysis.

QUICK START:
    Generate structured medical content:

        from medkit_client import MedKitClient
        from pydantic import BaseModel, Field

        class ProcedureGuide(BaseModel):
            name: str = Field(description="Procedure name")
            steps: list = Field(description="Step-by-step instructions")
            risks: list = Field(description="Known complications")

        client = MedKitClient()
        guide = client.generate_text(
            prompt="Explain the colonoscopy procedure",
            schema=ProcedureGuide
        )

COMMON USES:
    - Generating standardized medical decision trees
    - Creating procedure guidelines with risk documentation
    - Analyzing medical images with structured output
    - Building medical knowledge bases with validated schemas
    - Generating patient education materials with consistent formatting
    - Creating clinical protocol documentation

KEY FEATURES:
    - Automatic schema-aware prompt generation from Pydantic models
    - Low temperature settings (0.3) for factual medical accuracy
    - Integrated image analysis with base64 encoding
    - Configurable prompt styles (DETAILED, CONCISE, TECHNICAL)
    - Built-in retry logic (max 3 attempts) with exponential backoff
    - JSON response validation against schemas
    - Support for markdown JSON extraction from LLM responses
"""

import base64
import json
from typing import Optional

from pydantic import BaseModel

from medkit.core.gemini_client import GeminiClient, ModelConfig, ModelInput
from medkit.utils.pydantic_prompt_generator import PydanticPromptGenerator, PromptStyle


class MedKitClient(GeminiClient):
    """
    Extended GeminiClient for medical content generation and image analysis.

    Inherits all retry logic and error handling from GeminiClient.
    """

    def __init__(self, model_name: str = "gemini-2.5-flash", **kwargs):
        """
        Initialize MedKitClient with optimized configuration.

        Args:
            model_name: Gemini model to use
            **kwargs: Additional arguments passed to GeminiClient
        """
        config = ModelConfig(
            model_name=model_name,
            max_retries=3,
            initial_delay=1.0,
            temperature=0.3,
        )
        super().__init__(config=config, **kwargs)

    def generate_text(
        self,
        prompt: str,
        schema: type[BaseModel],
        sys_prompt: str = None,
    ) -> BaseModel:
        """
        Generate structured text with schema validation.

        Args:
            prompt: User prompt describing the task
            schema: Pydantic model for structured output
            sys_prompt: System prompt for context (optional)

        Returns:
            Validated Pydantic model instance with generated data
        """
        # Generate schema-aware prompt from Pydantic schema
        generator = PydanticPromptGenerator(
            schema,
            style=PromptStyle.DETAILED,
            include_examples=True,
            validate_schema=True,
        )
        schema_prompt = generator.generate_prompt()

        user_prompt = f"{prompt}\n\n{schema_prompt}"

        model_input = ModelInput(
            user_prompt=user_prompt,
            sys_prompt=sys_prompt,
            response_schema=schema,
        )

        return self.generate_content(model_input)

    def analyze_image(
        self,
        image_data: str,
        schema: type[BaseModel],
        prompt: str,
        sys_prompt: Optional[str] = None,
        mime_type: str = "image/jpeg",
        temperature: float = 0.3,
    ) -> BaseModel:
        """
        General-purpose image analysis with structured output.

        Args:
            image_data: Base64 encoded image data
            schema: Pydantic model for structured output
            prompt: User prompt describing the analysis task
            sys_prompt: System prompt for context (optional)
            mime_type: MIME type of the image (default: image/jpeg)
            temperature: Model temperature for response (default: 0.3 for accurate extraction)

        Returns:
            Validated Pydantic model instance with extracted/analyzed data
        """
        from google import genai

        # Prepare the image part
        image_part = genai.types.Part.from_bytes(
            data=base64.b64decode(image_data),
            mime_type=mime_type
        )

        # Create content with image and prompt
        contents = [
            genai.types.Content(
                role="user",
                parts=[image_part, genai.types.Part(text=prompt)]
            )
        ]

        # Prepare config
        config_params = {
            'temperature': temperature,
            'response_mime_type': 'application/json'
        }
        if sys_prompt:
            config_params['system_instruction'] = sys_prompt
        config = genai.types.GenerateContentConfig(**config_params)

        # Generate response
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=config
        )

        # Parse response
        result_text = response.text
        try:
            extracted_json = json.loads(result_text)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown if needed
            if "```json" in result_text:
                json_str = result_text.split("```json")[1].split("```")[0].strip()
                extracted_json = json.loads(json_str)
            elif "```" in result_text:
                json_str = result_text.split("```")[1].split("```")[0].strip()
                extracted_json = json.loads(json_str)
            else:
                raise ValueError(f"Could not parse image analysis result: {result_text}")

        # Validate against schema
        return schema(**extracted_json)
