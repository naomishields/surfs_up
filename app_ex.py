# importing dependency
from flask import Flask

# create a new instance
app = Flask(__name__)

# defining starting point
@app.route('/')
def hello_world():
    return 'Hello world'