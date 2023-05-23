from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print("Charging {{Customer name}} for {{count}} fruits")
    
    nameFruit1_from_form = request.form['nameFruit1']
    nameFruit2_from_form = request.form['nameFruit2']
    nameFruit3_from_form = request.form['nameFruit3']
    firstname_from_form = request.form['firstname']
    lastname_from_form = request.form['lastname']
    id_from_form = request.form['id']
    return render_template("checkout.html",nameFruit1_from_form=nameFruit1_from_form,nameFruit2_from_form=nameFruit2_from_form,
                          nameFruit3_from_form=nameFruit3_from_form,firstname_from_form=firstname_from_form,
                          lastname_from_form=lastname_from_form,id_from_form=id_from_form  )
@app.route('/fruits')         
def fruits():
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    