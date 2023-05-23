from flask import Flask, render_template, request, redirect 
app = Flask(__name__)   
@app.route('/')
def index():
    return render_template("index.html")       
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    Location_from_form = request.form['Location']
    Language_from_form = request.form['Language']
    Comment_from_form = request.form['Comment']
    return render_template("info.html", name_from_form=name_from_form, Location_from_form=Location_from_form ,
                           Language_from_form=Language_from_form ,Comment_from_form=Comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)
