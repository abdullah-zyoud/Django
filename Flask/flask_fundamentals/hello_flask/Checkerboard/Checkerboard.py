from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/')                           
def print():
    return render_template('index.html',row=8,colom=8,color1="red",color2="black") 
@app.route('/<row>')                           
def row(row):
    return render_template('index.html',row=int(row),colom=8,color1="red",color2="black")
@app.route('/<row>/<colom>')                           
def row_colom(row,colom):
    return render_template('index.html',row=int(row),colom=int(colom),color1="red",color2="black")
@app.route('/<row>/<colom>/<color1>/<color2>')                           
def row_colom_color(row,colom,color1,color2):
    return render_template('index.html',row=int(row),colom=int(colom),color1=color1,color2=color2)  

    
if __name__=="__main__":
    app.run(debug=True)                   

