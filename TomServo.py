from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)
from bs4 import BeautifulSoup
import requests
import random

quotes = []
for quote in quotes:
    quote.replace("\n", "<br>")

source = requests.get('https://en.wikiquote.org/wiki/Mystery_Science_Theater_3000').text 

soup = BeautifulSoup(source, 'lxml')

for funnies in soup.find_all('dl'):
    formatted_quote = funnies.text.replace("\n", "<br>")
    quotes.append(formatted_quote)

mst3kquotes = quotes[random.randint(0,2649)]

@app.route("/")
def home():
    return render_template("CrowTRobot.html", content=random.choice(quotes))
if __name__ == "__main__":
    app.run(debug=True)