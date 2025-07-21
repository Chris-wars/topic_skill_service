import os # Für die Interaktion mit dem Betriebssystem, z.B. Dateipfade
import json # Für die Arbeit mit JSON-Daten
import uuid # Zum Generieren eindeutiger IDs
from flask import Flask, jsonify, request # Flask-Bibliothek für Webanwendungen

class JsonDataManager:
    """
    Eine Klasse zur Verwaltung von JSON-Daten in Dateien.
    Diese Version ist dateipfad-agnostisch und die Methoden
    nehmen den Dateipfad als Argument entgegen.
    """
    def read_data(self, file_path):
        """
        Liest Daten aus einer JSON-Datei.
        Gibt eine leere Liste zurück, wenn die Datei nicht existiert oder leer/ungültig ist.
        """
        if not os.path.exists(file_path):
            # Wenn die Datei nicht existiert, gib eine leere Liste zurück
            return []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Versuche, die JSON-Daten aus der Datei zu laden
                return json.load(f)
        except json.JSONDecodeError:
            # Fang den Fehler ab, wenn die Datei kein gültiges JSON ist oder leer ist
            print(f"Warnung: {file_path} ist keine gültige JSON-Datei oder ist leer. Initialisiere mit einer leeren Liste.")
            return []
        except Exception as e:
            # Fang andere potenzielle Fehler beim Lesen ab
            print(f"Fehler beim Lesen von {file_path}: {e}")
            return []

    def write_data(self, file_path, data):
        """
        Schreibt Daten in eine JSON-Datei.
        """
        try:
            # Stelle sicher, dass das Verzeichnis der Datei existiert
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                # Schreibe die Daten formatiert (mit Einrückung) in die JSON-Datei
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            # Fang Fehler beim Schreiben ab
            print(f"Fehler beim Schreiben nach {file_path}: {e}")

# Initialisiere die Flask-Anwendung
app = Flask(__name__)
# Erstelle eine Instanz des JsonDataManager
data_manager = JsonDataManager()

# Definiere die Dateipfade für Topics und Skills
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') # Pfad zum 'data'-Verzeichnis
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json') # Vollständiger Pfad zur topics.json
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json') # Vollständiger Pfad zur skills.json

# --- Start der API-Routen ---

@app.route('/')
def hello_world():
    """
    Einfacher Root-Endpunkt zur Überprüfung, ob der Service läuft.
    """
    return "Hello from Topic and Skill Service!"

@app.route('/topics', methods=['GET'])
def get_topics():
    """
    Gibt eine Liste aller Topics zurück.
    """
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)

@app.route('/skills', methods=['GET'])
def get_skills():
    """
    Gibt eine Liste aller Skills zurück.
    """
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)

@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    """
    Gibt ein spezifisches Topic anhand seiner ID zurück.
    """
    topics = data_manager.read_data(TOPICS_FILE)
    # Suche das Topic mit der passenden ID (Groß-/Kleinschreibung ignorieren)
    topic = next((topic for topic in topics if topic.get('id', '').lower() == id.lower()), None)
    if topic:
        return jsonify(topic)
    else:
        # Wenn Topic nicht gefunden, gib 404 Not Found zurück
        return jsonify({"error": "Topic not found."}), 404

@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    """
    Gibt einen spezifischen Skill anhand seiner ID zurück.
    """
    skills = data_manager.read_data(SKILLS_FILE)
    # Suche den Skill mit der passenden ID (Groß-/Kleinschreibung ignorieren)
    skill = next((skill for skill in skills if skill.get('id', '').lower() == id.lower()), None)
    if skill:
        return jsonify(skill)
    else:
        # Wenn Skill nicht gefunden, gib 404 Not Found zurück
        return jsonify({"error": "Skill not found."}), 404

