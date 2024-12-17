import os


class FoldersService:
    def __init__(self):
        pass
    
    @staticmethod
    def get_folders(pasta_selecionada: str) -> list:
        return [folder for folder in os.listdir(pasta_selecionada) if os.path.isdir(os.path.join(pasta_selecionada, folder))]
    
    @staticmethod
    def get_files_with_extension(pasta_selecionada: str, extension: list[str]) -> list:
        return [file for file in os.listdir(pasta_selecionada) if any(file.endswith(ext) for ext in extension)]

