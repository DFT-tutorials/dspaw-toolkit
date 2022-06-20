from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()
test=os.getenv('test')
app = Flask(__name__)

