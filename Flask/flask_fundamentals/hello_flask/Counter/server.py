from flask import Flask, render_template, redirect,request, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    if 'count'and'counter' not in session:
        session['count'] = 1
        session['counter'] = 1
    else:
        session['count'] += 1
        session['counter'] += 1
    return render_template("index.html", count=session['count'],real_count= session['counter'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/user',methods=['POST'])
def user_number():
    session['number'] = request.form['number']
    session['count'] += int(session['number'])-1
   
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)