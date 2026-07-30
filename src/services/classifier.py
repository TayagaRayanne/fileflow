class Classifier:
    """
    Responsável por classificar arquivos de acordo com sua extensão
    e informar a pasta onde eles deverão ser armazenados.
    """

    IMAGE_EXTENSIONS = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
    }

    DOCUMENT_EXTENSIONS = {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".odt",
    }

    SPREADSHEET_EXTENSIONS = {
        ".xls",
        ".xlsx",
        ".csv",
        ".ods",
    }

    @classmethod
    def classify(cls, extension: str) -> str:
        """
        Retorna a categoria correspondente à extensão informada.

        Args:
            extension (str): Extensão do arquivo.

        Returns:
            str: Categoria do arquivo.
        """

        extension = extension.lower()

        if extension in cls.IMAGE_EXTENSIONS:
            return "Imagem"

        if extension in cls.DOCUMENT_EXTENSIONS:
            return "Documento"

        if extension in cls.SPREADSHEET_EXTENSIONS:
            return "Planilha"

        return "Outros"

    @classmethod
    def get_folder_name(cls, extension: str) -> str:
        """
        Retorna o nome da pasta de destino para a extensão informada.

        Args:
            extension (str): Extensão do arquivo.

        Returns:
            str: Nome da pasta de destino.
        """

        extension = extension.lower()

        if extension in cls.IMAGE_EXTENSIONS:
            return "Imagens"

        if extension in cls.DOCUMENT_EXTENSIONS:
            return "Documentos"

        if extension in cls.SPREADSHEET_EXTENSIONS:
            return "Planilhas"

        return "Outros"