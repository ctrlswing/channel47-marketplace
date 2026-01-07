---
name: image-gen
description: Use when asked to generate, create, or make images, pictures, artwork, or visual content. Also triggers on requests for product photos, illustrations, concept art, or any visual media creation.
args:
  - name: subject
    description: What to generate (the main subject or scene)
    required: false
  - name: style
    description: Visual style (photo, illustration, painting, 3d, sketch, cartoon)
    required: false
    flag: true
  - name: aspect
    description: "Aspect ratio: square, landscape, portrait, cinematic, wide"
    required: false
    flag: true
  - name: quality
    description: "Quality level: fast (Flash model) or pro (Pro model)"
    required: false
    flag: true
  - name: output
    description: File path to save the image
    required: false
    flag: true
---

# Image Generation Skill

Generate AI-powered images using Nano Banana Pro (Gemini 3 Pro Image) and Nano Banana (Gemini 2.5 Flash Image).
This skill provides professional-grade image generation with smart model selection, aspect ratio control, and Google Search grounding.

## Capabilities

- **Smart Model Selection**:
  - `Pro` (Gemini 3 Pro Image): Best for photorealism, text rendering, and complex scenes. Supports up to 4K resolution.
  - `Flash` (Gemini 2.5 Flash Image): Best for speed (2-3s), iterating on concepts, and simple illustrations.
  - `Auto`: Automatically selects based on prompt keywords (e.g., "4k", "professional" triggers Pro; "sketch", "draft" triggers Flash).

## Workflow

### Step 1: Gather Requirements

If the user hasn't specified details, clarify:

1. **Subject**: What should be in the image?
2. **Style**: Photo, illustration, painting, 3D render, sketch?
3. **Aspect**: Square (1:1), landscape (16:9), portrait (9:16)?
4. **Quality**: Fast iteration or final quality?

Load prompt tips if crafting complex prompts:
```
@prompt-tips.md
```

### Step 2: Select Model and Settings

**Model Selection Logic:**

Use **Flash** when:
- User says "quick", "fast", "sketch", "draft"
- Iterating on concepts
- Time-sensitive requests
- Simple subjects

Use **Pro** when:
- User says "professional", "4k", "detailed", "photorealistic"
- Commercial or final assets
- Complex compositions
- Grounding is needed

**Aspect Ratio Mapping:**

| User Says | Ratio | Use Case |
|-----------|-------|----------|
| square | 1:1 | Social media, profiles |
| landscape | 16:9 | Desktop, presentations |
| portrait | 9:16 | Mobile, stories |
| cinematic | 21:9 | Ultrawide, films |
| wide | 2:1 | Panoramas, headers |

### Step 3: Craft the Prompt

Good prompts include:

1. **Subject**: Main focus clearly described
2. **Style**: Art style or photography type
3. **Lighting**: Time of day, light quality
4. **Composition**: Framing, perspective
5. **Mood**: Atmosphere, feeling
6. **Details**: Colors, textures, elements

**Example Enhancement:**

User: "a cat"

Enhanced: "A fluffy orange tabby cat sitting on a sunny windowsill, warm afternoon light streaming in, soft focus background, cozy home interior, photorealistic style"

### Step 4: Generate Image

Call the appropriate MCP tool:

For full control:
```
generate_image(
  prompt="enhanced prompt here",
  model_tier="auto|flash|pro",
  aspect_ratio="1:1|16:9|9:16|21:9",
  number_of_images=1-4,  # Generate multiple variations
  safety_level="STRICT|MODERATE|PERMISSIVE|OFF",
  seed=12345,  # For reproducible results
  thinking_level="LOW|HIGH",
  use_grounding=false|true,
  output_path="/path/to/save.png"
)
```

### Using Reference Images

When user provides or wants to use a reference image:

**With uploaded file:**
```
generate_image(
  prompt="Your detailed prompt describing desired output",
  reference_file_uri="files/abc123",  # URI from upload_file
  reference_file_mime_type="image/png",
  model_tier="pro",  # Pro model recommended for reference-based generation
  ...other params
)
```

**With base64 data:**
```
generate_image(
  prompt="Your detailed prompt",
  reference_image_base64="iVBORw0KGg...",  # Base64 string
  reference_file_mime_type="image/jpeg",
  ...other params
)
```

**Tips for reference-based generation:**
- Use specific prompts describing what to change from the reference
- Pro model generally handles references better than Flash
- Reference helps maintain brand consistency for marketing materials

### Step 5: Handle Result

**On Success:**
1. Report the generated image details
2. If saved to file, provide the path
3. Offer refinement options if needed

**On Failure:**
1. Explain the error clearly
2. Suggest modifications to the prompt
3. Try alternative approaches if possible

### Step 6: Iterate if Needed

Common refinements:
- "Make it more [adjective]"
- "Change the [element]"
- "Try a different style"
- "Higher/lower quality"

## Quick Reference

### Styles
- **photo**: Photorealistic, professional photography
- **illustration**: Digital art, clean lines
- **painting**: Traditional art styles, brushstrokes
- **3d**: CGI, rendered graphics
- **sketch**: Hand-drawn, pencil art
- **cartoon**: Animated, stylized

### Quality Levels
- **fast**: Flash model, 2-3 seconds, 1024px
- **pro**: Pro model, 5-10 seconds, up to 4K

### Grounding
Enable for:
- Real landmarks and locations
- Famous people or characters
- Historical events
- Scientific accuracy

### Advanced Parameters

**Number of Images (1-4):**
- Generate multiple variations in one request
- Useful for A/B testing or exploring different interpretations
- Each image gets a separate output entry

**Safety Level:**
- `STRICT` (default): Maximum content filtering
- `MODERATE`: Balanced filtering for general use
- `PERMISSIVE`: Minimal filtering, more creative freedom
- `OFF`: No filtering (may be overridden by API)

**Seed (Reproducibility):**
- Use same seed value for consistent results
- Helpful for iterating on a specific generation
- Example: `seed=42` produces the same image each time

## Tips for Complex Generations

Load the prompt tips reference for detailed guidance:
```
@prompt-tips.md
```

Load aspect ratio guide for platform-specific recommendations:
```
@aspect-ratio-guide.md
```
