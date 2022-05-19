from flask import Flask, render_template
import requests as req
from settings import *
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    response = req.get(URL)
    title = BeautifulSoup(response.text,'lxml').select_one('#firstHeading').text.strip()
    src = response.url
    return render_template('index.html',**{'title':title,'src':src})

app.run()