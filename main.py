from core.sqli import generate_sqli_payloads

def main():
    print("=== Payload Generator ===")
    attack_type = input("Select type (xss / sqli): ").strip().lower()
    param = input("Enter the parameter name (e.g., username): ").strip()

    if attack_type == "xss":
        from core.xss import generate_xss_payloads
        payloads = generate_xss_payloads(param)
    elif attack_type == "sqli":
        payloads = generate_sqli_payloads(param)
    else:
        print("[!] Invalid attack type.")
        return

    print("\nGenerated Payloads:\n")
    for p in payloads:
        print(p)

if __name__ == "__main__":
    main()
