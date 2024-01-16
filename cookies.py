
# built-in
from pathlib import Path

THIS_PATH = Path.cwd()
COOKIES_DATA_PATH = Path.joinpath(THIS_PATH, "cookies.txt")
SSO_COOKIE_URL = "https://ca.account.sony.com/api/v1/ssocookie"


def get_cached_npsso_code():
    with open(COOKIES_DATA_PATH, "r") as cookies_file_obj:
        return cookies_file_obj.read().replace('"', "")
