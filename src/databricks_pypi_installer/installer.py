import subprocess
import sys


def install(package: str, extra_index_url: str | None = None) -> None:
    command = [sys.executable, "-m", "pip", "install", package]
    if extra_index_url:
        command.extend(["--extra-index-url", extra_index_url])
    subprocess.check_call(command)
