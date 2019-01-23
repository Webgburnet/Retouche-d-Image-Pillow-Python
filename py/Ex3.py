import PIL.Image as Image
im = Image.open(r'rond-bac-SIN.jpg')
img = Image.open(r'rond-bac-SIN-nb.jpg')
#acces a un pixel de l'image
pixels = im.load()
print("Image Couleur")
print("acces a un pixel de l'image [0,0] : ",pixels[0,0])
pixels = img.load()
print("Image Noir et Blanc")
print("acces a un pixel de l'image [0,0] : ",pixels[0,0])
