from flask import Flask
from flask import request,render_template
import os

app = Flask(__name__)

#loading configuration for .env file
app.config['analysisPath']=os.environ.get("ANALYSIS_PATH")
app.config['DB_USERNAME'] = os.environ.get("DB_USERNAME")
app.config['DB_PASSWORD'] = os.environ.get("DB_PASSWORD")
app.config['DB_HOST'] = os.environ.get("DB_HOST")
app.config['DB_NAME'] = os.environ.get("DB_NAME")

from app import index
from app import analyzer
# if __name__ == "__main__":
#     app.run(debug=True)