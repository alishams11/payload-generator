import urllib.parse
import html
import base64
from typing import List

def url_encode(payload: str) -> str:
    return urllib.parse.quote(payload)

def html_encode(payload: str) -> str:
    return html.escape(payload)

def base64_encode(payload: str) -> str:
    return base64.b64encode(payload.encode()).decode()

def apply_encodings(payload: str, types: List[str]) -> List[str]:
    results = []

    for enc_type in types:
        if enc_type == "url":
            results.append(url_encode(payload))
        elif enc_type == "html":
            results.append(html_encode(payload))
        elif enc_type == "base64":
            results.append(base64_encode(payload))
        else:
            results.append(f"[Unsupported encoding: {enc_type}]")

    return results
