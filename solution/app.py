from flask import Flask, request, jsonify
import sqlite3
import json
import re # regular expressions
from pprint import pprint


app = Flask(__name__)
DBPATH = "../database.db"

@app.route("/messages", methods=["GET"])
def messages_route():
    """
    Return all the messages
    """

    with sqlite3.connect(DBPATH) as conn:
        messages_res = conn.execute("select body from messages")
        messages = [m[0] for m in messages_res]
        return jsonify(list(messages)), 200

@app.route("/test", methods=["GET"])
def test_route():
    """
    Return all the messages
    """

    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cursor()
        cur.execute("select * from state")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        # messages = [ messages for row in rows ]
        # return jsonify(list(messages)), 200
        return jsonify("list(messages)"), 200

@app.route("/search", methods=["POST"])
def search_route():
    """
    Search for answers!

    Accepts a 'query' as JSON post, returns the full answer.

    curl -d '{"query":"Star Trek"}' -H "Content-Type: application/json" -X POST http://localhost:5000/search
    """

    with sqlite3.connect(DBPATH) as conn:
        query = request.get_json().get("query", None)
        if not query:
            return jsonify({"error": "Invalid input"}), 400
        res = conn.execute(
            "select id, title from answers where title like ? ", [f"%{query}%"],
        )
        answers = [{"id": r[0], "title": r[1]} for r in res]
        print(query, "--> ")
        pprint(answers)
        return jsonify(answers), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
