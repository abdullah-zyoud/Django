from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/play')                           
def display():
    return render_template('index.html',number=3,color="aqua") 
@app.route('/play/<number>')                           
def change_number(number):
    return render_template('index.html',number=int(number),color="aqua") 
@app.route('/play/<number>/<color>')                           
def change_color(number,color):
    return render_template('index.html',number=int(number),color=color) 

if __name__=="__main__":
    app.run(debug=True)                   

