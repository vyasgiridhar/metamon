import os
from importlib.metadata import version

__version__ = "1.5.1"

# ANSI color codes
_YELLOW = "\033[38;5;228m"
_BLUE = "\033[94m"
_CYAN = "\033[96m"
_RED = "\033[91m"
_WHITE = "\033[97m"
_BOLD = "\033[1m"
_DIM = "\033[2m"
_RESET = "\033[0m"

_METAMON_LOGO_LINES = [
    r"    __  ___     __                            ",
    r"   /  |/  /__  / /_____ _____ ___  ____  ____ ",
    "  / /|_/ / _ \\/ __/ __ `/ __ `__ \\/ __ \\/ __ \\",
    " / /  / /  __/ /_/ /_/ / / / / / / /_/ / / / /",
    "/_/  /_/\\___/\\__/\\__,_/_/ /_/ /_/\\____/_/ /_/ ",
]


def print_banner():
    print(f'{_BLUE}╔{"═" * 60}╗{_RESET}')

    for line in _METAMON_LOGO_LINES:
        padding = 60 - len(line)
        print(
            f'{_BLUE}║{_RESET}{_YELLOW}{_BOLD}{line}{" " * padding}{_RESET}{_BLUE}║{_RESET}'
        )

    print(f'{_BLUE}╠{"═" * 60}╣{_RESET}')
    tagline = f"Pokémon Showdown RL  •  v{__version__}  •  UT-Austin-RPL/metamon"
    pad_left = (60 - len(tagline)) // 2
    pad_right = 60 - len(tagline) - pad_left
    print(
        f'{_BLUE}║{_RESET}{" " * pad_left}{_WHITE}{tagline}{_RESET}{" " * pad_right}{_BLUE}║{_RESET}'
    )
    print(f'{_BLUE}╚{"═" * 60}╝{_RESET}')
    print()


poke_env_version = version("poke-env")

if poke_env_version != "0.8.3.2":
    import warnings
    warnings.warn(
        f"poke-env version {poke_env_version} (expected 0.8.3.2). "
        f"Set METAMON_ALLOW_ANY_POKE_ENV=True to suppress.",
        stacklevel=2,
    )

from .config import SUPPORTED_BATTLE_FORMATS, METAMON_CACHE_DIR
