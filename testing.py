from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # when going to this route...
def index(): # this function is called
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', the_name=name)

if __name__ == '__main__':
    app.debug = True
    app.run() # start the server specified above
