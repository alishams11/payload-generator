import argparse
from core.xss import generate_xss_payloads
from core.sqli import generate_sqli_payloads
from core.encoder import apply_encodings
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Security Payload Generator")
    parser.add_argument("--type", required=True, choices=["xss", "sqli"], help="Type of payload to generate")
    parser.add_argument("--param", required=True, help="Parameter name")
    parser.add_argument("--encode", nargs="*", choices=["url", "html", "base64"], help="Encodings to apply")
    args = parser.parse_args()

    if args.type == "xss":
        payloads = generate_xss_payloads(args.param)
    else:
        payloads = generate_sqli_payloads(args.param)

    all_payloads = []
    for payload in payloads:
        if args.encode:
            encoded_versions = apply_encodings(payload, args.encode)
            for encoded in encoded_versions:
                print(encoded)
                all_payloads.append(encoded)
                print("---")
        else:
            print(payload)
            all_payloads.append(payload)
            print("---")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/payloads_{args.type}_{args.param}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for p in all_payloads:
            f.write(p + "\n---\n")
    print(f"\n[+] Payloads saved to {filename}")

if __name__ == "__main__":
    main()
