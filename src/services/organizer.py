from pathlib import Path
from services.classifier import Classifier


class Organizer:
    def __init__(self, config):
        # Armazena as configurações da aplicação para que possam ser
        # utilizadas pelos demais métodos da classe.
        self.config = config

    def list_files(self):
        """
        Lista todos os arquivos presentes na pasta de origem.

        Returns:
            list[Path]: Lista contendo os arquivos encontrados.
        """

        # Converte o caminho configurado em um objeto Path para facilitar
        # a manipulação de arquivos e diretórios.
        source_folder = Path(self.config.source_folder)
        files = []

        # Percorre todos os itens existentes na pasta.
        for item in source_folder.iterdir():

            # Adiciona apenas arquivos à lista, ignorando diretórios.
            if item.is_file():
                files.append(item)

        return files
    
    def show_files_info(self):
        """
        Exibe informações básicas dos arquivos encontrados e sua categoria.
        Utilizado durante o desenvolvimento para validar a classificação.
        """

        files = self.list_files()

        for file in files:

            if Classifier.is_image(file.suffix):
                category = "Imagem"

            elif Classifier.is_document(file.suffix):
                category = "Documento"

            elif Classifier.is_spreadsheet(file.suffix):
                category = "Planilha"

            else:
                category = "Outros"

            print(f"Arquivo: {file.name}")
            print(f"Nome: {file.stem}")
            print(f"Extensão: {file.suffix}")
            print(f"Categoria: {category}")
            print("-" * 40)