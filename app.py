# Importing of Libraries
from flask import Flask, render_template, request, redirect, url_for
import requests

# Flask App
app = Flask(__name__)
@app.route('/')

# Defining stats function 
def stats():
    url = "https://lob82mgiw0.execute-api.ap-south-1.amazonaws.com/attendance_count/getcount"
    #url = "https://lob82mgiw0.execute-api.ap-south-1.amazonaws.com/attendance_count"
    # Change the above url with your API Url
    response = requests.get(url)
    # Converting the json format
    r = response.json()
    print(r)
    # Rendering the html template
    return render_template('Dashboard.html',a=sum(r),b=str(r[0]),c=str(r[1]))

if __name__ == "__main__":
    app.run(debug=True)