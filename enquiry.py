from flask import Flask, request
from flask_mysqldb import MySQL
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registration'

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

    return "Enquiry Submitted"

if __name__ == '__main__':
    app.run()