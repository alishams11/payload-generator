import argparse
from core.xss import generate_xss_payloads
from core.sqli import generate_sqli_payloads
from core.encoder import apply_encodings

import os
from datetime import datetime

def save_to_file(payloads, payload_type, param):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"outputs/payloads_{payload_type}_{param}_{timestamp}.txt"
    os.makedirs("outputs", exist_ok=True)
    try:
        with open(filename, "w") as f:
            for payload in payloads:
                if isinstance(payload, list):
                    for p in payload:
                        f.write(p + "\n")
                else:
                    f.write(payload + "\n")
        print(f"\n[+] Payloads saved to {filename}")
    except Exception as e:
        print(f"[!] Error saving file: {e}")


def main():
    parser = argparse.ArgumentParser(description="Payload Generator for XSS and SQLi")
    parser.add_argument('--type', required=True, choices=['xss', 'sqli'], help='Type of vulnerability payload (xss/sqli)')
    parser.add_argument('--param', required=True, help='Parameter name to inject')
    parser.add_argument('--encode', nargs='*', choices=['url', 'html', 'base64'], help='Encoding options (url, html, base64)')

    args = parser.parse_args()

    if args.type == "xss":
        payloads = generate_xss_payloads(args.param)
    elif args.type == "sqli":
        payloads = generate_sqli_payloads(args.param)
    else:
        print("[!] Invalid type selected.")
        return

    print("\nGenerated Payloads:\n")

    for payload in payloads:
        if args.encode:
            encoded_versions = apply_encodings(payload, args.encode)
            for ep in encoded_versions:
                print(ep)
            print("---")
        else:
            print(payload)
            save_to_file(payloads, args.type, args.param)
if __name__ == "__main__":
    main()
