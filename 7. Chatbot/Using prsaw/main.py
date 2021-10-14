from flask import Flask, render_template, request
from prsaw import RandomStuffV2

app = Flask(__name__)

@app.route("/")
def fun():
    return render_template('index.html')

@app.route("/get_response", methods = ['GET', 'POST'])
def get_response():
    if request.method == 'POST':
        rs = RandomStuffV2()
        user_text = request.form.get('msg') 
        response = rs.get_ai_response(user_text)  # result will be in dict type -->  {'message': 'Wassup man, how you doing.'}
        return response['message']
    return render_template('index.html')

if __name__ == "__main__":
    app.run()