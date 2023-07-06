from flask import Flask
import os

app = Flask(__name__)

# Load configuration to flask app
ENV = os.getenv("ENV", default="DEV")
if(ENV == "PROB") :
    app.config.from_object('config.ProductionConfig')
elif(ENV == "DEV") :
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.TestingConfig')

from app import views