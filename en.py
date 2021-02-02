from flask import Flask, request
from flask_mysqldb import MySQL
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

app.config['MYSQL_HOST'] = 'us-cdbr-east-03.cleardb.com'
app.config['MYSQL_USER'] = 'b57a400989f5d4'
app.config['MYSQL_PASSWORD'] = 'e8cfc7df'
app.config['MYSQL_DB'] = 'heroku_37ffb1562e3eec2'
#
mysql = MySQL(app)

@app.route('/enquiry',methods=['POST'])
def enquiry():
    # if request.is_json:
    #     content = request.get_json()
    #     username = content['username']
    #     email = content['email']
    #     phoneno = content['phoneno']

    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO enquiry(username, email, phoneno) VALUES(%s, %s, %s)",(username, email, phoneno))
    #     mysql.connection.commit()
    #     cur.close()
    # if request.method == "POST":
    return "Enquiry Submitted"

if __name__ == '__main__':
    app.run()