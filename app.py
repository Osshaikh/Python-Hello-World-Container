from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IIT Bombay Workshop</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #1e3c72 100%);
                color: white;
            }
            .container {
                text-align: center;
                padding: 40px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                max-width: 600px;
                margin: 20px;
            }
            .logo {
                font-size: 60px;
                margin-bottom: 20px;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            .subtitle {
                font-size: 1.8rem;
                color: #ffd700;
                margin-bottom: 20px;
                font-weight: bold;
            }
            .welcome-text {
                font-size: 1.2rem;
                line-height: 1.6;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .tech-stack {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-top: 20px;
            }
            .tech-badge {
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-size: 0.9rem;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .divider {
                height: 2px;
                background: linear-gradient(90deg, transparent, #ffd700, transparent);
                margin: 25px 0;
            }
            .footer {
                margin-top: 20px;
                font-size: 0.9rem;
                opacity: 0.7;
            }
            .pulse {
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">🎓</div>
            <h1>Welcome to</h1>
            <div class="subtitle pulse">IIT Bombay Workshop</div>
            <div class="divider"></div>
            <p class="welcome-text">
                Learn how to build, containerize, and deploy applications to the cloud!<br>
                This app is running on <strong>Azure Container Apps</strong> 🚀
            </p>
            <div class="tech-stack">
                <span class="tech-badge">🐍 Python</span>
                <span class="tech-badge">🐳 Docker</span>
                <span class="tech-badge">☁️ Azure</span>
            </div>
            <div class="divider"></div>
            <p class="footer">December 2025 | Powered by Azure Container Apps</p>
        </div>
    </body>
    </html>
    '''
    return html

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



  