@app.route('/topics', methods=['POST'])
def create_topic():
    """
    Erstellt ein neues Topic.
    Erwartet JSON mit 'name' und 'description' im Request-Body.
    """
    new_topic_data = request.json

    # Datenvalidierung: Überprüfen, ob 'name' und 'description' vorhanden sind
    if not new_topic_data or 'name' not in new_topic_data or 'description' not in new_topic_data:
        return jsonify({"error": "'name' and 'description' for the topic are required in the request body."}), 400

    # Generiere eine eindeutige ID für das neue Topic
    new_topic_id = str(uuid.uuid4())

    # Erstelle das Topic-Objekt
    topic = {
        "id": new_topic_id,
        "name": new_topic_data['name'],
        "description": new_topic_data['description']
    }

    # Lade bestehende Topics, füge das neue hinzu und speichere sie
    topics = data_manager.read_data(TOPICS_FILE)
    topics.append(topic)
    data_manager.write_data(TOPICS_FILE, topics)

    # Gib das neu erstellte Topic mit Status 201 Created zurück
    return jsonify(topic), 201

@app.route('/skills', methods=['POST'])
def create_skill():
    """
    Erstellt einen neuen Skill.
    Erwartet JSON mit 'name' und 'topicId' im Request-Body.
    """
    new_skill_data = request.json

    # Datenvalidierung: Überprüfen, ob 'name' und 'topicId' vorhanden sind
    if not new_skill_data or 'name' not in new_skill_data or not new_skill_data['name']:
        return jsonify({"error": "Der 'name' des Skills ist erforderlich."}), 400
    if 'topicId' not in new_skill_data or not new_skill_data['topicId']:
        return jsonify({"error": "Die 'topicId' des Skills ist erforderlich."}), 400

    # Generiere eine eindeutige ID für den neuen Skill
    new_skill_id = str(uuid.uuid4())

    # Füge die generierte ID zu den eingehenden Daten hinzu
    new_skill_data['id'] = new_skill_id

    # Lade bestehende Skills, füge den neuen hinzu und speichere sie
    skills = data_manager.read_data(SKILLS_FILE)
    skills.append(new_skill_data) # Füge das vollständige, aktualisierte Dictionary hinzu

    data_manager.write_data(SKILLS_FILE, skills)

    # Gib den neu erstellten Skill mit Status 201 Created zurück
    return jsonify(new_skill_data), 201

@app.route('/topics/<id>', methods=['PUT'])
def update_topic(id):
    """
    Aktualisiert ein bestehendes Topic vollständig anhand seiner ID.
    Erwartet JSON mit den aktualisierten Daten ('name', 'description') im Request-Body.
    """
    updated_data = request.json
    if not updated_data:
        return jsonify({"error": "Der Request-Body muss JSON-Daten enthalten."}), 400

    # Datenvalidierung: 'name' und 'description' sind erforderliche Felder
    if 'name' not in updated_data or not updated_data['name'] or \
       'description' not in updated_data or not updated_data['description']:
        return jsonify({"error": "'name' und 'description' sind erforderliche Felder."}), 400

    topics = data_manager.read_data(TOPICS_FILE)
    topic_found = False
    updated_topic = None

    # Iteriere durch die Topics, um das zu aktualisierende zu finden
    for i, topic in enumerate(topics):
        if topic.get('id', '').lower() == id.lower():
            # Aktualisiere das Topic mit den neuen Daten aus dem Request-Body
            topics[i].update(updated_data)
            topics[i]['id'] = id # Stelle sicher, dass die ID durch das Update nicht überschrieben wird
            updated_topic = topics[i]
            topic_found = True
            break # Breche die Schleife ab, sobald das Topic gefunden und aktualisiert wurde

    if topic_found:
        # Wenn das Topic gefunden und aktualisiert wurde, speichere die Daten und gib 200 OK zurück
        data_manager.write_data(TOPICS_FILE, topics)
        return jsonify(updated_topic), 200
    else:
        # Wenn das Topic nicht gefunden wurde, gib 404 Not Found zurück
        return jsonify({"error": "Topic not found."}), 404

@app.route('/topics/<id>', methods=['DELETE'])
def delete_topic(id):
    """
    Löscht ein bestehendes Topic anhand seiner ID.
    """
    topics = data_manager.read_data(TOPICS_FILE)
    initial_length = len(topics) # Speichere die ursprüngliche Länge der Liste

    # Erstelle eine neue Liste, die alle Topics außer dem zu löschenden enthält
    topics = [topic for topic in topics if topic.get('id', '').lower() != id.lower()]

    if len(topics) < initial_length: # Wenn die Länge der Liste abgenommen hat, wurde ein Topic gelöscht
        data_manager.write_data(TOPICS_FILE, topics)
        return '', 204 # 204 No Content, da nach dem Löschen keine Inhalte zurückgegeben werden
    else:
        # Wenn die Länge nicht abgenommen hat, wurde kein Topic mit der gegebenen ID gefunden
        return jsonify({"error": "Topic not found."}), 404

