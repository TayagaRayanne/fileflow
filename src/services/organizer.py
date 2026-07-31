from pathlib import Path
from core.logger import get_logger
from services.classifier import Classifier


class Organizer:
    def __init__(self, config):
        # Armazena as configurações da aplicação para que possam ser
        # utilizadas pelos demais métodos da classe.
        self.config = config
        self.logger = get_logger()

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

        # Impede utilizar a mesma pasta como origem e destino.
        if source_folder.resolve() == destination_folder.resolve():
            raise ValueError(
                "A pasta de origem e a pasta de destino não podem ser iguais."
            )

        # Impede que a pasta de destino esteja dentro da pasta de origem.
        if source_folder.resolve() in destination_folder.resolve().parents:
            raise ValueError(
                "A pasta de destino não pode estar dentro da pasta de origem."
            )
            
        # Impede que a pasta de origem esteja dentro da pasta de destino.
        if destination_folder.resolve() in source_folder.resolve().parents:
            raise ValueError(
                "A pasta de origem não pode estar dentro da pasta de destino."
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
    
    def create_destination_folder(self, folder_name: str) -> Path:
        """
        Cria (caso necessário) a pasta de destino onde o arquivo será armazenado.

        Args:
            folder_name (str): Nome da categoria (Imagens, Documentos, etc.)

        Returns:
            Path: Caminho completo da pasta criada.
        """

        destination_root = Path(self.config.destination_folder)

        destination = destination_root / folder_name

        folder_exists = destination.exists()

        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        if not folder_exists:
            self.logger.info(
                "Pasta criada: %s",
                destination
            )

        return destination
    
    def generate_unique_filename(
        self,
        source: Path,
        destination: Path
    ) -> Path:
        """
        Gera um nome de arquivo único caso já exista um arquivo
        com o mesmo nome na pasta de destino.

        Args:
            source (Path): Arquivo original.
            destination (Path): Pasta de destino.

        Returns:
            Path: Caminho disponível para salvar o arquivo.
        """

        destination_file = destination / source.name

        # Se o arquivo ainda não existir, pode utilizá-lo normalmente.
        if not destination_file.exists():
            return destination_file

        counter = 1

        while True:

            new_name = (
                f"{source.stem} ({counter})"
                f"{source.suffix}"
            )

            destination_file = destination / new_name

            if not destination_file.exists():
                return destination_file

            counter += 1
    
    def move_file(self, source: Path, destination: Path) -> Path:
        """
        Move um arquivo para a pasta de destino.

        Args:
            source (Path): Arquivo de origem.
            destination (Path): Pasta onde o arquivo será movido.

        Returns:
            Path: Caminho final do arquivo movido.
        """

        destination_file = self.generate_unique_filename(
            source,
            destination
        )

        source.rename(destination_file)
        
        self.logger.info(
            "[MOVE] %s -> %s/%s",
            source.name,
            destination.name,
            destination_file.name
        )

        return destination_file
        
    def organize_files(self):
        """
        Organiza todos os arquivos encontrados na pasta de origem.
        """

        files = self.list_files()

        # Encerra a execução caso não existam arquivos para organizar.
        if not files:
            self.logger.info(
                "Nenhum arquivo encontrado para organizar."
            )
            return

        self.logger.info(
            "Iniciando organização de %d arquivo(s).",
            len(files)
        )

        for file in files:

            folder_name = Classifier.get_folder_name(file.suffix)

            destination = self.create_destination_folder(folder_name)

            destination_file = self.move_file(file, destination)

            print(
                f"{file.name} -> "
                f"{destination_file.parent.name}/{destination_file.name}"
            )

        self.logger.info(
            "Organização concluída com sucesso."
        )

    def show_files_info(self):
        """
        Exibe informações básicas dos arquivos encontrados e
        sua categoria.
        """

        files = self.list_files()

        for file in files:

            category = Classifier.classify(file.suffix)
            destination = Classifier.get_folder_name(file.suffix)
            
            destination_path = self.create_destination_folder(destination)

            print(f"Arquivo: {file.name}")
            print(f"Nome: {file.stem}")
            print(f"Extensão: {file.suffix}")
            print(f"Categoria: {category}")
            print(f"Destino: {destination_path}")
            print("-" * 40)