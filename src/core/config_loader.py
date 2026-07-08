import json
from pathlib import Path

from core.config_model import AppConfig


class ConfigLoader:
    """
    Responsável por carregar as configurações da aplicação.
    """

    CONFIG_FILE = Path("config/config.json")

    def load(self) -> AppConfig:
        with open(self.CONFIG_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return AppConfig(
            source_folder=data["source_folder"],
            destination_folder=data["destination_folder"],
            ignored_extensions=data["ignored_extensions"],
            log_level=data["log_level"],
        )