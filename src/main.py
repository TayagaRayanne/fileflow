from datetime import datetime
from pathlib import Path

from core.config_loader import ConfigLoader
from core.logger import get_logger
from services.organizer import Organizer
from services.report import Report


def main():
    # Inicializa o sistema de logs da aplicação.
    logger = get_logger()

    # Registra o início da execução da aplicação.
    logger.info("Iniciando FileFlow...")

    # Carrega as configurações definidas no arquivo config.json.
    loader = ConfigLoader()
    config = loader.load()

    # Cria o relatório da execução.
    report = Report(
        started_at=datetime.now()
    )

    # Cria uma instância do organizador utilizando as configurações
    # carregadas e o relatório da execução.
    organizer = Organizer(config, report)

    # Confirma que as configurações foram carregadas com sucesso.
    logger.info("Configurações carregadas com sucesso.")

    # Organiza os arquivos encontrados.
    organizer.organize_files()

    # Registra o final da execução.
    report.finished_at = datetime.now()

    # Salva o relatório da execução em CSV.
    report_path = Path("reports/fileflow_report.csv")
    report.save_csv(report_path)


if __name__ == "__main__":
    main()