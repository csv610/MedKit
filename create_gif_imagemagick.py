#!/usr/bin/env python3
"""
Create animated GIF using ImageMagick (convert command).
Shows MedKit data flow pipeline with particle animations.
"""

import os
import subprocess
import tempfile
from pathlib import Path

# Configuration
OUTPUT_PATH = "/Users/csv610/Projects/Gemini/MedKit/medkit_pipeline_animation.gif"
FRAMES = 240  # 8 seconds at 30 FPS
WIDTH, HEIGHT = 1600, 900
DELAY = 33  # milliseconds (30 FPS = 33ms per frame)

# Colors (RGB)
COLORS = {
    'bg': 'rgb(248,249,250)',
    'border': 'rgb(200,200,200)',
    'text': 'rgb(26,26,26)',
    'header': 'rgb(2,119,189)',
    'input': 'rgb(46,125,50)',
    'process': 'rgb(2,119,189)',
    'cache': 'rgb(245,124,0)',
    'api': 'rgb(123,31,162)',
    'output': 'rgb(194,24,91)',
    'particle_fast': 'rgb(46,125,50)',
    'particle_full': 'rgb(2,119,189)',
}

# Pipeline stages
STAGES = [
    ("User Input", 1, COLORS['input']),
    ("API Layer", 2, COLORS['input']),
    ("MedKitClient", 3, COLORS['process']),
    ("Cache Check", "4a", COLORS['cache']),
    ("Prompt Gen", 5, COLORS['process']),
    ("Gemini API", 6, COLORS['api']),
    ("Parse Response", 7, COLORS['process']),
    ("Validation", 8, COLORS['process']),
    ("Privacy Check", 9, COLORS['process']),
    ("Store Cache", 10, COLORS['cache']),
    ("Return", 11, COLORS['output']),
]

