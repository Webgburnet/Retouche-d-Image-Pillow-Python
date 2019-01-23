import PIL.Image as Image
im = Image.open(r'rond-bac-SIN.jpg')
img = Image.open(r'rond-bac-SIN-nb.jpg')
pixels = im.load()
pixels[0,0] = 0
im.save(r'rond-bac-SIN_mod.jpg')
pixels = img.load()
pixels[0,0] = 0
img.save(r'rond-bac-SIN-nb_mod.jpg')
