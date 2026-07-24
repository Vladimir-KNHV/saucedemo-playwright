from pathlib import Path
import platform
import sys
from config import settings

def create_allure_environment_file():
    items = [
        f"app_url={settings.app_url}",
        f"headless={settings.headless}",
        f"browsers={settings.browsers}",
        f"test_user={settings.test_user}",
        f"os_info={platform.system()}, {platform.release()}",
        f"python_version={sys.version}",
    ]

    properties = "\n".join(items)

    with open(Path("allure-results") / "environment.properties", "w") as file:
        file.write(properties)