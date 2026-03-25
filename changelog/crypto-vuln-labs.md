# Changelog — Crypto Vulnerability Labs

Path: `/crypto-vuln-labs/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-11

### [feature] Created full 10-lab Python Crypto Vulnerability Labs section
- `crypto-vuln-labs/index.html` — hub page with dark-theme card grid, 5 vulnerability categories
- `crypto-vuln-labs/shared.css` — shared dark-theme stylesheet (164 lines)
- `crypto-vuln-labs/shared.js` — shared utilities (19 lines)
- Lab 01 `01-hardcoded-secrets.html` — identify hardcoded API keys and secrets in Python code (138 lines)
- Lab 02 `02-weak-prng.html` — spot weak random number generator usage (136 lines)
- Lab 03 `03-broken-password-hashing.html` — find broken/insecure password hashing (137 lines)
- Lab 04 `04-ecb-mode.html` — identify ECB mode encryption misuse (136 lines)
- Lab 05 `05-unauthenticated-encryption.html` — catch unauthenticated encryption vulnerabilities (138 lines)
- Lab 06 `06-weak-key-derivation.html` — find weak key derivation functions (136 lines)
- Lab 07 `07-timing-attack.html` — spot timing attack vulnerabilities in comparison code (136 lines)
- Lab 08 `08-insecure-tls.html` — identify insecure TLS configuration (141 lines)
- Lab 09 `09-predictable-iv.html` — catch predictable initialization vectors (141 lines)
- Lab 10 `10-broken-cipher.html` — find fundamentally broken cipher implementations (140 lines)
- Lab format: read real Python code, identify the most critical flaw (no coding required)
- Categories covered: Secrets Management, Hashing, Encryption, Protocol, Algorithm
- Added Crypto Vuln Labs card to main `index.html`
