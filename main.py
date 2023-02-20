from flask import Flask, jsonify, request
import csv

all_articles= []
with open('articles.csv') as f:
    reader= csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


liked_articles = []
disliked_articles = []
did_not_watch_articles = []

app = Flask(__name__)

@app.route('/get-article')
def get_article(): 
    return jsonify({
        'data': all_articles[0],
        "status": 'success'    
    })

@app.route('like-article', methods=["POST"])
def liked_article(): 
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status': 'sucess'
    })
    
@app.route('disliked-article', methods=["POST"])
def disliked_article(): 
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        'status': 'sucess'
    })

@app.route('did-not-watch', methods=["POST"])
def did_not_watch(): 
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        'status': 'sucess'
    })
    
if __name__ == "__main__" :
    app.run() 


