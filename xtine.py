from flask import Flask, render_template

# let there be Flask
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html', url='index')


@app.route('/projects')
def projects():
    return render_template('projects.html', url='projects')


if __name__ == '__main__':
    app.run()
