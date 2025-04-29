import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Unknown')
    
    return f"""
    <html>
        <body>
            <h1>Server Information</h1>
            <p><b>Hostname:</b> {hostname}</p>
            <p><b>IP Address:</b> {ip_address}</p>
            <p><b>Author:</b> {author}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)