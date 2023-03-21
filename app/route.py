import os
import importlib
import datetime
from flask import render_template, request
from app import get
from app import app
from PIL import Image, ImageFilter
from PIL.ImageFilter import(
	BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SHARPEN
	)
@app.after_request
def add_header(response):
	response.cache_control.max_age = 0 
	return response




#pics = get.pics.replace('\\', '/')
#counter = get.counter
imagen = None
def filt(pluck):
	#importlib.reload(Image)
	im = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{pluck}")
	""" -----------------------------effect--------------------------"""
	#importlib.reload(ImageFilter)
	sim_blur = im.filter(ImageFilter.BLUR)
	sim_blur.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb1.png')

	box_blur = im.filter(ImageFilter.BoxBlur(5))
	box_blur.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb2.png')

	gauss = im.filter(ImageFilter.GaussianBlur(5))
	gauss.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edb3.png')
	""" -----------------------------filter--------------------------"""
	try:
		r, g, b = im.split()
		merged = Image.merge("RGB", (b, g, r)) 
		merged.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/edc1.png')

	except ValueError as e:
		pass
	
	
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

#for the crop
	
def cropfilt(pluck):
	im = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{pluck}")
	try:
		a = int(input("Reduce the left by: "))
		b = int(input("Reduce the up by: "))
		c = int(input("Reduce the right by: "))
		d = int(input("Reduce the down by: ")) 	                      
		crop = im.crop((a, b, c, d))
	except SystemError as e:
		print("put lesser value")
		a = int(input("Reduce the left by: "))
		b = int(input("Reduce the up by: "))
		c = int(input("Reduce the right by: "))
		d = int(input("Reduce the down by: "))
		crop = im.crop((a, b, c, d))
	crop.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda1.png')


def filtfh(pluck):
	im = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{pluck}")
	hori_flip = im.transpose(Image.FLIP_LEFT_RIGHT)
	hori_flip.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda2.png')

def filtfv(pluck):
	im = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{pluck}")
	vert_flip = im.transpose(Image.FLIP_TOP_BOTTOM)
	vert_flip.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda3.png')


def filtrot(pluck):
	im = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{pluck}")
	rotate_90 = im.transpose(Image.ROTATE_90)
	rotate_90.save('C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images/eda4.png')



"""

@app.after_request
def add_header(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

"""
@app.route('/')
def index():
	return render_template("index.html")




@app.route('/select')
def select():
	return render_template("select.html", box=get.pics)
	# return "<html>Hi</html>"


@app.route('/editor', methods=['POST'])
def edit():
	newpic = request.form.get("choice")
	global imagen
	if newpic == None:
		data = request.form.get("best")
		imagen = f"/static/images/shaditor{data}.png"
		filt(imagen)
	else:
		imagen = f"/static/images/ed{newpic}.png"
		filt(imagen)

	
	return render_template("editor.html", imagen=imagen)


""" -----------------------------crop--------------------------"""
@app.route('/editor/c', methods=['POST'])
def cropp():
	global imagen
	cropfilt(imagen)
	imagen = "/static/images/eda1.png"
	filt(imagen)
	return render_template("editor.html", imagen=imagen)


@app.route('/editor/fv', methods=['POST'])
def flipv():
	global imagen
	filtfv(imagen)
	imagen = "/static/images/eda3.png"
	filt(imagen)
	return render_template("editor.html", imagen=imagen)





@app.route('/editor/fh', methods=['POST'])
def fliph():
	global imagen
	filtfh(imagen)
	imagen = "/static/images/eda2.png"
	filt(imagen)
	return render_template("editor.html", imagen=imagen)



@app.route('/editor/r', methods=['POST'])
def rott():
	global imagen
	filtrot(imagen)
	imagen = "/static/images/eda4.png"
	filt(imagen)
	return render_template("editor.html", imagen=imagen)


@app.route('/editor/s', methods=['POST'])
def save():
	savepic = Image.open(f"C:/Users/VERA OLEHI/Documents/Shaditor/app{imagen}")
	date=datetime.datetime.now()
	datee = f"r-{date:%Y%m%d%H%M%S}"
	savepic.save(f'C:/Users/VERA OLEHI/Documents/Shaditor/SavedImages/shadito{datee}.png')
	return render_template("editor.html", imagen=imagen)


	
"""
dir1 = 'C:/Users/VERA OLEHI/Documents/Shaditor/app/static/images'
filelist = [ f for f in os.listdir(dir1) if f.endswith(".png") ]
for f in filelist:
	os.remove(os.path.join(dir1, f))

dir2 = 'C:/Users/VERA OLEHI/Documents/Shaditor/app/__pycache__'
filelist = [ f for f in os.listdir(dir2) ]
for f in filelist:
	os.remove(os.path.join(dir2, f))

"""




#later try the merge two pictures function



