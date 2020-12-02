# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

ops_dict = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/<operation>")
def perform_operations(operation):
    """ perform math operations based on the URL and query inputs"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = ops_dict[operation](a, b)
    return f""" <html><body>{result}</body> </html>"""
