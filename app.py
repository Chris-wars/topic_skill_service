import json # Importiert das JSON-Modul für die Arbeit mit JSON-Daten
import os # Importiert das OS-Modul für die Interaktion mit dem Betriebssystem, z.B. Dateipfade

from flask import Flask, jsonify # Importiert Flask-Klasse zum Erstellen der Webanwendung und jsonify zum Konvertieren von Python-Objekten in JSON-Antworten

app = Flask(__name__) # Initialisiert die Flask-Anwendung. __name__ hilft Flask, den Stammordner für die App zu finden.

# Definiert den Pfad zum Datenverzeichnis relativ zum aktuellen Skript
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
# Definiert den vollständigen Pfad zur topics.json-Datei im Datenverzeichnis
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')


@app.route('/') # Definiert eine Route für die Startseite ('/')
def hello_world():
    # Gibt eine einfache Begrüßungsnachricht zurück, wenn die Startseite aufgerufen wird
    return 'Hello from Topic and Skill Service!'


def read_json_file(filepath):
    """
    Liest eine JSON-Datei vom angegebenen Dateipfad.
    Gibt den Inhalt der JSON-Datei als Python-Liste oder -Dictionary zurück.
    Gibt eine leere Liste zurück, wenn die Datei nicht existiert oder ein Fehler auftritt.
    """
    if not os.path.exists(filepath):
        # Prüft, ob die Datei existiert
        print(f"Datei nicht gefunden: {filepath}") # Gibt eine Meldung aus, wenn die Datei nicht existiert
        return [] # Gibt eine leere Liste zurück
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # Öffnet die Datei im Lesemodus mit UTF-8-Kodierung
            return json.load(file) # Lädt den JSON-Inhalt und gibt ihn zurück
    except json.JSONDecodeError:
        # Fängt Fehler ab, die beim Dekodieren von JSON auftreten können (z.B. ungültige JSON-Syntax)
        print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
        return [] # Gibt eine leere Liste im Fehlerfall zurück
    except Exception as e:
        # Fängt alle anderen unerwarteten Fehler ab
        print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
        return [] # Gibt eine leere Liste im Fehlerfall zurück


@app.route('/topics', methods=['GET']) # Definiert eine Route für '/topics', die nur GET-Anfragen akzeptiert
def get_topics():
    """
    Endpunkt zum Abrufen aller Themen aus der topics.json-Datei.
    Gibt eine JSON-Antwort mit der Liste der Themen zurück.
    """
    topics = read_json_file(TOPICS_FILE) # Ruft die Themen aus der JSON-Datei ab
    return jsonify(topics) # Konvertiert die Themenliste in eine JSON-Antwort und gibt sie zurück

if __name__ == '__main__':
    # Dieser Block wird nur ausgeführt, wenn das Skript direkt gestartet wird (nicht importiert)
    app.run(debug=True, port=5000) # Startet den Flask-Entwicklungsserver
    # debug=True ermöglicht den Debug-Modus (automatische Neuladung bei Codeänderungen und detaillierte Fehlermeldungen)
    # port=5000 legt den Port fest, auf dem der Server lauscht
