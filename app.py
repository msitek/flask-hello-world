# ---- Flask "Hello world" ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
        return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

### other formats (int, float, path - accepts slashes)
#@app.route("/integer/<int:value>")
#def int_type(value):
#	return str(value + 1) 

#@app.route("/float/<float:value>")
#def float_type(value):
#	return str(value + 1)

#@app.route("/path/<path:value>")
#def path_type(value):
#	return value

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
	if name.lower() == "monika":
		return "Hello, {}".format(name)
	else:
		return "Not found", 404

# start the development server using the run() method
if __name__ == "__main__":
	app.run() 
