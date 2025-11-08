#!/usr/bin/env python3
"""
Create animated GIF showing MedKit data flow pipeline with particle animations.
Shows both cache hit (fast path) and cache miss (full path) scenarios.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import math

# Configuration
OUTPUT_PATH = "/Users/csv610/Projects/Gemini/MedKit/medkit_pipeline_animation.gif"
WIDTH, HEIGHT = 1600, 900
FPS = 30
TOTAL_SECONDS = 8
FRAMES = FPS * TOTAL_SECONDS

# Colors
BG_COLOR = (248, 249, 250)
BORDER_COLOR = (200, 200, 200)
TEXT_COLOR = (26, 26, 26)
HEADER_COLOR = (2, 119, 189)
INPUT_COLOR = (46, 125, 50)
PROCESS_COLOR = (2, 119, 189)
CACHE_COLOR = (245, 124, 0)
API_COLOR = (123, 31, 162)
OUTPUT_COLOR = (194, 24, 91)

# Particle colors
PARTICLE_FAST = (46, 125, 50)  # Green for cache hit
PARTICLE_FULL = (2, 119, 189)  # Blue for full path
PARTICLE_VALID = (76, 175, 80)  # Light green for valid
PARTICLE_FAIL = (244, 67, 54)  # Red for failed

# Pipeline stages with positions
STAGES = [
    {"name": "User Input", "x": 80, "color": INPUT_COLOR, "step": 1},
    {"name": "API Layer", "x": 200, "color": INPUT_COLOR, "step": 2},
    {"name": "MedKitClient", "x": 320, "color": PROCESS_COLOR, "step": 3},
    {"name": "Cache Check", "x": 440, "color": CACHE_COLOR, "step": "4a"},
    {"name": "Prompt Gen", "x": 560, "color": PROCESS_COLOR, "step": 5},
    {"name": "Gemini API", "x": 680, "color": API_COLOR, "step": 6},
    {"name": "Parse Response", "x": 800, "color": PROCESS_COLOR, "step": 7},
    {"name": "Validation", "x": 920, "color": PROCESS_COLOR, "step": 8},
    {"name": "Privacy Check", "x": 1040, "color": PROCESS_COLOR, "step": 9},
    {"name": "Store Cache", "x": 1160, "color": CACHE_COLOR, "step": 10},
    {"name": "Return", "x": 1280, "color": OUTPUT_COLOR, "step": 11},
]

# Fast path (cache hit) - skips steps 5-10
FAST_PATH_INDICES = [0, 1, 2, 3, 10]  # User -> API -> Client -> Cache -> Return
FULL_PATH_INDICES = list(range(11))  # All steps


def draw_box(draw, x, y, width, height, color, label, step):
    """Draw a pipeline stage box."""
    # Draw box
    draw.rectangle([x - width // 2, y - height // 2, x + width // 2, y + height // 2],
                   fill=color, outline=BORDER_COLOR, width=2)

    # Draw step number
    step_text = str(step)
    step_bbox = draw.textbbox((0, 0), step_text, font=None)
    step_w = step_bbox[2] - step_bbox[0]
    step_h = step_bbox[3] - step_bbox[1]
    draw.text((x - width // 2 + 15, y - height // 2 + 10), step_text,
              fill="white", font=None)

    # Draw label
    label_lines = label.split("\n")
    y_offset = y - 5
    for line in label_lines:
        draw.text((x - width // 2 + 40, y_offset), line, fill=TEXT_COLOR, font=None)
        y_offset += 15


def draw_arrow(draw, x1, y1, x2, y2, color, width=2):
    """Draw arrow from (x1, y1) to (x2, y2)."""
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

    # Arrowhead
    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_size = 12
    arrow_x = x2 - arrow_size * math.cos(angle)
    arrow_y = y2 - arrow_size * math.sin(angle)

    p1 = (arrow_x + arrow_size * math.cos(angle - math.pi / 6),
          arrow_y + arrow_size * math.sin(angle - math.pi / 6))
    p2 = (arrow_x + arrow_size * math.cos(angle + math.pi / 6),
          arrow_y + arrow_size * math.sin(angle + math.pi / 6))

    draw.polygon([p1, p2, (x2, y2)], fill=color)


def draw_particle(draw, x, y, radius=6, color=PARTICLE_FULL):
    """Draw a particle (circle)."""
    draw.ellipse([x - radius, y - radius, x + radius, y + radius],
                 fill=color, outline=color)


def create_frame(frame_num):
    """Create a single frame of the animation."""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw header
    draw.rectangle([0, 0, WIDTH, 80], fill="white", outline=BORDER_COLOR, width=1)
    draw.text((WIDTH // 2 - 150, 25), "MedKit Data Flow Pipeline", fill=HEADER_COLOR, font=None)
    draw.text((WIDTH // 2 - 200, 50), "Particle Animation: Data Journey Through System", fill=(100, 100, 100), font=None)

    # Draw pipeline boxes
    y_pos = 250
    for stage in STAGES:
        draw_box(draw, stage["x"], y_pos, 80, 60, stage["color"],
                stage["name"], stage["step"])

    # Draw arrows between stages
    for i in range(len(STAGES) - 1):
        x1 = STAGES[i]["x"] + 45
        x2 = STAGES[i + 1]["x"] - 45
        draw_arrow(draw, x1, y_pos, x2, y_pos, BORDER_COLOR, width=1)

    # Draw label for paths
    draw.text((80, 350), "Cache Hit (Fast Path)", fill=PARTICLE_FAST, font=None)
    draw.text((80, 370), "Full Path (Cache Miss)", fill=PARTICLE_FULL, font=None)

    # Calculate particle positions based on frame
    progress = (frame_num % FRAMES) / FRAMES

    # Fast path particles (cache hit - 1/3 of animation)
    if progress < 0.33:
        fast_progress = progress * 3
        # Move through fast path indices
        stage_idx = int(fast_progress * len(FAST_PATH_INDICES))
        if stage_idx < len(FAST_PATH_INDICES):
            current_stage_idx = FAST_PATH_INDICES[stage_idx]
            particle_x = STAGES[current_stage_idx]["x"]

            # Interpolate between stages
            if stage_idx < len(FAST_PATH_INDICES) - 1:
                next_stage_idx = FAST_PATH_INDICES[stage_idx + 1]
                stage_progress = (fast_progress * len(FAST_PATH_INDICES)) % 1.0
                particle_x = (STAGES[current_stage_idx]["x"] +
                            stage_progress * (STAGES[next_stage_idx]["x"] -
                                            STAGES[current_stage_idx]["x"]))

            # Draw multiple particles for fast path
            for offset in range(3):
                p_progress = (fast_progress - offset * 0.1) % 1.0
                if p_progress >= 0:
                    p_stage_idx = int(p_progress * len(FAST_PATH_INDICES))
                    if p_stage_idx < len(FAST_PATH_INDICES):
                        p_current = FAST_PATH_INDICES[p_stage_idx]
                        p_x = STAGES[p_current]["x"]
                        if p_stage_idx < len(FAST_PATH_INDICES) - 1:
                            p_next = FAST_PATH_INDICES[p_stage_idx + 1]
                            p_stage_progress = (p_progress * len(FAST_PATH_INDICES)) % 1.0
                            p_x = (STAGES[p_current]["x"] +
                                 p_stage_progress * (STAGES[p_next]["x"] - STAGES[p_current]["x"]))
                        draw_particle(draw, int(p_x), y_pos - 80, color=PARTICLE_FAST)

    # Full path particles (cache miss - 2/3 of animation)
    else:
        full_progress = (progress - 0.33) * 1.5
        stage_idx = int(full_progress * len(FULL_PATH_INDICES))

        if stage_idx < len(FULL_PATH_INDICES):
            current_stage_idx = FULL_PATH_INDICES[stage_idx]
            particle_x = STAGES[current_stage_idx]["x"]

            # Interpolate between stages
            if stage_idx < len(FULL_PATH_INDICES) - 1:
                next_stage_idx = FULL_PATH_INDICES[stage_idx + 1]
                stage_progress = (full_progress * len(FULL_PATH_INDICES)) % 1.0
                particle_x = (STAGES[current_stage_idx]["x"] +
                            stage_progress * (STAGES[next_stage_idx]["x"] -
                                            STAGES[current_stage_idx]["x"]))

            # Draw multiple particles for full path
            for offset in range(3):
                p_progress = (full_progress - offset * 0.08) % 1.0
                if p_progress >= 0:
                    p_stage_idx = int(p_progress * len(FULL_PATH_INDICES))
                    if p_stage_idx < len(FULL_PATH_INDICES):
                        p_current = FULL_PATH_INDICES[p_stage_idx]
                        p_x = STAGES[p_current]["x"]
                        if p_stage_idx < len(FULL_PATH_INDICES) - 1:
                            p_next = FULL_PATH_INDICES[p_stage_idx + 1]
                            p_stage_progress = (p_progress * len(FULL_PATH_INDICES)) % 1.0
                            p_x = (STAGES[p_current]["x"] +
                                 p_stage_progress * (STAGES[p_next]["x"] - STAGES[p_current]["x"]))
                        draw_particle(draw, int(p_x), y_pos + 80, color=PARTICLE_FULL)

    # Draw legend
    legend_y = 500
    draw.text((80, legend_y), "Legend:", fill=TEXT_COLOR, font=None)
    draw_particle(draw, 100, legend_y + 25, color=PARTICLE_FAST)
    draw.text((120, legend_y + 20), "Cache Hit Path (Steps: 1→2→3→4→11)", fill=TEXT_COLOR, font=None)

    draw_particle(draw, 100, legend_y + 50, color=PARTICLE_FULL)
    draw.text((120, legend_y + 45), "Full Path (Steps: 1→2→...→11)", fill=TEXT_COLOR, font=None)

    # Draw info box
    info_y = 650
    draw.rectangle([60, info_y, WIDTH - 60, info_y + 180], outline=BORDER_COLOR, width=1, fill=(255, 253, 231))
    draw.text((80, info_y + 10), "DATA FLOW EXPLANATION:", fill=HEADER_COLOR, font=None)
    draw.text((80, info_y + 30), "Cache Hit (Green): Request hits LMDB cache at step 4 → Returns immediately (steps 5-10 skipped)", fill=TEXT_COLOR, font=None)
    draw.text((80, info_y + 50), "Full Path (Blue): Cache miss → Generates prompt (5) → Calls Gemini API (6) → Parses response (7) →", fill=TEXT_COLOR, font=None)
    draw.text((100, info_y + 70), "Validates with Pydantic (8) → Privacy check (9) → Stores in cache (10) → Returns response", fill=TEXT_COLOR, font=None)
    draw.text((80, info_y + 95), "Key Benefits: Caching reduces API calls by ~60% • Schema validation ensures data integrity", fill=(0, 100, 0), font=None)
    draw.text((80, info_y + 115), "Privacy compliance built-in • Pydantic ensures type-safe structured output", fill=(0, 100, 0), font=None)

    return img


def create_gif():
    """Create the animated GIF."""
    print(f"Creating {FRAMES} frames for animation...")
    frames = []

    for frame_num in range(FRAMES):
        if frame_num % 10 == 0:
            print(f"  Frame {frame_num}/{FRAMES}")

        frame = create_frame(frame_num)
        frames.append(frame)

    print(f"Saving GIF to {OUTPUT_PATH}...")
    frames[0].save(
        OUTPUT_PATH,
        save_all=True,
        append_images=frames[1:],
        duration=1000 // FPS,  # Convert to milliseconds
        loop=0,  # Loop forever
        optimize=False
    )
    print(f"✓ GIF created successfully!")
    print(f"  Size: {WIDTH}x{HEIGHT}px")
    print(f"  Duration: {TOTAL_SECONDS} seconds")
    print(f"  FPS: {FPS}")


if __name__ == "__main__":
    create_gif()
