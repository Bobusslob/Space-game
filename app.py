
from flask import Flask, render_template, request,jsonify
import sqlite3

app = Flask(__name__)
DB = 'game_scores.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS game_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')

init_db()
@app.route('/')

@app.route("/leaderboard")
def leaderboard():
    with sqlite3.connect(DB) as conn: 
        data = conn.execute(
            'SELECT username, score FROM game_scores ORDER BY SCORE DESC LIMIT 20'
        ).fetchall()
    return render_template('leaderboard.html',data=data)

@app.route('/api/scores', methods=['POST'])
def scores():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    score = data.get('score')
    with sqlite3.connect(DB) as conn:
        conn.execute(
            'INSERT INTO game_scores (username, score) VALUES (?, ?)',
            (username, score)
        )
    return jsonify({"status": "success", "message": "Score saved!"}), 200

if __name__=='__main__':
    app.run(debug=True)