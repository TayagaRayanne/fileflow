from dataclasses import dataclass


@dataclass(slots=True)
class AppConfig:
    """
    Representa todas as configurações da aplicação.
    """

    source_folder: str
    destination_folder: str
    ignored_extensions: list[str]
    log_level: str