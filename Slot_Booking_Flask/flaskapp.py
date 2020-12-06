from flask import Flask, render_template
app = Flask(__name__)

bookings = [
{
        "Day":"1",
        "Time":"10:00",
        "Name":"Harsh",
        "Event":"1"
    },

{
        "Day":"1",
        "Time":"10:30",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"1",
        "Time":"10:45",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"1",
        "Time":"11:00",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"1",
        "Time":"11:15",
        "Name":"NIL",
        "Event":"1"
    },

{
        "Day":"2",
        "Time":"10:00",
        "Name":"Sanjay",
        "Event":"1"
    },

{
        "Day":"2",
        "Time":"10:30",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"2",
        "Time":"10:45",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"2",
        "Time":"11:00",
        "Name":"NIL",
        "Event":"1"
    },
{
        "Day":"2",
        "Time":"11:15",
        "Name":"NIL",
        "Event":"1"
    },
]



@app.route('/')
@app.route('/home')
def hello():
    return render_template("home.html", bookings = bookings)


@app.route('/about')
def about():
    return("<h1>About page!<h1>")



if __name__ == "__main__":
    app.run(debug=True)