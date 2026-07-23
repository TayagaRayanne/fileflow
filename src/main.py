from core.config_loader import ConfigLoader
from core.logger import get_logger
from services.organizer import Organizer


def main():
    # Inicializa o sistema de logs da aplicação.
    logger = get_logger()

    # Registra o início da execução da aplicação.
    logger.info("Iniciando FileFlow...")

    # Carrega as configurações definidas no arquivo config.json.
    loader = ConfigLoader()
    config = loader.load()

    # Cria uma instância do organizador utilizando as configurações carregadas.
    organizer = Organizer(config)

    # Confirma que as configurações foram carregadas com sucesso.
    logger.info("Configurações carregadas com sucesso.")

    # Exibe informações dos arquivos encontrados.
    organizer.show_files_info()


if __name__ == "__main__":
    main()