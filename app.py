from flask import Flask , render_template , request
from google import genai
from dotenv import load_dotenv
import os


gemini_api_key=os.getenv('gemini_api_key')
client = genai.Client(api_key="")
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =="GET":
        return render_template('index.html')
    elif request.method=='POST':

        v1=request.form['name']
        v2=request.form['gender']
        v3=int(request.form['age'])
        v4=int(request.form['height'])
        v5=int(request.form['weight'])
        v6=request.form['target']
        v7=request.form['fp']

        response = client.models.generate_content(
            model="gemini-3.5-flash", contents=f"my name is {v1}. i am {v3} year old {v2}. My height is {v4} and weight is {v5}. "
                                               f"i want to {v6} and my food preference is {v7} food. so according to my given data "
                                               f"my a 7 days diet plan for me to achive my target and also suggest the helth tips. "
                                               f"make sure all the result in html format apply proper css to it so that it look "
                                               f"attractive and intractive. result must be in html format don't show any additional "
                                               f"information "
        )
        # print(response.text)
        return render_template('result.html',result=response.text)
app.run(debug=True)



