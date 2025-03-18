from flask import Flask,render_template, request

### WSGI application ( web server gateway interface)
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to flask module very usefull</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html',methods=['GET'])


@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        return f'Hello {name},{email} welcome to the plat from and you want to necome {message}'
    return render_template('form.html')


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        return f'Hello {name},{email} welcome to the plat from and you want to necome {message}'





if __name__=="__main__":
    app.run(debug=True)

#hhtp GET,POST,PUT and delete