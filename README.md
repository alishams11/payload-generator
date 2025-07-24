# Payload Generator 🔥

A simple CLI tool to generate automated security payloads for testing purposes in bug bounty and penetration testing.

## 🔹 Features (Planned)
- XSS payload generator
- SQL Injection payload generator
- Multiple encoding options (URL, HTML, Base64)
- Customizable parameter names
- CLI support
- Output to text files

## 📂 Structure
- `core/` – logic for payload generation and encoding
- `outputs/` – generated payload files
- `wordlists/` – optional custom payload lists
- `screenshots/` – tool demo images

## 💡 Usage (soon):
```bash
python3 main.py --type xss --param username --encode url html

