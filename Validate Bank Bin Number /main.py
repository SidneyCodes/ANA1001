from flask import Flask, render_template, request
from validate import valid
import time
import json
import os.path

app = Flask('app')

@app.route('/', methods = ['GET', 'POST'])
def order():
  return render_template("index.html")

@app.route('/form', methods = ['GET', 'POST'])
def form_data():
    if request.method == 'POST':
        data = request.form
        print(data)
        
        #logging
        log = {}
        log[time.time()] = data 
        path = 'static/logs'
        
        with open(os.path.join(path, f'{time.time()}-json_data.json'), 'w') as outfile:
            json.dump(log, outfile)
        
        if data["Credit"].isnumeric() == True:
            result = data["Credit"][:6]
            #result = valid(result)
            #turned off validation due to API
            result = True
            if result == True:
                return render_template("success.html",data=data)
            else:
                return render_template("failure.html",data=data)
        else:
            print("Invalid Card")
            return render_template("failure.html",data=data)
        if result == True:
            return render_template("success.html",data=data)
        else:
            return render_template("failure.html",data=data)

app.run(host='0.0.0.0', port=8080)
