# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

This project uses automated secret scanning via Gitleaks on every push and pull request.

If you discover a security vulnerability, **do not open a public issue**. Instead:
- Open a draft PR with the fix, or
- Contact the repository owner directly

## Secret Scanning

- Pre-commit hooks with Gitleaks prevent secrets from being committed
- CI pipeline runs Gitleaks on every push and pull request
- If a secret is detected, the pipeline fails and the commit is blocked

## Best Practices

- Never commit `.env` files, API keys, passwords, or credentials
- Use environment variables or secret management services
- Keep dependencies updated
- Run `gitleaks detect` locally before pushing
