from pathlib import Path
import logging

""" 
Usar o path facilita a criação de pastas e arquivos de forma multiplataforma.
Ele funciona melhor do que usar strings para representar caminhos de arquivos, 
pois ele lida com as diferenças entre sistemas operacionais automaticamente.
"""

LOG_FOLDER = Path("logs")
LOG_FILE = LOG_FOLDER / "fileflow.log"


def get_logger() -> logging.Logger:
    """
    Cria e retorna o logger da aplicação. Isso permite reutilizar sempre a mesma instância. 
    """

    LOG_FOLDER.mkdir(exist_ok=True)

    logger = logging.getLogger("fileflow")

    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger
# Evita adicionar múltiplos FileHandlers caso get_logger()
# seja chamado mais de uma vez durante a execução.

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger