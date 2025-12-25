---
name: generate-art
description: Create freeform ASCII art from text descriptions
args:
  - name: description
    description: Description of the ASCII art to create
    required: true
  - name: size
    description: "Approximate size: small, medium, large (default: medium)"
    required: false
    flag: true
  - name: style
    description: "Art style: detailed, minimal, geometric, retro (default: detailed)"
    required: false
    flag: true
---

# Generate ASCII Art

Create freeform ASCII art from natural language descriptions. Generate illustrations, symbols, scenes, and decorative elements using text characters.

## Size Guidelines

### small
Compact art, roughly 5-10 lines:
```
  /\_/\
 ( o.o )
  > ^ <
```

### medium (default)
Standard art, roughly 10-20 lines:
```
    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
```

### large
Detailed art, 20+ lines:
```
                                     .
                                    / V\
                                  / `  /
                                 <<   |
                                 /    |
                               /      |
                             /        |
                           /    \  \ /
                          (      ) | |
                  ________|   _/_  | |
                <__________\______)\__)
```

## Style Options

### detailed (default)
Rich detail with shading and texture:
```
       .---.
      /     \
     | () () |
      \  ^  /
       |||||
       |||||
    .-'-'-'-'-.
   /           \
  |             |
  |             |
   \           /
    '-._____.-'
```

### minimal
Clean lines, simple shapes:
```
   ___
  |   |
  |   |
  |___|
   | |
  /   \
```

### geometric
Sharp angles, patterns:
```
    /\
   /  \
  /    \
 /______\
 \      /
  \    /
   \  /
    \/
```

### retro
Classic computer art feel:
```
 ################
 #              #
 #  ##      ##  #
 #              #
 #   ########   #
 #              #
 ################
```

## Common Subjects

The skill works well with:
- **Animals**: cats, dogs, birds, fish, dragons
- **Objects**: rockets, computers, houses, trees, vehicles
- **Symbols**: hearts, stars, arrows, checkmarks
- **Scenes**: landscapes, cityscapes, space
- **Characters**: robots, faces, stick figures
- **Decorative**: borders, dividers, flourishes

## Workflow

**Step 1: Parse the request**
- Understand what subject to draw
- Note size preference (default: medium)
- Note style preference (default: detailed)

**Step 2: Plan the art**
- Determine key features to represent
- Plan the character palette (which ASCII characters to use)
- Consider symmetry and proportions

**Step 3: Create the art**
- Build the artwork line by line
- Use appropriate characters for shading and detail
- Maintain consistent style throughout

**Step 4: Output the result**
- Display in a code block
- Ensure proper alignment
- Center the art if appropriate

## Character Palette Reference

| Purpose | Characters |
|---------|------------|
| Shading (light to dark) | `.` `:` `-` `=` `+` `*` `#` `%` `@` |
| Curves | `(` `)` `/` `\` `|` `_` |
| Blocks | `█` `▓` `▒` `░` `■` `□` |
| Lines | `─` `│` `┌` `┐` `└` `┘` |
| Decoration | `*` `~` `^` `•` `°` `·` |

## Error Handling

**Vague description**: "Could you be more specific? For example: 'a cat sitting' or 'a rocket launching into space'"

**Complex scene**: "That's a complex scene! I'll focus on the main subject. For detailed scenes, consider generating elements separately."

**Inappropriate content**: "I can't create that. Let's try something else - how about [alternative suggestion]?"

## Examples

**Basic animal:**
```
/generate-art "a cute owl"
```

**With size:**
```
/generate-art "a rocket ship" --size large
```

**With style:**
```
/generate-art "a heart" --style geometric
```

**Scene:**
```
/generate-art "mountains with a sunset" --size large --style minimal
```

**Symbol:**
```
/generate-art "a checkmark" --size small --style minimal
```

**Decorative:**
```
/generate-art "a decorative divider with stars"
```

## Tips

- **Start simple**: Basic shapes and animals work best
- **Be specific**: "a cat sitting" is better than just "a cat"
- **Use size wisely**: Small for inline decorations, large for splash screens
- **Match style to purpose**: Minimal for professional docs, detailed for fun
- **Iterate**: Request variations if the first result isn't quite right
- **Combine with other skills**: Use generate-box to frame your art!
