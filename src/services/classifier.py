class Classifier:
    """
    As extensões são armazenadas em um conjunto (set) porque nosso objetivo é
    apenas verificar se uma extensão pertence a determinada categoria.
    O uso de {} torna essa consulta mais eficiente do que uma lista ([]),
    principalmente à medida que a quantidade de extensões aumenta.
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
    }
    
    @classmethod
    def is_image(cls, extension: str) -> bool:
        """
        Verifica se a extensão pertence à categoria de imagens.

        Args:
            extension (str): Extensão do arquivo.

        Returns:
            bool: True se for uma imagem, False caso contrário.
        """

        return extension.lower() in cls.IMAGE_EXTENSIONS
    
    @classmethod
    def is_document(cls, extension: str) -> bool:
        """
        Verifica se a extensão pertence à categoria de documentos.

        Args:
            extension (str): Extensão do arquivo.

        Returns:
            bool: True se for um documento, False caso contrário.
        """

        return extension.lower() in cls.DOCUMENT_EXTENSIONS

    @classmethod
    def is_spreadsheet(cls, extension: str) -> bool:
        """
        Verifica se a extensão pertence à categoria de planilhas.

        Args:
            extension (str): Extensão do arquivo.

        Returns:
            bool: True se for uma planilha, False caso contrário.
        """

        return extension.lower() in cls.SPREADSHEET_EXTENSIONS