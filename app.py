# Import the operating system
# Importing Flask module
# In order to use our environment variables, we need to import the 'env' package.

import os
from flask import Flask
if os.path.exists("env.py"):
    import env
    

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

# Telling the app how and where to run the application

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True) # Be sure to change to FALSE upon deployment