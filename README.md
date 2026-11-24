# odoo_mcp_server_mpi

Odoo MCP Server (`mcp_server`) maintained and hardened by **MPI GmbH, Michael Plöckinger** ([https://mpi-erp.at](https://mpi-erp.at)).

## Odoo.sh Deployment

Odoo.sh installs Python dependencies from `requirements.txt` at the **repository root**:

```text
authlib>=1.6.12,<1.7.0
defusedxml
packaging
```

## Security Hardening Defaults

- **Rate limiting** (`mcp_server.enable_rate_limiting`) is **enabled by default** (300 req/min per user per worker).
- **OAuth 2.1** (`mcp_server.enable_oauth`) is **disabled by default** (API keys only until an administrator enables OAuth; when OAuth is enabled, Dynamic Client Registration `/mcp/oauth/register` can also be toggled via `mcp_server.allow_oauth_dcr` and browser origins should be restricted via `mcp_server.allowed_origins`).
- **Chatter `post_message`** restricts posts to internal notes (`subtype="note"`, no `partner_ids`) by default (`mcp_server.allow_external_chatter_messages = False`) to prevent accidental customer emails.
- **Attachment download links** keep a 1-hour default TTL (`mcp_server.link_ttl_hours = 1`) and can be disabled altogether via `mcp_server.allow_attachment_download_links`.

## License

See [LICENSE](LICENSE) (`OPL-1`).
