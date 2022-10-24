from normalize import normalize
import sys
import shutil
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ARCHIVES = []
others = []

REGISTER_EXTENSIONS = {
    'JPEG':JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
    }

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    # перетворюємо розширення файлу на назву папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()

def new_folder(folder: Path, file: Path):
    # створюємо папку, переміщаємо, нормалізуємо
    folder.mkdir(exist_ok=True, parents=True)
    file.replace(folder / normalize(file.name))

def sort_trash(path):
    trash = Path(path)
    for element in trash.iterdir():
        # обробка вкладених папок
        if element.is_dir():
            # скрипт ігнорує папки
            if element.name not in ('archives', 'video', 'audio', 'documents', 'images', 'others'):
                FOLDERS.append(element)
                sort_trash(element)  # рекурсія
                continue
        else:
            # сортування файлів
            ext = get_extension(element.name)  # беремо розширення
            fullname = trash / element.name  # беремо шлях до файлу
            
            if not ext:  # файл без розширення додаємо до списку <інші>
                others.append(fullname)
            else:
                try:
                    # шукаємо в переліку розширень
                    container = REGISTER_EXTENSIONS[ext]
                    EXTENSIONS.add(ext) # додаємо до списку знайдених розширень
                    container.append(fullname)
                    
                except KeyError:
                    #    додаємо до списку <інші>, якщо невідоме розширення
                    UNKNOWN.add(ext)
                    others.append(fullname)


if __name__ == '__main__':
# виводимо списки в консоль python3 sort.py `назва_папки_для_сортування`
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    sort_trash(Path(folder_for_scan))
    if not JPEG_IMAGES == []:
        print (f'Images jpeg: {JPEG_IMAGES}')
    if not PNG_IMAGES == []:
        print (f'Images png: {PNG_IMAGES}')
    if not JPG_IMAGES == []:
        print (f'Images jpg: {JPG_IMAGES}')
    if not SVG_IMAGES == []:
        print(f'Images svg: {SVG_IMAGES}')
    if not AVI_VIDEO == []:
        print(f'Video avi: {AVI_VIDEO}')
    if not MP4_VIDEO == []:
        print(f'Video mp4: {MP4_VIDEO}')
    if not MOV_VIDEO == []:
        print(f'Video mov: {MOV_VIDEO}')
    if not MKV_VIDEO == []:
        print(f'Video mkv: {MKV_VIDEO}')
    if not DOC_DOCUMENTS == []:
        print(f'Documents doc: {DOC_DOCUMENTS}')
    if not DOCX_DOCUMENTS == []:
        print(f'Documents docx: {DOCX_DOCUMENTS}')
    if not TXT_DOCUMENTS == []:
        print(f'Documents txt: {TXT_DOCUMENTS}')
    if not PDF_DOCUMENTS == []:
        print(f'Documents pdf: {PDF_DOCUMENTS}')
    if not XLSX_DOCUMENTS == []:
        print(f'Documents xlsx: {XLSX_DOCUMENTS}')
    if not PPTX_DOCUMENTS == []:
        print(f'Documents pptx: {PPTX_DOCUMENTS}')
    if not MP3_AUDIO == []:
        print(f'Audio mp3: {MP3_AUDIO}')
    if not OGG_AUDIO == []:
        print(f'Audio ogg: {OGG_AUDIO}')
    if not WAV_AUDIO == []:
        print(f'Audio wav: {WAV_AUDIO}')
    if not AMR_AUDIO == []:
        print(f'Audio amr: {AMR_AUDIO}')
    if not ARCHIVES == []:
        print(f'Archives: {ARCHIVES}')
    
    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')
