from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/',methods=['POST'])
def trial():
    if request.is_json:
        content = request.get_json()
        name = content['name']
        if name == "Kshitija":
            return "API Link Successful " + name

if __name__=='__main__':
    app.run()