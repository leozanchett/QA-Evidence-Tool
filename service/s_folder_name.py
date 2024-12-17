class FolderNameService:
    def __init__(self):
        pass
    
    @staticmethod
    def get_folder_name(pasta_selecionada: str) -> str:
        try:
            if not pasta_selecionada:
                raise ValueError("Pasta não selecionada")
            folder_name = pasta_selecionada.split("/")[-1]
            return folder_name
        except ValueError as e:
            return str(e)
