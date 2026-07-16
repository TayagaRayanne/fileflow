from pathlib import Path
import logging

# Utilizamos pathlib para trabalhar com caminhos de forma multiplataforma.
# Assim evitamos diferenças entre Windows, Linux e macOS ao manipular
# arquivos e diretórios.

# Caminho onde serão armazenados os arquivos de log da aplicação.
LOG_FOLDER = Path("logs")

LOG_FILE = LOG_FOLDER / "fileflow.log"


def get_logger() -> logging.Logger:
    """
    Cria e configura o logger principal da aplicação.

    Returns:
        logging.Logger: Logger configurado para gravar mensagens
        no arquivo logs/fileflow.log.
    """

    # Garante que a pasta de logs exista antes da criação do arquivo.
    LOG_FOLDER.mkdir(exist_ok=True)

    # Obtém ou cria uma única instância do logger da aplicação.
    logger = logging.getLogger("fileflow")

    # Define o nível mínimo de mensagens que serão registradas.
    logger.setLevel(logging.INFO)

    # Evita adicionar múltiplos FileHandlers caso esta função
    # seja chamada mais de uma vez durante a execução.
    if logger.hasHandlers():
        return logger

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    # Define o formato das mensagens gravadas no arquivo de log.
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )

    # Associa o formato criado ao arquivo de log.
    file_handler.setFormatter(formatter)

    # Conecta o FileHandler ao logger da aplicação.
    logger.addHandler(file_handler)

    return logger