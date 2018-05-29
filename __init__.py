from flask import Flask, request, redirect, session, \
url_for, abort, render_template, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import time
import os

app = Flask(__name__)
app.config.from_object('config')
#initialize database
engine = create_engine(
    'mysql+pymysql://root:@localhost:3306/TrainTimetable?charset=utf8')
#create a session
DBSession = sessionmaker(bind = engine)
dbsession = DBSession()

@app.route('/')
def home():
    return render_template('Homepage.html')

if __name__ == '__main__':

    #create tables
    #Base.metadata.create_all(engine)
    #run
    app.run(host = '0.0.0.0', debug = True)
    dbsession.close()
