## bulding the url dynamically
## jinja 2 tamplate engine

## {{}} expression to print output in html
# {%...% } conditional  for loop
# {#..#} this for comments 

from flask import Flask, redirect,render_template, request, url_for

### WSGI application ( web server gateway interface)
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to flask module very usefull</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html',methods=['GET'])



@app.route("/submit1",methods=['GET','POST'])
def submit1():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        return f'Hello {name},{email} welcome to the plat from and you want to necome {message}'
# variable rule
@app.route('/sucess/<int:score>')
def success(score):
    res=""
    if score>50:
        res='passed'
    else:
        res='failed'
    return render_template("result.html",result=res)


# for loop with html
@app.route('/successres/<int:score>')
def successres(score):
    # res=""
    # if score>50:
    #     res='passed'
    # else:
    #     res='failed'
    # exp={'score':score,'res':res}
    return render_template("result.html",result=score)


## if loop with html
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result.html",result=score)

@app.route('/fail/<int:score>')
def fail(score):
   
    return render_template("result.html",result=score)
@app.route('/submit',methods=['POST','GET'])
def submit():
    totalmarks=0
    if request.method=='POST':
        student1_name = request.form['student1_name']
        maths1 = float(request.form['maths1'])
        science1 = float(request.form['science1'])
        english1 = float(request.form['english1'])
        totalmarks=(maths1+science1+english1)/3

    return redirect(url_for('successres',score=totalmarks))


if __name__=="__main__":
    app.run(debug=True)

#hhtp GET,POST,PUT and delete