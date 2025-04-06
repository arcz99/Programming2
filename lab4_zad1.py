from flask import Flask


users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <h1>Aplikacja FLASK</h1>
    <p><a href='/about'>O nas</a></p>
    <p><a href='/users'>Lista użytkowników</a></p>
    """

@app.route('/about')
def about():
    return """
    <h1>O nas</h1>
    <h2>Zajmujemy sie niczym</h2>
    <p><a href='/'>Powrót na stronę główną</a></p>
    """

@app.route('/users')
def users_list():
    user_links = ''.join([f'<p><a href="/user/{user_id}">{user["name"]}</a></p>' for user_id, user in users.items()])
    return f"""
    <h1>Lista użytkowników</h1>
    {user_links}
    <p><a href='/'>Powrót na stronę główną</a></p>
    """
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = users.get(user_id)
    if user is None:
        return "Użytkownik nie istnieje", 404
    return f"""
    <h1>Profil użytkownika</h1>
    <p>{user["name"]}, {user["age"]} lat</p>
    <p><a href='/users'>Powrót do listy użytkowników</a></p>
    """


if __name__ == '__main__':
    app.run(debug=True)




