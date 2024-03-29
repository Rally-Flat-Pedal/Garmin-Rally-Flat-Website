from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/') # when going to this route...
def index(): # this function is called
    # return render_template('P1_page.html')
    # return render_template('index.html')
    return render_template('index.html')


@app.route('/static/')
def get_image(image_name):
    return send_from_directory('images', image_name)

@app.route('/background')
def background():
    with open('static/text/problem_statement.txt', 'r') as file:
        content = file.read()
    paragraphs = content.split('\n\n')
    return render_template('./background.html', paragraphs=paragraphs)

@app.route('/research')
def research():
    return render_template('./research.html')

@app.route('/testing')
def testing():
    return render_template('./testing.html')

@app.route('/designs')
def prototypes():
    return render_template('./designs.html')

@app.route('/prototype_1')
def prototype1():
    return render_template('./prototype_1.html')

@app.route('/manufacturing')
def manufacturing():
    return render_template('./manufacturing.html')

@app.route('/the_team')
def the_team():
    return render_template('./the_team.html')


if __name__ == '__main__':
    app.debug = True
    app.run() # start the server specified above

