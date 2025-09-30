from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Welcome to Flask</h1></html>"



@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return f"<html><h1>Welcome {name} you are {age} years old</h1></html>"
    
    return render_template('submit.html')

@app.route('/success/<int:score>')
def success(score):
    result=""
    if score>32:
        result='PASSED'
    else:
        result='FAILED'
    
    exp={'score':score,'result':f"You are {result}"}

    return render_template('result1.html',results=exp)

if __name__=="__main__":
    app.run(debug=True)