@app.route('/skills/<id>', methods=['PUT'])
def update_skill(id):
    """
    Aktualisiert einen bestehenden Skill vollständig anhand seiner ID.
    Erwartet JSON mit den aktualisierten Daten ('name', 'topicId') im Request-Body.
    """
    updated_data = request.json
    if not updated_data:
        return jsonify({"error": "Der Request-Body muss JSON-Daten enthalten."}), 400

    # Datenvalidierung: 'name' und 'topicId' sind erforderliche Felder
    if 'name' not in updated_data or not updated_data['name'] or \
       'topicId' not in updated_data or not updated_data['topicId']:
        return jsonify({"error": "'name' und 'topicId' sind erforderliche Felder."}), 400

    skills = data_manager.read_data(SKILLS_FILE)
    skill_found = False
    updated_skill = None

    # Iteriere durch die Skills, um den zu aktualisierenden zu finden
    for i, skill in enumerate(skills):
        if skill.get('id', '').lower() == id.lower():
            # Aktualisiere den Skill mit den neuen Daten aus dem Request-Body
            skills[i].update(updated_data)
            skills[i]['id'] = id # Stelle sicher, dass die ID durch das Update nicht überschrieben wird
            updated_skill = skills[i]
            skill_found = True
            break # Breche die Schleife ab, sobald der Skill gefunden und aktualisiert wurde

    if skill_found:
        # Wenn der Skill gefunden und aktualisiert wurde, speichere die Daten und gib 200 OK zurück
        data_manager.write_data(SKILLS_FILE, skills)
        return jsonify(updated_skill), 200
    else:
        # Wenn der Skill nicht gefunden wurde, gib 404 Not Found zurück
        return jsonify({"error": "Skill not found."}), 404

@app.route('/skills/<id>', methods=['DELETE'])
def delete_skill(id):
    """
    Löscht einen bestehenden Skill anhand seiner ID.
    """
    skills = data_manager.read_data(SKILLS_FILE)
    initial_length = len(skills) # Speichere die ursprüngliche Länge der Liste

    # Erstelle eine neue Liste, die alle Skills außer dem zu löschenden enthält
    skills = [skill for skill in skills if skill.get('id', '').lower() != id.lower()]

    if len(skills) < initial_length: # Wenn die Länge der Liste abgenommen hat, wurde ein Skill gelöscht
        data_manager.write_data(SKILLS_FILE, skills)
        return '', 204 # 204 No Content
    else:
        # Wenn die Länge nicht abgenommen hat, wurde kein Skill mit der gegebenen ID gefunden
        return jsonify({"error": "Skill not found."}), 404

# --- Start der Initialisierung und Ausführung des Servers ---
if __name__ == '__main__':
    # Dieser Block wird nur ausgeführt, wenn das Skript direkt gestartet wird (nicht importiert)

    # Stelle sicher, dass das 'data'-Verzeichnis existiert
    os.makedirs(DATA_DIR, exist_ok=True)

    # Überprüfe für beide Datendateien (topics.json und skills.json):
    # Wenn die Datei nicht existiert ODER der Versuch, Daten zu lesen, fehlschlägt (z.B. leere/ungültige JSON-Datei),
    # dann schreibe eine leere JSON-Liste in die Datei, um sie zu initialisieren.
    for file_path in [TOPICS_FILE, SKILLS_FILE]:
        if not os.path.exists(file_path) or not data_manager.read_data(file_path):
            data_manager.write_data(file_path, []) # Schreibe eine leere Liste

    # Starte die Flask-Anwendung im Debug-Modus auf Port 5000
    # 'debug=True' ermöglicht automatische Neuladung bei Codeänderungen und detailliertere Fehlermeldungen
    app.run(debug=True, port=5000)