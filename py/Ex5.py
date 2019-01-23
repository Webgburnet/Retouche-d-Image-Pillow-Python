import PIL.Image as Image
#img = Image.open(r'rond-bac-SIN.jpg')
img = Image.open(r'rond-bac-SIN-nb.jpg')

def rev(im):
    # negatif image couleur
    pix = im.load()
    for i in range(0, im.size[0]):
        for j in range(0, im.size[1]):
            r,v,b = pix[i,j]
            pixels[i,j] = 255 - r,255 - v,255 - b
    #im.save(r'rond-bac-SIN_rev.jpg')
    im.save(r'rond-bac-SIN-nb_rev.jpg')

pixels = img.load()
rev(img)
