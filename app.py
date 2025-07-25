import os # Importiert das OS-Modul für die Interaktion mit dem Betriebssystem, z.B. Dateipfade
from flask import Flask, jsonify # Importiert Flask-Klasse zum Erstellen der Webanwendung und jsonify zum Konvertieren von Python-Objekten in JSON-Antworten
from data_manager import JsonDataManager# Importiert das data_manager-Modul, das die JsonDataManager-Klasse enthält


app = Flask(__name__) # Initialisiert die Flask-Anwendung. __name__ hilft Flask, den Stammordner für die App zu finden.
data_manager = JsonDataManager() # Erstellt eine Instanz der JsonDataManager-Klasse, um JSON-Daten zu verwalten


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') # Definiert den Pfad zum Datenverzeichnis relativ zum aktuellen Dateipfad
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json') # Definiert den Pfad zur topics.json-Datei im Datenverzeichnis
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json') # Definiert den Pfad zur skills.json-Datei im aktuellen Verzeichnis


@app.route('/') # Definiert eine Route für die Startseite ('/')
def hello_world():
    # Gibt eine einfache Begrüßungsnachricht zurück, wenn die Startseite aufgerufen wird
    return 'Hello from Topic and Skill Service!'


@app.route('/topics', methods=['GET']) # Definiert eine Route für '/topics', die nur GET-Anfragen akzeptiert
def get_topics():

    topics = data_manager.read_data(TOPICS_FILE) # Ruft die Themen aus der JSON-Datei ab
    return jsonify(topics) # Konvertiert die Themenliste in eine JSON-Antwort und gibt sie zurück


@app.route('/topics/<id>', methods=['GET']) # Definiert eine Route für '/topics/<id>', die GET-Anfragen akzeptiert, wobei <id> ein Platzhalter für die Themen-ID ist
def get_topic_by_id(id):
    
    topics = data_manager.read_data(TOPICS_FILE) # Ruft die Themen aus der JSON-Datei ab
    topic = next((topic for topic in topics if topic.get('id').lower() == id.lower()), None) # Sucht das Thema mit der angegebenen ID in der Liste der Themen
    if topic:
        return jsonify(topic) # Konvertiert das gefundene Thema in eine JSON-Antwort und gibt es zurück, falls vorhanden
    else:
        return jsonify({"[ERROR]": "Topic ID Not found"}), 404


@app.route('/skills', methods=['GET']) # Definiert eine Route für '/skills', die nur GET-Anfragen akzeptiert
def get_skills():

    skills = data_manager.read_data(SKILLS_FILE) # Ruft die Fähigkeiten aus der JSON-Datei ab
    return jsonify(skills) # Konvertiert die Fähigkeitenliste in eine JSON-Antwort und gibt sie zurück


@app.route('/skills/<id>', methods=['GET']) # Definiert eine Route für '/skills/<id>', die GET-Anfragen akzeptiert, wobei <id> ein Platzhalter für die Fähigkeits-ID ist
def get_skill_by_id(id): # Ruft eine einzelne Fähigkeit anhand ihrer ID aus der JSON-Datei ab und gibt sie als JSON-Antwort zurück

    skills = data_manager.read_data(SKILLS_FILE) # Ruft die Fähigkeiten aus der JSON-Datei ab
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None) # Sucht die Fähigkeit mit der angegebenen ID in der Liste der Fähigkeiten
    if skill:   # Wenn die Fähigkeit gefunden wurde, wird sie als JSON-Antwort zurückgegeben
        return jsonify(skill) # Konvertiert die gefundene Fähigkeit in eine JSON-Antwort und gibt sie zurück
    else:# Wenn die Fähigkeit nicht gefunden wurde, wird eine Fehlermeldung zurückgegeben
        return jsonify({"[ERROR]": "Skill ID Not found"}), 404 # Gibt eine Fehlermeldung zurück, wenn die Fähigkeit nicht gefunden wurde, mit Statuscode 404 (Nicht gefunden)


if __name__ == '__main__':
    # Dieser Block wird nur ausgeführt, wenn das Skript direkt gestartet wird (nicht importiert)
    app.run(debug=True, port=5000) # Startet den Flask-Entwicklungsserver
    # debug=True ermöglicht den Debug-Modus (automatische Neuladung bei Codeänderungen und detaillierte Fehlermeldungen)
    # port=5000 legt den Port fest, auf dem der Server lauscht
