import os
from service.s_write_docx import WriteDocxService


class WriteDocxController:
    def __init__(self):
        self.write_docx_service = WriteDocxService()

    def write_docx(self, pasta_selecionada: str) -> str:
        if not pasta_selecionada:
            return "Pasta não selecionada"
        if not os.path.exists(pasta_selecionada):
            return "A pasta selecionada não existe"
        return self.write_docx_service.write_docx(pasta_selecionada=pasta_selecionada)

