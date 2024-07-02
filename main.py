import argparse
import os

from PIL import Image

def convertToWebp(dirpath: str, fromExt: str, toExt: str, quality: int = 50):

    with os.scandir(f'{dirpath}') as entries:
            imageFormat: str

            if toExt == 'jpg':
                imageFormat = 'jpeg'
            else:
                imageFormat = toExt

            for entry in entries:
                if entry.is_file() and entry.name.endswith(f'.{fromExt}'):
                    fileWithOutExtension = os.path.splitext(entry.name)[0]

                    try:
                        im = Image.open(f"{dirpath}{entry.name}").convert('RGB')
                        im.save(f"{dirpath}{fileWithOutExtension}.{toExt}", f"{imageFormat}", quality=quality)
                        os.remove(f"{dirpath}{entry.name}")
                        print("\033[1;36m" + f"{entry.name} Converted!".upper())
                    except:
                        print("\033[1;31m" + 'Oops! Something went wrong...')

            print("\033[1;32m" + f"Converted images!".upper())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Procesar imágenes en un directorio.')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directorio de imágenes. DEBE SEGUIR EL FORMATO LINUX "../.." ')
    parser.add_argument('--fromExt', type=str, required=True, help='Extensión de archivo de origen.')
    parser.add_argument('--toExt', type=str, required=True, help='Extensión de archivo de destino.')
    parser.add_argument('-q', '--quality', type=int, help='Calidad de imagen.')

    args = parser.parse_args()


    convertToWebp(args.directory,args.fromExt,args.toExt,args.quality)

