from flask import Flask, escape, request

app = Flask(name)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'