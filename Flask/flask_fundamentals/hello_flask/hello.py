from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def success():
  return "Dojo"  
@app.route('/say/<name>')
def say(name):
    return "Hi " + name
@app.route('/repeat/<int:number>/<name>')
def repeat(number,name):
    return name * number 
if __name__=="__main__":      
    app.run(debug=True) 
