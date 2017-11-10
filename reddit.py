#!venv/bin/python
import requests
import json
import struct
import bs4
from flask import Flask, jsonify, render_template, request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath'] 
    return get_articles('r/'+projectpath+'/',1)
	

def get_articles(category='',cattype=0):
    index_url="http://www.reddit.com/"
    while True:
		response=requests.get(index_url+category)
		if response:
			break
    ret=[]
    soup = bs4.BeautifulSoup(response.text)
    posts=soup.select("div#siteTable div.thing")
    for post in posts:
        article=post.select("p.title a")[0]
        ret.append({"title":article.text,"link":article['href']})
	
    
    return render_template('listing.html', article=ret)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)