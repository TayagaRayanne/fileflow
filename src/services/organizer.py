from pathlib import Path


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