import flask

app1 = flask.Flask(__name__)

@app1.route("/")
def fun1():
    return flask.render_template('demo.html')

@app1.route("/demo.html")
def fun2():
    return flask.render_template('demo.html')

@app1.route("/demo2.html")
def fun3():
    return flask.render_template('demo2.html')

@app1.route('/wordFunction')
def wordFunction():
    return "Hello World from Python Coding - Flask"

if __name__ == "__main__":
    app1.run()