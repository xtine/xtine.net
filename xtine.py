from flask import Flask, render_template, request, send_from_directory

# let there be Flask
app = Flask(__name__)
app.config.from_object(__name__)


# oh, the places this app will go
@app.route('/')
def index():
    return render_template('index.html', url='index')


@app.route('/about/')
def about():
    return render_template('about.html', url='about')


@app.route('/blog/')
def blog():
    return render_template('blog.html', url='blog')


@app.route('/projects/')
@app.route('/portfolio/')
def projects():
    return render_template('projects.html', url='projects')


@app.route('/contact/')
def contact():
    return render_template('contact.html', url='contact')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/favicon.ico")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    # return send_static_file('favicon.ico')


# run ze app!
if __name__ == '__main__':
    app.run()
