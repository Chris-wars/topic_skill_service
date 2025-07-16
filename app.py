# app.py
from flask import Flask

# Erstellt eine Instanz der Flask-Anwendung
app = Flask(__name__)

# Definiert eine Route für die Stamm-URL ('/')
@app.route('/')
def hello_world():
    """
    Diese Funktion wird aufgerufen, wenn die Stamm-URL aufgerufen wird.
    
    """
    return 'Hello from Topic and Skill Service!'

# Stellt sicher, dass die Anwendung nur gestartet wird, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    # Startet den Flask-Entwicklungsserver
    # debug=True ermöglicht den Debug-Modus, der automatische Neuladungen bei Codeänderungen bietet
    app.run(debug=True, port=5000)
