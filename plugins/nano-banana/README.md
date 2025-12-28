# Nano Banana Pro Plugin

AI-powered image generation using Google's Nano Banana Pro (Gemini 3 Pro Image) with professional 4K quality, smart model selection, and Google Search grounding.

## Features

- **Multi-Model Support**: Choose between Flash (fast, 2-3s) and Pro (high-quality, 4K)
- **Smart Model Selection**: Automatically picks the best model based on your prompt
- **Multiple Aspect Ratios**: 1:1, 16:9, 9:16, 21:9, 4:3, and more
- **Google Search Grounding**: Generate factually accurate images with real-world knowledge
- **Advanced Reasoning**: Configurable thinking levels for complex generations
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
python ~/.claude/plugins/nano-banana/scripts/test_auth.py
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
