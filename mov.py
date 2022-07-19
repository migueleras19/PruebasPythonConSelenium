from PIL import Image
import os

descargas ='/home/qacore/Descargas/'
jarfolder = '/media/qacore/data/VARIOS/JAR/'

if __name__ == '__main__':
    for filename in os.listdir(descargas):
        name, extension = os.path.splitext(descargas + filename)

        if extension in [".pdf"]:
            datos = Image.open(descargas + filename)
            datos.save(jarfolder + "compressed_"+filename)
            os.remove(descargas + filename)
            print(name + ": " + extension)
        
        if extension in ['.pdf']:
            pdffolder = '/media/qacore/data/VARIOS/PDF/'
            os.rename (descargas + filename, pdffolder + filename)
            print(name + ': ' + extension)