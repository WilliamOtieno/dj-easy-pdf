import requests


def validate_image_url(url):
    try:
        response = requests.head(url, timeout=5)
        content_type = response.headers.get("content-type")
        if content_type is None:
            return False

        if "image" not in content_type:
            return False
        return True
    except requests.exceptions.RequestException:
        return False
