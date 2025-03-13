from flask import Flask

### WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to flask module"



if __name__=="__main__":
    app.run()

