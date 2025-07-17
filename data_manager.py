import json
import os

class JsonDataManager:
    """
    Verwaltet das Lesen und Schreiben von JSON-Daten aus Dateien.
    """

    def __init__(self):
        pass
      
        

    def read_data(self, filepath):

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



    def write_data(self, filepath, data):

        os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Stellt sicher, dass das Verzeichnis existiert
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist beim Schreiben in '{filepath}' aufgetreten: {e}")
            return False
