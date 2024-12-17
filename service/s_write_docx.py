import os
from s_folder_name import FolderNameService
from s_folders import FoldersService


class WriteDocxService:
    EXTENSIONS = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".ico", ".webp"]

    def __init__(self):
        pass
    
    def write_docx(self, pasta_selecionada):
        self.write_image_to_docx(pasta_selecionada)
    
    def write_image_to_docx(self, target_folder):
        folders = FoldersService.get_folders(target_folder)
        files = FoldersService.get_files_with_extension(target_folder, self.EXTENSIONS)
        
        if files:
            folder_name = FolderNameService.get_folder_name(target_folder)
            with open('imagens.txt', 'a') as arquivo:
                arquivo.write(f'{folder_name}\n')
                for file in files:
                    arquivo.write(f'{file}\n')
        
        for folder in folders:
            subfolder_path = os.path.join(target_folder, folder)
            self.write_image_to_docx(subfolder_path)


if __name__ == "__main__":
    path = 'C:/Users/lzandrade.TOPAZ/Documents/GitHub/QA-Evidence-Tool/docs'
    write_docx_service = WriteDocxService()
    write_docx_service.write_docx(path)
