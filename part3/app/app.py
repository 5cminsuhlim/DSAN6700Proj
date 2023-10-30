from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import fetch_openml

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'