# Testing Checklist

## Manual Testing Scenarios

### Test 1: Basic Edit
1. Create test file: `echo "This is a game-changing approach that will revolutionize your workflow. What do you think?" > test.txt`
2. Run: `/edit-draft @test.txt`
3. Verify: Hype words removed, ending more specific, uses default style guide

### Test 2: Custom Style Guide
1. Create custom guide: `cp plugins/creative-writing/examples/my-style-guide.md my-guide.md`
2. Run: `/edit-draft --style-guide my-guide.md @test.txt`
3. Verify: Uses custom guide (technical tone), not default

### Test 3: Settings File
1. Create: `.claude/creative-writing.local.md`
2. Add frontmatter: `custom_style_guide: my-guide.md`
3. Run: `/edit-draft @test.txt` (no --style-guide flag)
4. Verify: Uses custom guide from settings

### Test 4: Review Without Rewriting
1. Run: `/review-writing @test.txt`
2. Verify: Returns feedback organized by category, no rewrite

### Test 5: Generate Content
1. Run: `/generate-content`
2. Enter: "Blog post about git worktrees for technical audience"
3. Verify: Generates content following style guide, asks clarifying questions if needed

### Test 6: Improve Opening
1. Create: `echo "As an expert in software development, I'm excited to share revolutionary insights that will transform your coding." > opening-test.txt`
2. Run: `/improve-opening @opening-test.txt`
3. Verify: Removes performative authority, adds honesty

### Test 7: Strengthen Ending
1. Create: `echo "In conclusion, this approach has many benefits. What do you think? Let me know in the comments!" > ending-test.txt`
2. Run: `/strengthen-ending @ending-test.txt`
3. Verify: Replaces generic CTA with specific question

### Test 8: Remove AI Tells
1. Create file with em-dashes, colons, hype words
2. Run: `/remove-ai-tells @file.txt`
3. Verify: Annotates all changes, shows before/after

### Test 9: Generate Style Guide
1. Run: `/generate-style-guide`
2. Answer questionnaire
3. Verify: Creates `my-style-guide.md` with personalized content

### Test 10: Error Handling
1. Run: `/edit-draft --style-guide nonexistent.md @test.txt`
2. Verify: Shows warning, falls back to default
3. Run: `/edit-draft` with very short content (< 50 words)
4. Verify: Shows helpful message about content length

## Integration Testing

### Test 11: Full Workflow
1. Write draft with AI patterns
2. `/review-writing` to get feedback
3. `/improve-opening` for introduction
4. `/remove-ai-tells` to clean patterns
5. `/strengthen-ending` for conclusion
6. `/edit-draft` for final polish
7. Verify: Each step works, cumulative improvements

### Test 12: Settings Override
1. Set custom guide in `.claude/creative-writing.local.md`
2. Run skill with `--style-guide` parameter pointing to different guide
3. Verify: Parameter overrides settings file

## Success Criteria

- [ ] All skills load correct style guide (default, settings, or parameter)
- [ ] Smart chunking loads only relevant sections
- [ ] Error messages are helpful and actionable
- [ ] Generated content follows style principles
- [ ] Reviews provide specific, actionable feedback
- [ ] Custom style guides work seamlessly
- [ ] Settings file correctly sets defaults
- [ ] Parameter overrides work as expected
