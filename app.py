from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Embedded Webpage</title>
    </head>
    <body>
        <h1>Embedded Content</h1>
        <iframe src="https://discord.com" width="100%" height="600px">
            <p>Your browser does not support iframes.</p>
        </iframe>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(port=8080)
