

# internal
from psnawp_api import PSNAWP
from cookies import get_cached_npsso_code


class PSNCache:
    _NPSSO_CODE = get_cached_npsso_code()

    PSNAWP = PSNAWP(_NPSSO_CODE)
    CLIENT = PSNAWP.me()
