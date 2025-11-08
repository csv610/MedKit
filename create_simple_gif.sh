#!/bin/bash

# Simple script to create pipeline animation GIF
OUTPUT="/Users/csv610/Projects/Gemini/MedKit/medkit_pipeline_animation.gif"
TEMP_DIR=$(mktemp -d)

echo "Creating pipeline animation GIF..."
echo "Temp directory: $TEMP_DIR"

# Create PNG frames - we'll create 120 frames (4 seconds at 30fps for demo)
echo "Generating 120 animation frames..."
for i in {0..119}; do
    FRAME=$((i))
    PROGRESS=$(printf "%.4f" $(echo "scale=4; $i / 120" | bc))

    # Determine animation phase
    if (( $(echo "$PROGRESS < 0.33" | bc -l) )); then
        # Cache hit phase
        PHASE_PROGRESS=$(printf "%.4f" $(echo "scale=4; $PROGRESS * 3" | bc))
        PARTICLE_X=$(printf "%.0f" $(echo "$PHASE_PROGRESS * 1000 + 200" | bc))
        PARTICLE_Y=150
        LABEL_Y="Cache Hit Path"
        PARTICLE_COLOR="rgb(46,125,50)"
        BG_COLOR="rgb(232,245,233)"
    else
        # Full path phase
        PHASE_PROGRESS=$(printf "%.4f" $(echo "scale=4; ($PROGRESS - 0.33) / 0.67" | bc))
        PARTICLE_X=$(printf "%.0f" $(echo "$PHASE_PROGRESS * 1000 + 200" | bc))
        PARTICLE_Y=350
        LABEL_Y="Full Path (Cache Miss)"
        PARTICLE_COLOR="rgb(2,119,189)"
        BG_COLOR="rgb(227,242,253)"
    fi

    if [ $((i % 30)) -eq 0 ]; then
        echo "Creating frame $FRAME/120"
    fi

    # Create frame PNG using ImageMagick
    PROGRESS_PERCENT=$(echo "$PROGRESS * 100" | awk '{printf "%.1f", $0}')
    convert -size 1600x900 xc:"$BG_COLOR" \
        -fill "white" -draw "rectangle 0,0 1600,80" \
        -fill "rgb(2,119,189)" -pointsize 24 -gravity North -annotate +0+25 "MedKit Data Flow Pipeline" \
        -fill "rgb(100,100,100)" -pointsize 12 -annotate +0+55 "Particle Animation: Data Journey Through System" \
        -fill "rgb(120,120,120)" -pointsize 14 -gravity SouthWest -annotate +20+20 "Frame: $FRAME/120 | Progress: ${PROGRESS_PERCENT}%" \
        -fill "$PARTICLE_COLOR" -draw "circle $PARTICLE_X,$PARTICLE_Y $((PARTICLE_X+15)),$PARTICLE_Y" \
        -fill "rgb(150,150,150)" -pointsize 13 -gravity Center -annotate +0-100 "$LABEL_Y" \
        "$TEMP_DIR/frame_$(printf '%03d' $i).png"
done

echo "✓ Generated 120 frames"

# Create animated GIF from frames
echo "Creating animated GIF..."
convert -delay 3 -loop 0 "$TEMP_DIR"/frame_*.png "$OUTPUT"

echo "✓ GIF created successfully"
echo "  Output: $OUTPUT"
echo ""
echo "Note: Interactive HTML animation is also available at:"
echo "  medkit_pipeline_animation.html"
echo ""
echo "This provides an animated visualization of the data flow through:"
echo "  - Cache Hit Path (fast, ~10ms)"
echo "  - Full Path (cache miss, schema validation, API call)"

# Cleanup temp directory
rm -rf "$TEMP_DIR"
echo "✓ Temporary files cleaned up"
