# Nano Banana

AI-powered image generation using Google's Nano Banana Pro (Gemini 3 Pro Image) and Nano Banana (Gemini 2.5 Flash Image) with professional 4K quality, smart model selection, and Google Search grounding.

## Features

- **Dual Model Support**:
  - **Pro Tier**: Uses `gemini-3-pro-image-preview` for professional 4K quality and complex prompt adherence
  - **Flash Tier**: Uses `gemini-2.5-flash-image` for lightning-fast (2-3s) generation and draft iterations
- **Smart Model Selection**: Automatically chooses the right model based on your prompt (e.g., "quick sketch" vs "4k professional photo")
- **Future-Ready Architecture**: Code prepared for multiple image generation (currently limited to 1 by Gemini API)
- **Reproducible Generation**: Use seed values for consistent results across multiple generations
- **Content Safety Controls**: Four-level safety filtering (STRICT, MODERATE, PERMISSIVE, OFF)
- **Google Search Grounding**: Generate factually accurate images using Google Search
- **Aspect Ratio Control**: Support for various formats (16:9, 1:1, 9:16, etc.)
- **Advanced Reasoning**: Configurable "thinking" levels for complex prompts
- **File Management**: Upload and manage files via Gemini Files API

## Required Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Gemini API key | Yes |

### Quick Setup

1. Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey)

2. Add to `~/.claude/settings.json`:
```json
{
  "env": {
    "GEMINI_API_KEY": "your-api-key-here"
  }
}
```

3. Restart Claude Code

### Verification

Test your configuration:
```bash
python ~/.claude/plugins/creative-designer/scripts/test_auth.py
```

Or try:
```
"Generate an image of a sunset over mountains"
```

## Usage Examples

### Basic Image Generation
```
"Generate an image of a golden retriever playing in autumn leaves"
```

### With Style
```
"Create a photorealistic product photo of a coffee cup on a wooden table"
```

### Specific Aspect Ratio
```
"Generate a 16:9 landscape image of a futuristic city at night"
```

### With Grounding (Factual Accuracy)
```
"Generate an accurate image of the Eiffel Tower at sunset with grounding enabled"
```

### Quick Generation
```
"Quick sketch of a robot"
```

### Reproducible Generation
```
"Generate an image of a sunset with seed 42 for consistent results"
```

### Custom Safety Level
```
"Generate artistic portrait with moderate safety filtering"
```

### With Reference Image
Generate images inspired by reference materials:

```
"Use this product photo as reference and generate a similar composition with a coffee mug"
```

The plugin supports two ways to provide reference images:
1. **Upload a file first** using `upload_file`, then use the returned URI
2. **Provide base64-encoded image data** directly in the prompt

For file-based references:
```
"Upload reference.jpg for style matching"
# Then after upload succeeds:
"Generate an image with the same style as the uploaded reference"
```

## Advanced Parameters

### Number of Images
**Current Status**: The Gemini image generation API currently only supports generating 1 image per request. The `number_of_images` parameter is implemented in the code for future compatibility but is limited to 1 by the API.

Note: Google's separate [Imagen API](https://ai.google.dev/gemini-api/docs/imagen) does support generating multiple images (1-4) per request if you need that capability.

### Safety Filtering
Control content filtering with four levels:
- **STRICT** (default): Maximum filtering, blocks most potentially sensitive content
- **MODERATE**: Balanced filtering, suitable for general use
- **PERMISSIVE**: Minimal filtering, more creative freedom
- **OFF**: No filtering (may be overridden by API based on account tier)

### Seed Value
Ensure reproducible results:
- `seed`: Integer value for deterministic generation
- Same seed + same prompt = consistent output
- Useful for iterating on specific results

## Model Selection

| Model | Speed | Resolution | Best For |
|-------|-------|------------|----------|
| Flash | 2-3 seconds | Up to 1024px | Quick iterations, drafts, concepts |
| Pro | 5-10 seconds | Up to 4K | Final assets, product photos, detailed work |

### Auto-Selection Keywords

**Triggers Pro Model:**
- professional, 4k, high quality, detailed, photorealistic
- ultra, premium, studio, commercial, product photo
- portfolio, print, publication, magazine, advertisement

**Triggers Flash Model:**
- quick, fast, sketch, draft, concept
- rough, preview, test, iterate, simple

## Aspect Ratios

| Ratio | Dimensions | Use Case |
|-------|------------|----------|
| 1:1 | 1024x1024 | Social media, Instagram, profile pictures |
| 16:9 | 1920x1080 | YouTube thumbnails, presentations, desktop |
| 9:16 | 1080x1920 | Mobile wallpapers, Instagram Stories, TikTok |
| 21:9 | 2520x1080 | Cinematic, ultrawide displays |
| 4:3 | 1365x1024 | Classic photography, documents |
| 3:4 | 1024x1365 | Portrait orientation |
| 2:1 | 2048x1024 | Panoramic, website headers |

## Troubleshooting

### "Missing GEMINI_API_KEY"
1. Get your key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Add to settings.json as shown above
3. Restart Claude Code

### "API request failed"
- Check your internet connection
- Verify your API key is valid
- Check [Google AI Studio](https://aistudio.google.com/) for service status

### Image Not Generating
- Try a more specific prompt
- Check for content policy violations
- Use grounding for factual subjects

## More Information

- [Nano Banana MCP Server](https://github.com/zhongweili/nanobanana-mcp-server) - Reference implementation
- [Google AI Studio](https://aistudio.google.com/) - Get API keys and test models
- [Gemini API Documentation](https://ai.google.dev/docs) - Full API reference
