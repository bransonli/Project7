
from tesserocr import PyTessBaseAPI
from PIL import Image


column = Image.open(r'C:\Users\brans\Documents\Application-files-utilities\VScode\Project-007\Data-storage\Stop-Sign-400.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save(r'C:\Users\brans\Documents\Application-files-utilities\VScode\Project-007\Data-storage\sample.jpg')


with PyTessBaseAPI() as api:
    api.SetImageFile(r'C:\Users\brans\Documents\Application-files-utilities\VScode\Project-007\Data-storage\sample.jpg')
    print(api.GetUTF8Text())


