from flask import Flask, request, redirect, render_template, url_for, session, Response
from authy.api import AuthyApiClient

app = Flask(__name__)

# +16786162693
# SID - AC3f89b59e38e908bc00e652cf69f209d1
# Auth Token - 911b3583f3c487d0473b79af7ab811df

app.config.from_object('config')
app.secret_key = 'jsiauHyueajkajhs'
api = AuthyApiClient(app.config['AUTHY_API_KEY'])

@app.route("/phone_verification", methods=["GET", "POST"])
def phone_verification():
    if request.method == "POST":
        country_code = request.form.get("country_code")
        phone_number = request.form.get("phone_number")
        method = request.form.get("method") 

        session['country_code'] = country_code
        session['phone_number'] = phone_number

        api.phones.verification_start(phone_number, country_code, via=method)
        return redirect(url_for("verify"))
    return render_template("phone_verification.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        token = request.form.get("token")

        phone_number = session.get("phone_number")
        country_code = session.get("country_code")

        verification = api.phones.verification_check(phone_number,country_code,token)
        print(str(verification))
        if verification.ok():
            return Response("<h1>Success!</h1>")
    return render_template("verify.html")


if __name__ == '__main__':
    app.run()