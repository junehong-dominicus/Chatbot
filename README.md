# Chatbot

# The Setup

You are working on a database-backed web-app in which you have to fix bugs and add new functionality (sounds familiar?).

The application is written in the language you are most comfortable with. The choice is yours! You can find the Python version of this app in the solution folder and you can run it by executing the supplied `run.sh` script. If you choose to build your solution in a language other than Python, that's great! Just make sure that you also modify `run.sh` so that we'll be able to run your solution solely by calling that script. Ensure that any necessary libraries are properly installed and please have it run in Docker like the example we've given.

The database of the application can be queried through SQL and has the following schema:

![db schema](resources/database.png)

This is a simplified version of our bot schema, in which an `answer` (something that a bot says) consists of several, potentially deeply nested "blocks" (that are all stored as one big JSON blob per answer in the `blocks` table). These blocks represent functionality, such as showing text, showing images, performing HTTP requests, etc. The lower row of the diagram shows the `messages` table which show the messages that the bot has sent. Finally, `state` includes some conversation state that will be relevant in the first challenge.

Unlike in real-life there is also a test-suite that will give you instant feedback on whether your solution works or not. You can run the tests with the `run_tests_in_docker.sh` script located in the tests folder, or, if you prefer, feel free to run them directly with `python3 tests/testname.py`.

# Challenge 1: Messages

The `/messages` endpoint returns all the messages in the database. Try running the application and hitting the endpoint [in your browser](http://localhost:5000/messages) or through `curl http://localhost:5000/messages` (do it now!).

Unfortunately, as you can see, the messages only show the message *template* instead of the actual message because the variable values have not been filled in! In our message template, variables are identified by `{|}`. Everything after the initial `{` and before the `|` is the variable id, and everything after the `|` but before the closing `}` is a _fallback_ value, in case there is no value for this variable.

In this application, variable values are stored in the `state` table. For example, consider the template string `Hello {asdf|planet}`. If the `state` table has a row with the id `asdf`, and value of `Earth`, then the processed message should read `Hello Earth`. If no such row exists, then the string should read `Hello planet`.

Your mission, should you choose to accept it, is to modify the `/messages` route to fill in the correct variable values into the messages so that we may all profit from the wisdom within!

You can test your result by running `tests/run_tests_in_docker.sh` or `python3 tests/test_messages.py`


# Challenge 2: Search
The `/search` endpoint performs a search for answers based on their titles, for example:

```sh
curl -d '{"query":"Star Trek"}' -H "Content-Type: application/json" -X POST http://localhost:5000/search
```

will result in
```js
[{
    "id": 3,
    "title": "Star Trek API"
 }]
```

Due to changing business requirements and demanding clients, you will now have to modify the endpoint to not only return the _full_ answer (including its blocks), but also allow search within the content block fields! Don't forget to _also_ search the title, and while you're at it, please make sure that the endpoint `400`s on invalid input, as is best practice. Lastly, we now also want to support searching for multiple terms that **all** have to show up **somewhere** in the answer.

You can test your solution by running `tests/run_tests_in_docker.sh` or `tests/test_search.py`. Have a look at it too, as it will probably answer a lot of the questions you may be having.

It's possible to cheat your way into something that passes the specific test cases provided but goes against the spirit of the question. We'd rather you solve what we _mean_ and not *just* colour inside the lines that the tests provide :)

Good luck and ... _live long and prosper_ 🖖
