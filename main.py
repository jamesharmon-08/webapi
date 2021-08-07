from flask import Flask, render_template
import requests
from random import randint

URL_END = "https://the-one-api.dev/v2/quote"
headers = {'Authorization': 'Bearer USE_YOUR_OWN_KEY'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'

@app.route('/')
def home():
    return render_template("index.html", quote=get_quote())

def get_quote():
    response = requests.get(url=URL_END, headers=headers)
    data = response.json()
    quote = data['docs'][randint(0, 1000)]['dialog']
    print(quote)
    return quote

if __name__ == "__main__":
    app.run(debug=True)




