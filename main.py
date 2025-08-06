import argparse
from core.xss import generate_xss_payloads
from core.sqli import generate_sqli_payloads
from core.encoder import apply_encodings

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

if __name__ == "__main__":
    main()
