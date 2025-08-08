# Payload Generator

**Payload Generator** is a security testing tool for generating common **XSS** and **SQL Injection** payloads with optional encodings.  
It is designed for penetration testers, bug bounty hunters, and security researchers to quickly create test payloads.

> ⚠️ This tool is for **educational and authorized security testing purposes only**.  
> Do not use it on systems without permission.

---

## Features
- **XSS Payload Generation**  
  Common reflected/stored XSS patterns.
- **SQL Injection Payload Generation**  
  Classic SQL injection strings.
- **Encodings**  
  Supports multiple encodings: `url`, `html`, `base64`.
- **CLI Support**  
  Fully controllable from the command line.
- **Output Saving**  
  Automatically saves payloads to `outputs/` with timestamped filenames.

---

## Project Structure
payload-generator/
├── core/
│ ├── xss.py # XSS payload generator
│ ├── sqli.py # SQLi payload generator
│ └── encoder.py # Encoding functions
├── outputs/ # Saved payload files
├── screenshots/ # CLI demo screenshots
├── wordlists/ # Future payload lists
├── main.py # Main CLI script
├── requirements.txt
├── README.md
└── LICENSE

## Installation
```bash
git clone https://github.com/<your-username>/payload-generator.git
cd payload-generator
pip install -r requirements.txt

##Usage
Generate XSS Payloads

python3 main.py --type xss --param search

Generate SQL Injection Payloads

python3 main.py --type sqli --param username

##Apply Encodings

You can apply one or more encodings:

python3 main.py --type xss --param search --encode url html
python3 main.py --type sqli --param username --encode base64

##Example Output
XSS Example

python3 main.py --type xss --param search --encode url html

Output:

Generated Payloads:

search%3D%3Cscript%3Ealert%281%29%3C/script%3E
search=&lt;script&gt;alert(1)&lt;/script&gt;
---
search%3D%27%3E%3Cimg%20src%3Dx%20onerror%3Dalert%281%29%3E
search=&#x27;&gt;&lt;img src=x onerror=alert(1)&gt;
...

SQLi Example

python3 main.py --type sqli --param username --encode base64

Output:

Generated Payloads:

dXNlcm5hbWU9JyBPUiAnMSc9JzE=
---
dXNlcm5hbWU9YWRtaW4nLS0=
...

Output Files

Payloads are automatically saved in:

outputs/payloads_TYPE_PARAM_TIMESTAMP.txt

Example:

outputs/payloads_xss_search_2025-08-08_15-30.txt

##License

MIT License - See LICENSE for details

##Disclaimer

This tool must only be used for legal and authorized testing.
The author is not responsible for any misuse or damage caused by this tool.
