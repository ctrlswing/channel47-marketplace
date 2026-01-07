# Migration Guide: v3.0.0 → v3.1.0

## Summary

Version 3.1.0 changes how the MCP server is distributed, but **requires no action from users**.

## What Changed

### Before (v3.0.0)
- MCP server bundled with plugin in `server/` directory
- Plugin executes local `server/index.js`
- npm dependencies in plugin package.json
- Manual `npm install` required

### After (v3.1.0)
- MCP server published to npm as `@channel47/google-ads-mcp`
- Plugin executes `npx @channel47/google-ads-mcp@latest`
- Server auto-installed on first use
- Dependencies managed automatically by npx

## Migration Steps

### For Plugin Users: NONE

When you update to v3.1.0:
1. Plugin automatically updates `.mcp.json`
2. Next activation downloads MCP server via npx (3-5 seconds, one-time)
3. Server caches locally for subsequent uses
4. Everything else works identically

**No configuration changes needed. No workflow changes. Just update and use.**

### For Plugin Developers

If you've cloned the plugin repository:

1. **Update from marketplace or git pull**
   ```bash
   cd /path/to/channel47-marketplace
   git pull
   ```

2. **Note structural changes:**
   - `server/` directory removed from plugin
   - Skills remain in `skills/` directory
   - Hook validation unchanged in `.claude/hooks/`

3. **To test server changes:**
   - Clone [google-ads-mcp-server](https://github.com/channel47/google-ads-mcp-server)
   - Work on server in separate repository
   - Update `.mcp.json` temporarily to point to local server:
     ```json
     {
       "mcpServers": {
         "google-ads-nodejs": {
           "command": "node",
           "args": ["/path/to/google-ads-mcp-server/server/index.js"]
         }
       }
     }
     ```
   - Remember to restore npx command before committing

## What Stays the Same

✅ **Environment variables** (unchanged)
✅ **Skills** (unchanged - 9 skill files)
✅ **Hook validation** (unchanged)
✅ **Tool names and parameters** (unchanged)
✅ **Workflow** (unchanged)
✅ **OAuth setup** (unchanged)

## What's Different

### Distribution Architecture

**Old:**
```
Plugin Directory
├── server/        (MCP server code)
├── skills/        (Skills)
└── .mcp.json      (Points to local server)
```

**New:**
```
Plugin Directory
├── skills/        (Skills only)
└── .mcp.json      (Points to npm package)

NPM Package (@channel47/google-ads-mcp)
├── server/        (MCP server code)
└── dependencies   (Auto-installed)
```

### Version Independence

- **Server version**: 1.0.0 (independent npm package)
- **Plugin version**: 3.1.0 (marketplace release)

Server and plugin can now be updated independently:
- Server bug fixes → npm publish → users get update automatically (@latest)
- Plugin skill updates → marketplace publish → users get new skills

## Benefits

### For Users

1. **Zero-Click Dependency Management**: No manual `npm install` required
2. **Automatic Updates**: Using @latest ensures you get server bug fixes automatically
3. **Consistent Cross-Platform**: Works identically on macOS, Linux, and Windows
4. **Smaller Plugin Size**: Plugin only contains skills and configuration, not server code
5. **Clear Error Messages**: npm errors are more informative than silent failures

### For Maintainers

1. **Separation of Concerns**: Server code lives in dedicated repo, plugin contains only Claude Code-specific files
2. **Independent Versioning**: Can update server without re-publishing plugin
3. **Standard Node.js Workflow**: Uses familiar npm publish process
4. **Easier Testing**: Server can be tested independently with MCP Inspector

## Troubleshooting

### Issue: "Cannot find package @channel47/google-ads-mcp"

**Cause:** npm registry issue or network problem

**Fix:**
1. Check network connection
2. Verify npm package published: `npm view @channel47/google-ads-mcp`
3. Try clearing npx cache: `rm -rf ~/.npm/_npx`

### Issue: Slow first activation

**Expected behavior:** First activation takes 3-5 seconds to download npm package.

**Subsequent activations:** Instant (cached by npx)

**Not an issue** - This is normal npx behavior.

### Issue: "Permission denied" when running npx

**Cause:** Executable permissions not set on server/index.js

**Fix:** This is a server package issue. Report at [server repository](https://github.com/channel47/google-ads-mcp-server/issues)

### Issue: Environment variables not recognized

**Cause:** Environment inheritance issue

**Fix:** Environment variables should work identically to v3.0.0. If not:
1. Verify variables are set: `echo $GOOGLE_ADS_DEVELOPER_TOKEN`
2. Restart Claude Code
3. Check Claude Code logs for errors

## Rollback

### If you need to revert to v3.0.0:

**Option 1: Via Marketplace**
1. Plugin marketplace → Google Ads Specialist → Version history → v3.0.0
2. Click "Install v3.0.0"

**Option 2: Manual**
```bash
cd ~/.claude/plugins/google-ads-specialist
git checkout v3.0.0
```

The server will be bundled locally again, and everything works as before.

## Testing the Migration

### Verification Checklist

After updating to v3.1.0, verify:

- [ ] Plugin activates (check Claude Code logs)
- [ ] MCP server starts via npx (first time: 3-5 seconds)
- [ ] `list_accounts` tool works
- [ ] `query` tool works with skill reference
- [ ] `mutate` tool works (dry_run default)
- [ ] Hook validation prevents queries without skill
- [ ] Environment variables recognized
- [ ] Subsequent activations are instant (<1 second)

### Performance Comparison

| Metric | v3.0.0 | v3.1.0 (First Use) | v3.1.0 (Cached) |
|--------|--------|-------------------|-----------------|
| Plugin Size | ~500KB | ~100KB | ~100KB |
| Activation Time | <1s | 3-5s | <1s |
| Dependencies | Manual install | Auto-install | Cached |
| Server Updates | Plugin update | npm publish | npm publish |

## Questions?

- **General questions:** See updated [README.md](README.md)
- **Setup questions:** See updated [GETTING_STARTED.md](GETTING_STARTED.md)
- **Server development:** [Server Repository](https://github.com/channel47/google-ads-mcp-server)
- **Plugin issues:** [Marketplace Repository Issues](https://github.com/ctrlswing/channel47-marketplace/issues)
- **Server issues:** [Server Repository Issues](https://github.com/channel47/google-ads-mcp-server/issues)

## Summary

**Bottom line:** Update to v3.1.0 and everything works exactly the same, but with automatic server installation and independent server updates. No action required from users.

**Recommendation:** Update immediately to benefit from:
- Automatic server updates
- Smaller plugin size
- Faster future plugin updates
- Independent server development cycle
