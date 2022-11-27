from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt

app = Flask(__name__)
app.secret_key = "development"
# TO DO
# We need a MongoDB database launched in order to be able to give it
# as a client to Flask using
# client = pymongo.MongoClient("insert MongoDB here")