from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Welcome to Flask</h1></html>"

@app.route('/form',methods=['GET','POST'])
def form():
       
    return render_template('marks.html')

@app.route('/success/<int:score>')
def success(score):
    result=""
    if score>32:
        result='PASSED'
    else:
        result='FAILED'
    
    exp={'score':score,'result':f"You are {result}"}

    return render_template('result1.html',results=exp)

@app.route('/result',methods=['POST','GET'])
def result():
    total=0
    math=float(request.form['math'])
    science=float(request.form['science'])
    history=float(request.form['history'])
    english=float(request.form['english'])
    computer=float(request.form['computer'])
    total=math+science+history+english+computer
    percentage=total/5
    return redirect(url_for('success',score=percentage))

if __name__=="__main__":
    app.run(debug=True)