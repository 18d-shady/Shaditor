import os
import shutil
from PIL import Image

pics = ''
copy = ''
counter = 0
#stat = '"static"'
pic = ".png"
rec = '&Recycle.Bin'

thisdir = os.getcwd()

# print('Hello')

for r, d, f in os.walk("C:\\"):
	for file in f:
		filepath = os.path.join(r, file)
		# print(f'file=> {file}')
		if pic in file: 
			counter += 1 
			target = rf"C:\Users\VERA OLEHI\Documents\Shaditor\app\static\images\shaditor{counter}.png"
			copy += shutil.copyfile(os.path.join(r, file), target)
			#fil = f'"images/shaditor{counter}.png"'
			#pics += f"<div style='width:31vw; height:30vh; display: inline-block; background-color:#c3c3c3; margin: 4px 6px 4px 6px' position:relative;><a onclick='create()' href='/editor' ><img src='/static/images/shaditor{counter}.png' alt='image cant show' style='position:absolute; width:31vw; height:30vh;'/></a></div>"
			pics += f"<label style='width:31vw; height:30vh; display: inline-block; background-color:#c3c3c3; margin: 4px 6px 4px 6px'><input type='radio' name='best' id='best' value='{counter}' onchange='this.form.submit()'><img src='/static/images/shaditor{counter}.png' alt='image cant show' style='width:31vw; height:30vh;'/></label>"
			#pics += f"<input type='image' name='submit' value='shaditor{counter}' src='/static/images/shaditor{counter}.png' alt='image cant show' border='0' style='width:31vw; height:30vh; display: inline-block; background-color:#c3c3c3; margin: 4px 6px 4px 6px' />"
			if counter == 20: break
				# break
	# break
	if counter == 20: break


#{{{{ url_for({stat} , filename={fil}) }}}}


# print('Hello 2')