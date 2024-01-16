
# built-in
import os
import sys
import json
import logging
import subprocess
import webbrowser
import importlib.util as importlib_utils

# internal
from cookies import SSO_COOKIE_URL, COOKIES_DATA_PATH

# logger = logging.getLogger(__name__)

PSNAWP_PACKAGE_NAME = "PSNAWP"


def ensure_psnawp_is_installed():
    if importlib_utils.find_spec("psnawp_api"):
        logging.debug(f"'{PSNAWP_PACKAGE_NAME}' found, skipping")
        return True

    logging.warning(f"'{PSNAWP_PACKAGE_NAME}' not installed, installing...")

    # noinspection PyBroadException
    try:
        subprocess.check_call([sys.executable, "pip", "install", "PSNAWP", ])
        return True
    except Exception:
        logging.exception(
            f"Could not install '{PSNAWP_PACKAGE_NAME}', "
            f"see log for details!"
        )

    return False


def setup():
    if os.path.exists(COOKIES_DATA_PATH):
        return

    if not ensure_psnawp_is_installed():
        return

    is_logged_in = input(
        "Please login to your Playstation account and keep the browser open "
        "before moving forward. Type 'done' when ready to move on: "
    )
    if is_logged_in.lower() != "done":
        logging.warning(f"Expected 'done', got '{is_logged_in}', aborting...")
        return

    logging.info(f"Opening '{SSO_COOKIE_URL}' in active browser...")
    webbrowser.open(SSO_COOKIE_URL)
    cookies_given = input(
        "A URL should have opened up in the same browser you logged in. "
        "Please copy the 64 character npsso code and paste it below:"
        "\n\t"
        "(disclaimer: this code will be saved to a txt file at the root of this package)"
        "\n"
    )
    if len(cookies_given) != 64:
        logging.error(
            f"Expected 64 character npsso code, got '{len(cookies_given)}' "
            f"characters instead. Aborting..."
        )
        return

    with open(COOKIES_DATA_PATH, "w") as cookies_file_obj:
        json.dump(cookies_given, cookies_file_obj)
        logging.info(
            f"Saved cookies '{cookies_given}' to '{COOKIES_DATA_PATH}'..."
        )


if __name__ == "__main__":
    setup()
