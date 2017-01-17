from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
          <br><a href="/hello">To go to the greeting, click here</a><html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          Choose a compliment:
            <input type="radio" name="compliment" value="awesome">Awesome
            <input type="radio" name="compliment" value="terrific">Terrific
            <input type="radio" name="compliment" value="fantastic">Fantastic
          <br><input type="submit">
        </form><br>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label><br>
          Choose an insult:
            <input type="radio" name="insult" value="smelly">Smelly
            <input type="radio" name="insult" value="funnylooking">Funny-Looking
            <input type="radio" name="insult" value="Mother was a hamster and Father smelled of elderberries! (*your)">Monty Python
          <br><input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    #compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s, I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    #compliment = choice(AWESOMENESS)
    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s, I think you're %s!
      </body>
    </html>
    """ % (player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
