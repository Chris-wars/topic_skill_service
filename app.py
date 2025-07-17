import os # Importiert das OS-Modul für die Interaktion mit dem Betriebssystem, z.B. Dateipfade
from flask import Flask, jsonify # Importiert Flask-Klasse zum Erstellen der Webanwendung und jsonify zum Konvertieren von Python-Objekten in JSON-Antworten
from data_manager import JsonDataManager# Importiert das data_manager-Modul, das die JsonDataManager-Klasse enthält

app = Flask(__name__) # Initialisiert die Flask-Anwendung. __name__ hilft Flask, den Stammordner für die App zu finden.
data_manager = JsonDataManager() # Erstellt eine Instanz der JsonDataManager-Klasse, um JSON-Daten zu verwalten

# Definiert den Pfad zum Datenverzeichnis relativ zum aktuellen Skript
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
# Definiert den vollständigen Pfad zur topics.json-Datei im Datenverzeichnis
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')


@app.route('/') # Definiert eine Route für die Startseite ('/')
def hello_world():
    # Gibt eine einfache Begrüßungsnachricht zurück, wenn die Startseite aufgerufen wird
    return 'Hello from Topic and Skill Service!'


@app.route('/topics', methods=['GET']) # Definiert eine Route für '/topics', die nur GET-Anfragen akzeptiert
def get_topics():
    """
    Endpunkt zum Abrufen aller Themen aus der topics.json-Datei.
    Gibt eine JSON-Antwort mit der Liste der Themen zurück.
    """
    topics = data_manager.read_data(TOPICS_FILE) # Ruft die Themen aus der JSON-Datei ab
    return jsonify(topics) # Konvertiert die Themenliste in eine JSON-Antwort und gibt sie zurück

if __name__ == '__main__':
    # Dieser Block wird nur ausgeführt, wenn das Skript direkt gestartet wird (nicht importiert)
    app.run(debug=True, port=5000) # Startet den Flask-Entwicklungsserver
    # debug=True ermöglicht den Debug-Modus (automatische Neuladung bei Codeänderungen und detaillierte Fehlermeldungen)
    # port=5000 legt den Port fest, auf dem der Server lauscht
