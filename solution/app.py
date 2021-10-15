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
    # with sqlite3.connect(DBPATH) as conn:
    #     messages_res = conn.execute("select body from messages")
    #     messages = [m[0] for m in messages_res]
    #     return jsonify(list(messages)), 200

    with sqlite3.connect(DBPATH) as conn:
        messages = []
        messages_res = conn.execute("select body from messages")
        for message in messages_res:
            message_str = str(message[0])
            regex = r"\{.*?\}"
            templates = re.findall(regex, str(message))
            for template in templates:
                regex = r"{|\||}"
                state = re.split(regex, template)
                values = conn.execute("select value from state where id=:id", {"id": state[1]})
                value = values.fetchall()
                if len(value):
                    for v in value:
                        message_str = message_str.replace(template, v[0])
                else:
                    message_str = message_str.replace(template, state[2])
            messages.append(message_str)
        return jsonify(messages), 200

@app.route("/test", methods=["GET"])
def test_route():
    """
    Return all the messages
    """
    print("****************************************************************************")
    with sqlite3.connect(DBPATH) as conn:
        messages = []
        # messages_res = conn.execute("select body from messages")
        # for message in messages_res:
        #     message_str = str(message[0])
        #     print("==========================================================================")
        #     print(message_str)
        #     print("--------------------------------------------------------------------------")
        #     regex = r"\{.*?\}"
        #     templates = re.findall(regex, str(message))
        #     for template in templates:
        #         print("=> " + template)
        #         regex = r"{|\||}"
        #         state = re.split(regex, template)
        #         print("==> " + str(state))
        #         values = conn.execute("select value from state where id=:id", {"id": state[1]})
        #         value = values.fetchall()
        #
        #         if len(value):
        #             # print(value[0])
        #             for v in value:
        #                 print("===> " + v[0])
        #                 message_str = message_str.replace(template, v[0])
        #
        #         else:
        #             print("===> " + "No such row exists!!!" + ", so use " + state[2])
        #             message_str = message_str.replace(template, state[2])
        #     print("====> " + message_str)
        #     messages.append(message_str)
        #     print("****************************************************************************")
        print(messages)
        return jsonify(messages), 200

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
