from flask import Flask,render_template,request

### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Welcome to Flask</h1></html>"

@app.route('/index',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return f"<html><h1>Welcome {name} you are {age} years old</h1></html>"
    
    return render_template('newform.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return f"<html><h1>Welcome {name} you are {age} years old</h1></html>"
    
    return render_template('submit.html')

if __name__=="__main__":
    app.run(debug=True)