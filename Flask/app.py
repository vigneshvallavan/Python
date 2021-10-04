# import main Flask class and request object
from flask import Flask, request,render_template
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

# create the Flask app
app=Flask(__name__)

html = urlopen('file:///C:\\Users\\US\\Desktop\\Python Programming\\Flask\\templates\\index.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/move_forward')
def move_forward():   
        ip = request.remote_addr

        soup = BeautifulSoup(html,'html.parser')
        soup2 = soup.find('h1')
        product = soup2.text

        e = datetime.datetime.now() 
        current_date_time = e.strftime("%Y-%m-%d %H:%M:%S")

        result ="Date & Time : " + str(current_date_time) + ", IP Address = " + str(ip) + ", Product Name = " + str(product)
        print('result =' ,result)   
           
        filename = 'click_events.txt'
        f = open(filename,'w')
        f.write(str(result))

        return render_template('cart.html')
    
if __name__ == '__main__':    
    app.run(debug=True,port=5000)           # run app in debug mode on port 5000