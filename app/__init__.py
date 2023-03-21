from flask import Flask

app = Flask(__name__)

from app import route


app.run(debug=True)




@app.after_request
def add_header(response):
	response.cache_control.max_age = 0 
	return response



