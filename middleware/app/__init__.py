from flask import Flask
from flask import request,render_template

app = Flask(__name__)

from app import index
from app import analyzer
# if __name__ == "__main__":
#     app.run(debug=True)