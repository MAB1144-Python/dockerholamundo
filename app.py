from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hola Mundo Docker UNAD</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f0f0f0;
            }
            h1 {
                color: #333;
                font-size: 3em;
            }
            .container {
                background-color: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola Mundo UNAD!</h1>
            <p>Esta aplicación está corriendo en Docker 🐳</p>
            <p>Python + Flask + Docker = ❤️</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)