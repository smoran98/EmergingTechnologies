import flask as fl

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('webpage.html')

app.run()