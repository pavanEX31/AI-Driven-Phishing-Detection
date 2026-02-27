import urllib.parse

def extract_features(url):
    parsed_url = urllib.parse.urlparse(url)

    features = {
        "url_length": len(url),
        "num_special_chars": sum(1 for c in url if c in "-._?&=/#"),
        "has_https": 1 if parsed_url.scheme == "https" else 0,
        "contains_suspicious_word": 1 if any(
            word in url.lower() for word in ["login", "verify", "bank", "secure"]
        ) else 0,
        "num_digits": sum(c.isdigit() for c in url),
        "has_ip_address": 1 if parsed_url.netloc.replace(".", "").isdigit() else 0
    }

    return features