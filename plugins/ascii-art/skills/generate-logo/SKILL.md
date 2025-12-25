---
name: generate-logo
description: Generate large ASCII text logos in various font styles (figlet-style)
args:
  - name: text
    description: The text to convert to an ASCII logo
    required: true
  - name: style
    description: "Font style: standard, block, slant, banner, small (default: standard)"
    required: false
    flag: true
  - name: width
    description: Maximum character width (default: 80)
    required: false
    flag: true
---

# Generate ASCII Logo

Create large, eye-catching ASCII text logos similar to figlet/toilet CLI tools. Perfect for CLI tool banners, README headers, and terminal splash screens.

## Available Font Styles

### standard (default)
Classic ASCII art letters with clean lines:
```
  ____ _                 _
 / ___| | __ _ _   _  __| | ___
| |   | |/ _` | | | |/ _` |/ _ \
| |___| | (_| | |_| | (_| |  __/
 \____|_|\__,_|\__,_|\__,_|\___|
```

### block
Bold, blocky letters using block characters:
```
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
```

### slant
Italicized/slanted letters for a dynamic feel:
```
   ________                __
  / ____/ /___ ___  ______/ /__
 / /   / / __ `/ / / / __  / _ \
/ /___/ / /_/ / /_/ / /_/ /  __/
\____/_/\__,_/\__,_/\__,_/\___/
```

### banner
Large, simple banner-style letters:
```
#####  #        #    #     # ##### ######
#    # #       # #   #     # #    # #
#    # #      #   #  #     # #    # #####
#    # #     #######  #   #  #    # #
#    # #     #     #   # #   #    # #
#####  ##### #     #    #    ##### ######
```

### small
Compact 3-line letters for inline use:
```
 ___ _                _
/ __| |__ _ _  _ __ _| |___
\__ \ / _` | || / _` |  _/ _ \
|___/_\__,_|\_,_\__,_|\__\___/
```

## Workflow

**Step 1: Parse the input**
- Extract the text to convert
- Determine the font style (default to "standard" if not specified)
- Note any width constraints

**Step 2: Generate the ASCII logo**
- Render each character using the appropriate font style patterns
- Maintain proper spacing between characters
- Ensure consistent height across all characters in the output

**Step 3: Apply width constraints**
- If the result exceeds the specified width, inform the user
- For very long text, suggest breaking into multiple lines

**Step 4: Output the result**
- Display the ASCII logo in a code block for proper formatting
- Preserve monospace alignment

## Error Handling

**Empty text**: "Please provide text to convert to an ASCII logo."

**Unsupported characters**: "Some characters couldn't be rendered. Sticking to A-Z, 0-9, and common punctuation works best."

**Text too long**: "The text is quite long for the specified width. Consider using the 'small' style or breaking it into multiple lines."

## Examples

**Basic usage:**
```
/generate-logo Hello
```

**With style:**
```
/generate-logo "My CLI Tool" --style block
```

**With width constraint:**
```
/generate-logo AWESOME --style slant --width 60
```

## Tips

- Use **block** style for maximum visual impact in terminal splash screens
- Use **small** style for README headers where space is limited
- Use **slant** style for a modern, dynamic appearance
- Uppercase letters generally render more consistently
- Stick to alphanumeric characters for best results
