from flask import Flask, render_template


# let there be Flask
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', url='about')


@app.route('/projects')
def projects():
    return render_template('projects.html', url='projects')


if __name__ == '__main__':
    app.run()
