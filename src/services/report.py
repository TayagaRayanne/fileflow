import csv
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class Report:
    """
    Representa os dados de uma execução do FileFlow.
    """

    started_at: datetime
    finished_at: datetime | None = None
    files_organized: int = 0
    categories: dict[str, int] = field(default_factory=dict)

    def add_file(self, category: str):
        """
        Registra um arquivo organizado no relatório.

        Args:
            category (str): Categoria do arquivo organizado.
        """

        self.files_organized += 1

        self.categories[category] = (
            self.categories.get(category, 0) + 1
        )

    def generate_summary(self) -> dict:
        """
        Gera um resumo da execução do FileFlow.

        Returns:
            dict: Dados consolidados da execução.
        """

        duration = None

        if self.finished_at is not None:
            duration = (
                self.finished_at - self.started_at
            ).total_seconds()

        return {
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "files_organized": self.files_organized,
            "categories": self.categories,
            "duration_seconds": duration,
        }

    def to_csv_row(self) -> dict:
        """
        Converte o resumo da execução para uma linha de CSV.

        Returns:
            dict: Dados da execução preparados para o relatório.
        """

        summary = self.generate_summary()

        row = {
            "started_at": summary["started_at"].strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "finished_at": summary["finished_at"].strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "files_organized": summary["files_organized"],
            "duration_seconds": summary["duration_seconds"],
        }

        for category, quantity in summary["categories"].items():
            row[category] = quantity

        return row

    def save_csv(self, file_path: Path):
        """
        Salva os dados da execução em um arquivo CSV.

        Args:
            file_path (Path): Caminho do arquivo CSV.
        """

        row = self.to_csv_row()

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_exists = file_path.exists()

        with file_path.open(
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=row.keys()
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(row)