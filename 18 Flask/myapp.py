from flask import Flask

### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"
@app.route('/index')
def index():
    return "Weclome to index"

if __name__=="__main__":
    app.run(debug=True)