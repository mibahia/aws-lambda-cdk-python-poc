from io import BytesIO
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def get_data_from_url(url: str) -> bytes:
    try:
        request = Request(url=url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request) as response:
            data = response.read()
        return BytesIO(data)
    except HTTPError as e:
        print(f"Connection error: {e}")
