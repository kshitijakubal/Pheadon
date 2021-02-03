from flask import Flask, request, redirect, render_template
from instamojo_wrapper import Instamojo

app = Flask(__name__)



API_KEY = "test_267159126ed2e06fc3687320b4c"

AUTH_TOKEN = "test_8cbbedf17adcb4af655a77608c0"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        # if request.is_json:
        #     content = request.get_json()
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')

        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name=name,
        send_email=True,
        email=email,
        redirect_url="http://localhost:5000/success"
        )

        return redirect(response['payment_request']['longurl'])
    else:
        return redirect('/pay')

@app.route('/success')
def success():
    return render_template('success.html')



if __name__ == '__main__':
    app.run(debug=True)