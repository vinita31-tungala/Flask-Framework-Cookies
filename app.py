from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    return render_template('setcookie.html')  # handle GET requests too

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if name is None:
        name = "guest"  # fallback if no cookie is found
    return f'<h1>Welcome {name}</h1>'  # FIXED: closing tag was broken

if __name__ == '__main__':
    app.run(debug=True)
