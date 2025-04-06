from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return """
    <h1>O aplikacji</h1>
    <p>Aplikacja TO-DO do organizacji zadań</p>
    <p><a href="/">Powrót na stronę główną</a></p>
    """

if __name__ == '__main__':
    app.run(debug=True)