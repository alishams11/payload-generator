from core.xss import generate_xss_payloads

def main():
    print("=== XSS Payload Generator ===")
    param = input("Enter the parameter name (e.g., search): ").strip()
    payloads = generate_xss_payloads(param)

    print("\nGenerated XSS Payloads:\n")
    for p in payloads:
        print(p)

if __name__ == "__main__":
    main()
