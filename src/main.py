from core.config_loader import ConfigLoader
from core.logger import get_logger


def main():
    logger = get_logger()

    logger.info("Iniciando FileFlow...")

    loader = ConfigLoader()
    config = loader.load()

    logger.info("Configurações carregadas com sucesso.")

    print(config)


if __name__ == "__main__":
    main()