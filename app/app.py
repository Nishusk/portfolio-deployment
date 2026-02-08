from flask import Flask, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Nishu Kumari - DevOps Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: white;
            border-radius: 15px;
            padding: 50px;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        .header h1 { color: #667eea; font-size: 3em; margin-bottom: 10px; }
        .header p { color: #666; font-size: 1.3em; }
        .badge {
            background: #10b981;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            margin-top: 20px;
            display: inline-block;
            font-weight: bold;
        }
        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        .card h2 { color: #667eea; margin-bottom: 20px; font-size: 1.8em; }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        .skill {
            background: #667eea;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        .project {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
        }
        .project h3 { color: #333; margin-bottom: 10px; }
        .footer {
            background: white;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        .deployment-info {
            background: #e0e7ff;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 0.9em;
            color: #4c1d95;
        }
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .social-link {
            color: #667eea;
            text-decoration: none;
            font-size: 1.1em;
            padding: 10px 20px;
            border: 2px solid #667eea;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .social-link:hover {
            background: #667eea;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>👩‍💻 Nishu Kumari</h1>
            <p>Aspiring DevOps Engineer</p>
            <div class="badge">🚀 Open to DevOps Opportunities</div>
        </div>

        <div class="cards">
            <div class="card">
                <h2>🎯 About Me</h2>
                <p style="line-height: 1.8; color: #666;">
                    Passionate DevOps enthusiast with hands-on experience in containerization, 
                    CI/CD pipelines, and cloud technologies. Currently building real-world 
                    projects to demonstrate practical skills in modern DevOps practices.
                </p>
            </div>

            <div class="card">
                <h2>🛠️ Technical Skills</h2>
                <div class="skills">
                    <span class="skill">🐳 Docker</span>
                    <span class="skill">☁️ Google Cloud</span>
                    <span class="skill">🔄 CI/CD</span>
                    <span class="skill">🐍 Python</span>
                    <span class="skill">🐧 Linux</span>
                    <span class="skill">📊 Git/GitHub</span>
                    <span class="skill">⚙️ GitHub Actions</span>
                    <span class="skill">🔧 Bash Scripting</span>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>📂 Featured Projects</h2>
            
            <div class="project">
                <h3>🚀 Automated Cloud Deployment Pipeline</h3>
                <p><strong>Description:</strong> Built an end-to-end CI/CD pipeline that automatically 
                deploys this containerized application to Google Cloud Run. Reduced deployment time 
                from 30 minutes to 2 minutes (93% improvement).</p>
                <p style="margin-top: 10px;"><strong>Technologies:</strong> Docker, GitHub Actions, 
                Google Cloud Run, Python Flask, Git</p>
                <p style="margin-top: 10px; color: #10b981;"><strong>✅ Currently Live</strong></p>
            </div>
        </div>

        <div class="footer">
            <h2 style="color: #667eea; margin-bottom: 20px;">📧 Let's Connect</h2>
            
            <div class="social-links">
                <a href="mailto:nishuskumari05@gmail.com" class="social-link">📧 Email</a>
                <a href="https://github.com/Nishusk" target="_blank" class="social-link">💻 GitHub</a>
                <a href="https://www.linkedin.com/in/nishu-k-b7b34621a/" target="_blank" class="social-link">🔗 LinkedIn</a>
            </div>
            
            <div class="deployment-info">
                <strong>🚀 Deployment Info</strong><br>
                Platform: Google Cloud Run<br>
                Last Updated: {{ timestamp }}<br>
                Status: ✅ Production
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(TEMPLATE, timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
