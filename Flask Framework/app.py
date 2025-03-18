from flask import Flask

### WSGI application ( web server gateway interface)
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to flask module very usefull"

@app.route("/index")
def index():
    return "this is the index page"



if __name__=="__main__":
    app.run(debug=True)

