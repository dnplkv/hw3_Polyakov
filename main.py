from flask import Flask
from faker import Faker
import requests
import random
import string
fake = Faker()


app = Flask(__name__)


@app.route('/generate-users')
def generate_twenty_users() -> str:
    name_gen = [fake.name() for _ in range(20)]
    email_gen = [fake.free_email() for _ in range(20)]
    merged_data = tuple(zip(name_gen, email_gen))
    return '<br/>'.join(map(', '.join, merged_data))


@app.route('/users/generate/')
@app.route('/users/generate/<int:len>')
def generate_users(len=0) -> str:
    if len > 0:
        name_gen = [fake.name() for _ in range(len)]
        email_gen = [fake.free_email() for _ in range(len)]
        merged_data = tuple(zip(name_gen, email_gen))
        return '<br/>'.join(map(', '.join, merged_data))
    else:
        return 'Set a wanted number of user(s) to be generated'


@app.route('/password/generate')
@app.route('/password/generate/<int:len>')
def generate_password(len=0) -> str:
    if len > 0:
        password = [random.choice(string.ascii_letters + string.digits) for _ in range(len)]
        return "".join(password)
    else:
        return 'Set a wanted length of password to be generated'


@app.route('/astro')
def astro_counter() -> str:
    r = requests.get('http://api.open-notify.org/astros.json', json={"key": "value"})
    data = r.json()
    return f"Number of astronauts: {data['number']}"


if __name__ == "__main__":
    app.run(debug=True)
