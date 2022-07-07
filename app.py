from distutils.log import debug
from flask import Flask
from housing.logger import logging
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("we are running this code")

    return "ML projects started"


if __name__=="__main__":
    app.run(debug=True)