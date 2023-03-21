
"""
from PIL import Image, ImageFilter

from PIL.ImageFilter import(
	BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SHARPEN
	)

def imo(imm):
	im = Image.open(imm)


# -----------------------------crop--------------------------
def cropim(im):
	a = input("Reduce the left by: ")
	b = input("Reduce the up by: ")
	c = input("Reduce the right by: ")
	d = input("Reduce the down by: ")

	crop = im.crop((a, b, c, d))
	crop.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda1.png')

#cropim(im)
def hori(im):
	hori_flip = im.transpose(Image.FLIP_LEFT_RIGHT)
	hori_flip.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda2.png')

def vert(im):
	vert_flip = im.transpose(Image.FLIP_TOP_BOTTOM)
	vert_flip.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda3.png')

def rot(im):
	rotate_90 = im.transpose(Image.ROTATE_90)
	rotate_90.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda4.png')



#-----------------------------effect--------------------------

sim_blur = im.filter(ImageFilter.BLUR)
sim_blur.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb1.png')


box_blur = im.filter(ImageFilter.BoxBlur(5))
box_blur.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb2.png')


gauss = im.filter(ImageFilter.GaussianBlur(5))
gauss.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb3.png')


# -----------------------------filter--------------------------


def merged_rgb(im):
	r, g, b = im.split()
	merged = Image.merge("RGB", (b, g, r)) 
	merged.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc1.png')
merged_rgb(im)



mini_fil = im.filter(ImageFilter.MinFilter(3))
mini_fil.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc2.png')


blur = im.filter(BLUR)
blur.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc3.png')

cont = im.filter(CONTOUR)
cont.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc4.png')


detail = im.filter(DETAIL)
detail.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc5.png')

edge = im.filter(EDGE_ENHANCE)
edge.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc6.png')

edge_more = im.filter(EDGE_ENHANCE_MORE)
edge_more.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc7.png')

emb = im.filter(EMBOSS)
emb.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc8.png')

find_edge = im.filter(FIND_EDGES)
find_edge.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc9.png')

smooth = im.filter(SMOOTH)
smooth.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc10.png')

sharp = im.filter(SHARPEN)
sharp.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc11.png')







#later try the merge two pictures function


"""