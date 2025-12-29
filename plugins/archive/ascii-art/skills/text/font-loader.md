# Font Reference Loader

Maps font style names to font definition files.

## Font File Mapping

| Style Name | File Path | Best For |
|------------|-----------|----------|
| standard | ../../assets/fonts/standard.md | Classic ASCII art, general use |
| block | ../../assets/fonts/block.md | Bold impact, splash screens |
| slant | ../../assets/fonts/slant.md | Dynamic, modern appearance |
| banner | ../../assets/fonts/banner.md | Simple, hash-based letters |
| small | ../../assets/fonts/small.md | Compact, space-constrained |

## Loading Instructions

When `--style` is specified:
1. Look up the style name in the mapping above
2. Read the corresponding font file for character patterns
3. Use those patterns to render the text

## Font File Structure

Each font file contains character definitions:

```
# [Font Name]

## A
[ASCII pattern for letter A]

## B
[ASCII pattern for letter B]

...
```

Extract the pattern for each character in the input text and assemble into the logo.

## Default Behavior

If no `--style` specified: Use standard font.

If style not found in mapping: Show error and list available styles.
