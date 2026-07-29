from pathlib import Path

from services.classifier import Classifier


class Organizer:
    def __init__(self, config):
        # Armazena as configurações da aplicação para que possam ser
        # utilizadas pelos demais métodos da classe.
        self.config = config

    def is_ignored_folder(self, folder: Path) -> bool:
        """
        Verifica se uma pasta está configurada para ser ignorada.

        Args:
            folder (Path): Pasta a ser verificada.

        Returns:
            bool: True se a pasta deve ser ignorada.
        """

        # Verifica se o nome da pasta está na lista de pastas protegidas.
        return folder.name in self.config.ignored_folders

    def validate_source_folder(self) -> Path:
        """
        Valida se a pasta de origem pode ser utilizada pelo FileFlow.

        Raises:
            ValueError: Caso a pasta configurada seja inválida
            ou represente um risco para a automação.

        Returns:
            Path: Caminho validado da pasta de origem.
        """

        # Verifica se a pasta de origem foi configurada.
        if not self.config.source_folder:
            raise ValueError("A pasta de origem não foi configurada.")

        source_folder = Path(self.config.source_folder)

        # Verifica se a pasta existe.
        if not source_folder.exists():
            raise ValueError("A pasta de origem não existe.")

        # Verifica se o caminho realmente é uma pasta.
        if not source_folder.is_dir():
            raise ValueError("O caminho informado não é uma pasta.")

        # Verifica se a pasta de destino foi configurada.
        if not self.config.destination_folder:
            raise ValueError("A pasta de destino não foi configurada.")

        destination_folder = Path(self.config.destination_folder)

        # Obtém a raiz do projeto.
        project_root = Path.cwd()

        # Impede utilizar a raiz do projeto como origem.
        if source_folder.resolve() == project_root.resolve():
            raise ValueError(
                "A pasta de origem não pode ser a raiz do projeto."
            )

        # Impede utilizar a mesma pasta como origem e destino.
        if source_folder.resolve() == destination_folder.resolve():
            raise ValueError(
                "A pasta de origem e a pasta de destino não podem ser iguais."
            )

        return source_folder

    def list_files(self):
        """
        Lista todos os arquivos presentes na pasta de origem.

        Returns:
            list[Path]: Lista contendo os arquivos encontrados.
        """

        source_folder = self.validate_source_folder()
        files = []

        # Percorre todos os itens existentes na pasta.
        for item in source_folder.iterdir():

            # Ignora diretórios protegidos.
            if item.is_dir() and self.is_ignored_folder(item):
                continue

            # Adiciona apenas arquivos.
            if item.is_file():
                files.append(item)

        return files

    def show_files_info(self):
        """
        Exibe informações básicas dos arquivos encontrados e
        sua categoria.
        """

        files = self.list_files()

        for file in files:

            category = Classifier.classify(file.suffix)
            destination = Classifier.get_folder_name(file.suffix)

            print(f"Arquivo: {file.name}")
            print(f"Nome: {file.stem}")
            print(f"Extensão: {file.suffix}")
            print(f"Categoria: {category}")
            print(f"Destino: {destination}")
            print("-" * 40)