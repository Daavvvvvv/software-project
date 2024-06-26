from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

phrases = [
    "Sevval Ates is the most beautiful girl everr",
    "The best way to live in the future is living with you",
    "Sevval mean the world to me",
    "Ates mean the life to me",
    "Get ready to be inspired…",  
    "See rejection as redirection.", 
    "There is beauty in simplicity.", 
    "You can’t be late until you show up.", 
    "Maybe life is testing you. Don’t give up.", 
    "Impossible is just an opinion.", 
    "Alone or not you gonna walk forward.", 
]


@app.route('/')
def get_random_quote():
    phrase = random.choice(phrases)
    container_id = os.uname()[1] 
    return f"{phrase} - Container Id: {container_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)