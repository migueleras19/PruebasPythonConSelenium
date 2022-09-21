from PIL import Image

import os, shutil

descargas ='/home/qacore/Descargas/'
jarfolder = '/media/qacore/data/VARIOS/ZIP/'

if __name__ == "__main__":
    for filename in os.listdir(descargas):
        name, extension = os.path.splitext(descargas + filename)

        # if extension in [".jpg", ".jpeg", ".png"]:
        #     picture = Image.open(descargas + filename)
        #     picture.save(jarfolder + "compressed_"+filename, optimize=True, quality=60)
        #     os.remove(descargas + filename)
        #     print(name + ": " + extension)

        if extension in [".pdf"]:
            zipfolder = "/media/qacore/data/VARIOS/PDF/"
            os.rename(descargas + filename, zipfolder + filename)
            os.remove(descargas + filename)
            print(name + ": " + extension)