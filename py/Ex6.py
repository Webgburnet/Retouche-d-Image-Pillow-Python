import PIL.Image as Image
img = Image.open(r'rond-bac-SIN.jpg')
img = img.convert('L')
img.save('rond-bac-SIN_n&b.jpg')