def create_svg_frame(frame_num):
    """Create SVG for a single frame."""
    progress = (frame_num % FRAMES) / FRAMES

    # SVG header
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}">
<defs>
    <style>
        text {{ font-family: Arial, sans-serif; }}
        .title {{ font-size: 24px; font-weight: bold; text-anchor: middle; fill: {COLORS['header']}; }}
        .subtitle {{ font-size: 12px; fill: #666; text-anchor: middle; }}
        .stage-name {{ font-size: 10px; fill: #333; text-anchor: middle; }}
        .step-number {{ font-size: 16px; font-weight: bold; fill: white; text-anchor: middle; }}
        .legend-text {{ font-size: 11px; fill: #666; }}
    </style>
</defs>

<!-- Background -->
<rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg']}"/>

<!-- Header -->
<rect x="0" y="0" width="{WIDTH}" height="80" fill="white" stroke="{COLORS['border']}" stroke-width="1"/>
<text x="{WIDTH//2}" y="40" class="title">MedKit Data Flow Pipeline</text>
<text x="{WIDTH//2}" y="60" class="subtitle">Particle Animation: Data Journey Through System</text>

'''

    # Draw stages
    y_pos = 250
    stage_spacing = 100
    box_width, box_height = 80, 60

    for i, (name, step, color) in enumerate(STAGES):
        x = 80 + i * stage_spacing

        # Draw box
        svg += f'''<g>
  <rect x="{x - box_width//2}" y="{y_pos - box_height//2}" width="{box_width}" height="{box_height}"
        rx="8" fill="{color}" stroke="{COLORS['border']}" stroke-width="2"/>
  <text x="{x - 30}" y="{y_pos - 10}" class="step-number">{step}</text>
  <text x="{x + 10}" y="{y_pos - 5}" class="stage-name">{name.split()[0]}</text>
  <text x="{x + 10}" y="{y_pos + 8}" class="stage-name">{name.split()[1] if len(name.split()) > 1 else ''}</text>
</g>
'''

        # Draw arrow to next stage
        if i < len(STAGES) - 1:
            next_x = 80 + (i + 1) * stage_spacing
            border_color = COLORS['border']
            svg += f'<line x1="{x + 45}" y1="{y_pos}" x2="{next_x - 45}" y2="{y_pos}" stroke="{border_color}" stroke-width="2"/>\n'

    # Fast path label
    particle_fast = COLORS['particle_fast']
    particle_full = COLORS['particle_full']
    svg += f'<text x="100" y="130" class="legend-text" fill="{particle_fast}">Cache Hit Path (Fast)</text>\n'
    svg += f'<text x="100" y="147" class="legend-text" fill="{particle_full}">Full Path (Cache Miss)</text>\n'

    # Draw particles based on progress
    FAST_PATH = [0, 1, 2, 3, 10]
    FULL_PATH = list(range(11))

    pf_color = COLORS['particle_fast']
    pf_full_color = COLORS['particle_full']

    if progress < 0.33:
        # Fast path animation (first 33%)
        fast_progress = progress * 3
        for offset in range(3):
            p_progress = (fast_progress - offset * 0.1) % 1.0
            if p_progress >= 0:
                stage_idx = int(p_progress * len(FAST_PATH))
                if stage_idx < len(FAST_PATH):
                    stage = FAST_PATH[stage_idx]
                    particle_x = 80 + stage * stage_spacing

                    if stage_idx < len(FAST_PATH) - 1:
                        next_stage = FAST_PATH[stage_idx + 1]
                        next_x = 80 + next_stage * stage_spacing
                        intra_progress = (p_progress * len(FAST_PATH)) % 1.0
                        particle_x = particle_x + intra_progress * (next_x - particle_x)

                    svg += f'<circle cx="{particle_x:.1f}" cy="{y_pos - 80}" r="6" fill="{pf_color}" opacity="0.9"/>\n'
    else:
        # Full path animation (last 67%)
        full_progress = (progress - 0.33) / 0.67
        for offset in range(4):
            p_progress = (full_progress - offset * 0.08) % 1.0
            if p_progress >= 0:
                stage_idx = int(p_progress * len(FULL_PATH))
                if stage_idx < len(FULL_PATH):
                    stage = FULL_PATH[stage_idx]
                    particle_x = 80 + stage * stage_spacing

                    if stage_idx < len(FULL_PATH) - 1:
                        next_stage = FULL_PATH[stage_idx + 1]
                        next_x = 80 + next_stage * stage_spacing
                        intra_progress = (p_progress * len(FULL_PATH)) % 1.0
                        particle_x = particle_x + intra_progress * (next_x - particle_x)

                    svg += f'<circle cx="{particle_x:.1f}" cy="{y_pos + 80}" r="6" fill="{pf_full_color}" opacity="0.9"/>\n'

    # Progress bar
    progress_width = int(400 * (frame_num / FRAMES))
    svg += f'''<rect x="100" y="520" width="400" height="20" fill="{COLORS['border']}" stroke="#999" stroke-width="1"/>
<rect x="100" y="520" width="{progress_width}" height="20" fill="{COLORS['header']}"/>
<text x="520" y="535" class="legend-text">Frame {frame_num}/{FRAMES}</text>

<!-- Info box -->
<rect x="80" y="600" width="1440" height="250" rx="8" fill="#fff3cd" stroke="#ffc107" stroke-width="2"/>
<text x="100" y="625" style="font-weight: bold; font-size: 13px; fill: #856404;">📊 DATA FLOW EXPLANATION:</text>
<text x="100" y="645" class="legend-text" fill="#333;">Cache Hit (Green Particles): Request reaches LMDB cache at Step 4 → Data found → Returns immediately (Steps 5-10 skipped) → Response in ~10ms</text>
<text x="100" y="665" class="legend-text" fill="#333;">Full Path (Blue Particles): Cache miss → Prompt generation (5) → Gemini API (6) → Parse response (7) → Pydantic validation (8) →</text>
<text x="100" y="685" class="legend-text" fill="#333;">Privacy compliance (9) → Store in cache (10) → Return response</text>
<text x="100" y="710" style="font-weight: bold; font-size: 12px; fill: #2E7D32;">✓ Key Benefits:</text>
<text x="120" y="730" class="legend-text" fill="#333;">Caching reduces API calls by ~60% • Schema validation ensures data integrity • Privacy compliance built-in</text>
<text x="120" y="750" class="legend-text" fill="#333;">Pydantic ensures type-safe structured output • Automatic retry logic (max 3 attempts) with exponential backoff</text>
</svg>
'''

    return svg

def create_gif():
    """Create animated GIF using ImageMagick."""
    print(f"Creating {FRAMES} SVG frames...")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create SVG frames
        for frame_num in range(FRAMES):
            if frame_num % 30 == 0:
                print(f"  Creating frame {frame_num}/{FRAMES}")

            svg_content = create_svg_frame(frame_num)
            svg_path = tmpdir_path / f"frame_{frame_num:04d}.svg"

            with open(svg_path, 'w') as f:
                f.write(svg_content)

        # Convert SVG to PNG and create GIF
        print(f"Converting frames to GIF...")
        svg_pattern = str(tmpdir_path / "frame_%04d.svg")
        png_pattern = str(tmpdir_path / "frame_%04d.png")

        # Convert SVG to PNG
        cmd_convert = [
            'convert',
            '-density', '96',
            svg_pattern,
            png_pattern
        ]
        print(f"Converting SVG to PNG...")
        subprocess.run(cmd_convert, check=True, capture_output=True)

        # Create GIF from PNG frames
        print(f"Creating GIF...")
        cmd_gif = [
            'convert',
            '-delay', str(DELAY),
            '-loop', '0',
            '-fuzz', '5%',
            str(tmpdir_path / "frame_*.png"),
            OUTPUT_PATH
        ]
        subprocess.run(cmd_gif, check=True, capture_output=True)

    print(f"✓ GIF created successfully!")
    print(f"  Path: {OUTPUT_PATH}")
    print(f"  Size: {WIDTH}x{HEIGHT}px")
    print(f"  Duration: {FRAMES * DELAY / 1000:.1f} seconds")
    print(f"  FPS: {1000 / DELAY:.0f}")

if __name__ == "__main__":
    create_gif()
