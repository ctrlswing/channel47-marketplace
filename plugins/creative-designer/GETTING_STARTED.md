# Getting Started with Nano Banana Pro Plugin

This guide walks through the complete setup process for AI-powered image generation.

## Prerequisites

### 1. Google Account
- Any Google account works
- No special access or approvals needed

### 2. API Key
- Free to obtain from Google AI Studio
- Generous free tier included

## Installation

Install the plugin from the channel47 marketplace:

```bash
/plugin install creative-designer@channel47
```

## Configuration

### Step 1: Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Step 2: Configure Claude Code

Add the API key to your Claude Code settings:

**Option A: Via Settings File**

Edit `~/.claude/settings.json`:

```json
{
  "env": {
    "GEMINI_API_KEY": "your-api-key-here"
  }
}
```

**Option B: Via Setup Wizard**

Run the interactive setup:
```
/creative-designer:setup
```

### Step 3: Restart Claude Code

After updating settings, restart Claude Code:
1. Exit Claude Code (Ctrl+C or Cmd+Q)
2. Run `claude`
3. Use `/resume` to return to your session

### Step 4: Verify Installation

Test your configuration:

```
"Generate a simple test image"
```

Or run the test script:
```bash
python ~/.claude/plugins/cache/channel47/creative-designer/*/scripts/test_auth.py
```

## Usage Examples

### Basic Generation

```
"Generate an image of a cozy coffee shop interior"
```

### With Style Specification

```
"Create a watercolor illustration of a mountain landscape"
```

### Professional Quality

```
"Generate a professional 4K product photo of headphones on a marble surface"
```

### Mobile Format

```
"Create a 9:16 portrait image for Instagram Stories of a sunset beach scene"
```

### With Grounding

```
"Generate an accurate image of the Golden Gate Bridge at dawn, use grounding"
```

### Quick Sketches

```
"Quick sketch of a robot assistant"
```

### Reference-Based Generation

Generate images inspired by reference materials to maintain consistent style or composition:

#### Option 1: Upload Reference File

1. Upload your reference image:
```
"Upload my-style-reference.jpg to use for generation"
```

2. Generate with reference:
```
"Generate a product photo similar to the uploaded reference, but with a water bottle instead of a coffee mug"
```

#### Option 2: Direct Base64 (Advanced)

For programmatic use, you can provide base64-encoded image data directly. The reference image helps maintain:
- Consistent visual style
- Similar composition and framing
- Brand consistency across generated images

## Available Tools

### generate_image
Full-featured image generation with all options:
- Model selection (flash/pro/auto)
- Aspect ratio control
- Thinking level configuration
- Google Search grounding
- File output

### list_files
View files uploaded to Gemini Files API:
- File names and metadata
- Upload timestamps
- File states

### upload_file
Upload files for use in generation:
- Images, videos, PDFs
- Reference materials
- Style guides

### delete_file
Remove uploaded files:
- Free up storage
- Manage file library

## Model Selection Guide

### Use Flash Model When:
- Iterating on concepts quickly
- Creating rough drafts
- Testing prompt ideas
- Time is critical
- Resolution up to 1024px is sufficient

### Use Pro Model When:
- Creating final assets
- Needing 4K resolution
- Requiring maximum detail
- Commercial/professional use
- Using Google Search grounding

## Aspect Ratio Guide

| Use Case | Recommended Ratio |
|----------|-------------------|
| Instagram Post | 1:1 |
| Instagram Story | 9:16 |
| YouTube Thumbnail | 16:9 |
| TikTok | 9:16 |
| Website Header | 2:1 |
| Desktop Wallpaper | 16:9 |
| Mobile Wallpaper | 9:16 |
| Presentation Slide | 16:9 |
| Movie Poster | 3:4 |
| Cinematic | 21:9 |

## Tips for Better Results

### Prompt Engineering

1. **Be Specific**: Include details about style, lighting, composition
2. **Use Adjectives**: Describe colors, textures, moods
3. **Specify Context**: Mention time of day, location, atmosphere
4. **Reference Styles**: Mention art styles, photographers, or techniques

### Example Prompts

**Good:**
```
"A cozy coffee shop interior at golden hour, warm lighting streaming through
large windows, exposed brick walls, wooden tables with steaming cups,
potted plants, photorealistic style"
```

**Better:**
```
"Professional commercial photography of a modern coffee shop interior,
shot during golden hour with warm natural lighting streaming through
floor-to-ceiling windows, featuring exposed brick walls, reclaimed wood
tables, artisanal coffee cups with steam, lush green potted plants,
shallow depth of field, 4K quality"
```

## Troubleshooting

### "Missing GEMINI_API_KEY"

**Cause:** Environment variable not set

**Solution:**
1. Add key to `~/.claude/settings.json`
2. Restart Claude Code

### "API request failed with status 403"

**Cause:** Invalid or expired API key

**Solution:**
1. Generate new key at [Google AI Studio](https://aistudio.google.com/apikey)
2. Update settings.json
3. Restart Claude Code

### "No image data in response"

**Cause:** Content policy violation or generation failure

**Solution:**
1. Modify prompt to avoid policy violations
2. Try simpler prompt first
3. Check Gemini service status

### Images Look Different Than Expected

**Tips:**
1. Use more specific prompts
2. Try different styles (photo, illustration, etc.)
3. Enable grounding for factual subjects
4. Use Pro model for higher quality

## Rate Limits

Google Gemini API has generous free tier limits:
- Free tier: 60 requests per minute
- Paid tier: Higher limits available

The MCP server handles rate limiting automatically.

## Next Steps

- Explore different aspect ratios for various platforms
- Try grounding for factually accurate images
- Experiment with style modifiers
- Upload reference images for inspiration

For more examples and guides, visit [channel47.dev/plugins/creative-designer](https://channel47.dev/plugins/creative-designer)
