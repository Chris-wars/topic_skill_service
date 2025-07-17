## Personalized Learning Path Generator - Stage 1, Day 1 (Monday Morning) - Classroom Plan (Detailed & Polyrepo)

**Goal:** Implement the first API endpoint (`GET /topics`) and introduce the development environment and testing with Postman.

**Wichtiger Hinweis an die Schülerinnen und Schüler:** Jeder Schritt ist wichtig! Nehmt euch Zeit, lest die Erklärungen aufmerksam durch und fragt sofort, wenn etwas unklar ist. Wir bauen hier gemeinsam etwas Neues auf, und es ist okay, wenn nicht alles sofort sitzt. Das Wichtigste ist, dass ihr die Konzepte versteht und selbst ausprobiert.

### Epic: PLPG-API-SETUP (Einrichtung der Entwicklungsumgebung)

Dieses Epic befasst sich mit der grundlegenden Einrichtung unserer Arbeitsumgebung. Bevor wir Code schreiben können, müssen wir sicherstellen, dass unsere Werkzeuge bereit sind.

### Ticket: PLPG-API-1

**Titel:** GitHub Repository für den Topic & Skill Service erstellen

**Beschreibung:** Wir werden ein neues GitHub-Repository speziell für unseren ersten Microservice, den `Topic & Skill Service`, erstellen und es auf unsere lokalen Computer herunterladen (klonen). Dies ist der erste Schritt, um die Unabhängigkeit jedes Microservices auch in der Versionskontrolle zu gewährleisten. **Jeder Microservice wird sein eigenes, separates Git-Repository haben.Anforderungen:**

- Ein **GitHub-Konto** muss vorhanden sein. Falls nicht, jetzt schnell eines erstellen!
- **Git** (ein Programm zur Versionskontrolle) muss auf den lokalen Rechnern installiert sein. (In den meisten Entwicklungsumgebungen ist es bereits vorinstalliert). **Akzeptanzkriterien:**
- Ein leeres GitHub-Repository mit dem Namen `topic_skill_service` ist auf GitHub erstellt.
- Das Repository ist erfolgreich auf den lokalen Rechner geklont.
- Eine `.gitignore`Datei ist erstellt, um unnötige Dateien (z.B. virtuelle Umgebungen) von der Versionskontrolle auszuschließen.

**Schritte im Klassenzimmer (Lehrer führt vor, Schüler folgen Schritt für Schritt):**

1. **GitHub Repository erstellen (ca. 10 Minuten):**
   - Öffnet euren Webbrowser und geht zu [github.com](https://github.com/). Loggt euch mit eurem GitHub-Konto ein.
   - Oben rechts auf der Seite seht ihr ein `+` Symbol. Klickt darauf und wählt "New repository" (Neues Repository).
   - Gebt im Feld "Repository name" (Repository-Name) genau `topic_skill_service` ein. Achtet auf die genaue Schreibweise!
   - Wählt unter "Visibility" (Sichtbarkeit) die Option "Private". Das bedeutet, nur ihr und Personen, denen ihr Zugriff gebt, können den Code sehen.
   - Setzt ein Häkchen bei "Add a README file" (Eine README-Datei hinzufügen). Die README ist eine Beschreibung eures Projekts.
   - Setzt ein Häkchen bei "Add .gitignore" (Eine .gitignore-Datei hinzufügen). Wählt aus der Dropdown-Liste `Python` aus. **Was ist `.gitignore`?** Diese Datei teilt Git mit, welche Dateien und Ordner es ignorieren soll. Wir wollen zum Beispiel nicht unsere virtuelle Umgebung (die wir gleich erstellen) oder temporäre Dateien in unser GitHub-Repository hochladen, da diese groß sein können und auf jedem Computer anders sind. Die `Python.gitignore` hat bereits viele typische Python-spezifische Einträge.
   - Klickt abschließend auf den grünen Button "Create repository" (Repository erstellen).
2. **Repository auf den Computer klonen (ca. 10 Minuten):**
   - Nachdem das Repository erstellt wurde, seht ihr eine Seite mit eurem neuen Repository.
   - Klickt auf den grünen Button "Code". Es öffnet sich ein kleines Fenster.
   - Wählt den Tab "HTTPS" und klickt auf das Kopier-Symbol (zwei überlappende Quadrate), um die URL zu kopieren. Diese URL ist die Adresse eures Repositories.
   - Öffnet euer **Terminal** (auf Linux/macOS) oder **Git Bash** (auf Windows). Dies ist ein Textfenster, in dem ihr Befehle eingeben könnt.
   - Navigiert zu dem Ordner auf eurem Computer, in dem ihr eure Projekte speichern möchtet (z.B. `cd ~/Projekte`).
   - Führt nun den Befehl aus, um das Repository zu klonen (ersetzt `<die_kopierte_https_url>` durch die URL, die ihr eben kopiert habt):
     ```
     git clone <die_kopierte_https_url>

     ```
   - Ihr solltet sehen, wie Git das Repository herunterlädt. **Es wird ein neuer Ordner mit dem Namen `topic_skill_service` erstellt.** Dieser Ordner ist nun das Stammverzeichnis eures ersten Microservices.
   - Navigiert *in diesen* neu erstellten Ordner:
     ```
     cd topic_skill_service

     ```
   - **Überprüfung:** Ihr solltet jetzt im Terminal im Pfad enden, der mit `.../topic_skill_service` auf eurem Computer endet. Es gibt kein übergeordnetes `learning_path_backend`Verzeichnis, in das ihr wechseln müsstet.

### Ticket: PLPG-API-2

**Titel:** Python Virtuelle Umgebung einrichten **Beschreibung:** Wir werden eine "virtuelle Umgebung" für unseren `topic_skill_service` erstellen. Stellt euch das wie einen isolierten Container für Python-Projekte vor. Jedes Projekt hat seine eigenen Python-Pakete (Bibliotheken), ohne dass es zu Konflikten mit anderen Projekten auf eurem Computer kommt. Das hält eure Projekte sauber und unabhängig. **Anforderungen:**

- **Python 3** muss auf eurem Computer installiert sein. **Akzeptanzkriterien:**
- Ein neuer Ordner namens `venv` (für "virtual environment") ist im Verzeichnis `topic_skill_service` erstellt.
- Die virtuelle Umgebung ist aktiv, was durch eine Änderung des Terminal-Prompts angezeigt wird.

**Schritte im Klassenzimmer:**

1. **Python-Version überprüfen (ca. 2 Minuten):**
   - Bevor wir die Umgebung erstellen, überprüfen wir, welche Python-Version wir haben.
   - Stellt sicher, dass ihr im Verzeichnis `topic_skill_service` seid.
   - Führt einen der folgenden Befehle aus. Wenn der erste nicht funktioniert, probiert den zweiten:
     ```
     python3 --version
     # Oder:
     python --version

     ```
   - Ihr solltet etwas wie `Python 3.x.x` sehen. Wichtig ist, dass es eine 3.x.x Version ist.
2. **Virtuelle Umgebung erstellen (ca. 3 Minuten):**
   - Stellt sicher, dass ihr im Verzeichnis `topic_skill_service` seid.
   - Führt den Befehl aus, um die virtuelle Umgebung zu erstellen. Der Name `venv` ist eine gängige Konvention:
     ```
     python3 -m venv venv
     # Wenn python3 nicht funktioniert, versucht: python -m venv venv

     ```
   - Dieser Befehl erstellt einen Ordner namens `venv` in eurem aktuellen Verzeichnis. Dieser Ordner enthält eine Kopie des Python-Interpreters und Platz für die Pakete, die wir installieren werden.
3. **Virtuelle Umgebung aktivieren (ca. 2 Minuten):**
   - Nachdem die Umgebung erstellt wurde, müssen wir sie "aktivieren". Das bedeutet, dass euer Terminal nun die Python-Version und die Pakete aus dieser spezifischen `venv`Umgebung verwendet.
   - **Für Linux/macOS:**
     ```
     source venv/bin/activate

     ```
   - **Für Windows (in PowerShell):**
     ```
     .\venv\Scripts\Activate.ps1

     ```
   - **Für Windows (in der klassischen Eingabeaufforderung / Cmd):**
     ```
     venv\Scripts\activate.bat

     ```
   - **Überprüfung:** Euer Terminal-Prompt sollte sich ändern. Ihr solltet nun `(venv)` am Anfang eurer Zeile sehen, z.B.: `(venv) DeinBenutzername@DeinComputer:~/Projekte/topic_skill_service$`. Dies bestätigt, dass die virtuelle Umgebung aktiv ist.

### Ticket: PLPG-API-3

**Titel:** Flask installieren **Beschreibung:** Jetzt, da unsere isolierte Python-Umgebung bereit ist, können wir das Flask-Framework darin installieren. Flask ist eine Python-Bibliothek, die uns dabei hilft, Webanwendungen und APIs zu erstellen. **Anforderungen:**

- Die virtuelle Umgebung muss aktiv sein (ihr solltet `(venv)` im Terminal-Prompt sehen). **Akzeptanzkriterien:**
- Flask ist erfolgreich in der virtuellen Umgebung installiert.

**Schritte im Klassenzimmer:**

1. **Flask installieren (ca. 3 Minuten):**
   - Stellt sicher, dass eure virtuelle Umgebung aktiv ist.
   - Führt den Installationsbefehl aus. `pip` ist der Paketmanager für Python, der Pakete aus dem Python Package Index (PyPI) herunterlädt und installiert:
     ```
     pip install Flask

     ```
   - Ihr solltet eine Reihe von Meldungen sehen, die den Download und die Installation von Flask und seinen Abhängigkeiten anzeigen. Am Ende sollte eine Erfolgsmeldung erscheinen.
2. **Installation überprüfen (Optional, ca. 1 Minute):**
   - Um zu bestätigen, dass Flask installiert ist, könnt ihr diesen Befehl ausführen:
     ```
     pip list

     ```
   - Ihr solltet eine Liste der installierten Pakete sehen, und `Flask` sollte darin aufgeführt sein.

### Epic: PLPG-API-TOPICS (Topics API)

Dieses Epic konzentriert sich auf die Implementierung unseres ersten Microservices, der Informationen über Lern-Topics bereitstellt.

### Ticket: PLPG-API-4

**Titel:** Basis Flask App "Hello World" implementieren **Beschreibung:** Wir erstellen unsere allererste Flask-Anwendung. Sie wird sehr einfach sein: Beim Aufruf einer bestimmten Adresse im Webbrowser gibt sie lediglich einen Text zurück. Dies ist der grundlegende "Hello World"-Test für unsere Webanwendung. **Anforderungen:**

- Flask muss installiert sein. **Akzeptanzkriterien:**
- Eine Datei namens `app.py` ist im Verzeichnis `topic_skill_service` erstellt.
- Die App kann gestartet werden, ohne Fehler im Terminal.
- Beim Aufruf von `http://172.0.0.1:5000/` im Browser wird "Hello from Topic & Skill Service!" angezeigt.

**Schritte im Klassenzimmer:**

1. **`app.py` erstellen (ca. 5 Minuten):**
   - Stellt sicher, dass ihr im Terminal im Verzeichnis `topic_skill_service` seid.
   - Öffnet euren bevorzugten Code-Editor (z.B. VS Code, Sublime Text, PyCharm).
   - Erstellt eine neue Datei namens `app.py` in diesem Verzeichnis.
   - Fügt den folgenden Code ein:
     ```python
     # app.py
     # Dies ist die Hauptdatei unseres Flask-Microservices.

     # Importiere das Flask-Objekt aus dem Flask-Framework.
     # Flask ist die "Magie", die uns hilft, Webanwendungen zu bauen.
     from flask import Flask

     # Erstelle eine Instanz (ein Objekt) unserer Flask-Anwendung.
     # Der Parameter __name__ hilft Flask, den richtigen Pfad für Ressourcen zu finden.
     app = Flask(__name__)

     # Dies ist ein "Decorator". Er teilt Flask mit, welche Funktion ausgeführt werden soll,
     # wenn eine bestimmte URL aufgerufen wird.
     # Hier: Wenn jemand GET-Anfragen an '/' sendet, wird die Funktion 'hello_world' ausgeführt.
     @app.route('/')
     def hello_world():
         # Diese Funktion gibt einfach einen Text zurück.
         # Flask wandelt diesen Text automatisch in eine HTTP-Antwort um.
         return 'Hello from Topic & Skill Service!'

     # Dieser Block stellt sicher, dass der Entwicklungsserver nur gestartet wird,
     # wenn diese Datei direkt ausgeführt wird (nicht, wenn sie als Modul importiert wird).
     if __name__ == '__main__':
         # app.run() startet den Flask-Entwicklungsserver.
         # debug=True: Aktiviert den Debug-Modus. Das bedeutet:
         #   1. Bei Codeänderungen wird der Server automatisch neu gestartet.
         #   2. Detailliertere Fehlermeldungen werden im Browser angezeigt (sehr hilfreich!).
         # port=5000: Legt den Port fest, auf dem der Server läuft.
         # Standardmäßig ist das 5000, also http://127.0.0.1:5000/
         app.run(debug=True, port=5000)

     ```
2. **Flask App starten (ca. 2 Minuten):**
   - Speichert die `app.py`Datei.
   - Geht zurück zu eurem Terminal. Stellt sicher, dass ihr im Verzeichnis `topic_skill_service` seid und eure virtuelle Umgebung aktiv ist (das `(venv)` im Prompt).
   - Führt den Befehl aus, um die Flask-Anwendung zu starten:
     ```
     python app.py

     ```
   - Ihr solltet im Terminal eine Ausgabe sehen, die ähnlich aussieht wie:
     ```
      * Debug mode: on
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
      * Restarting with stat
      * Debugger is active!
      * Debugger PIN: XXX-XXX-XXX

     ```
   - **Wichtig:** Lasst dieses Terminal-Fenster geöffnet und den Server laufen!
3. **Im Browser testen (ca. 1 Minute):**
   - Öffnet euren Webbrowser (Chrome, Firefox, Edge etc.).
   - Gebt in die Adressleiste ein: `http://127.0.0.1:5000/`
   - Drückt Enter.
   - Ihr solltet den Text "Hello from Topic & Skill Service!" sehen. Wenn ja, super gemacht!

### Ticket: PLPG-API-5

**Titel:** Mock-Daten für Topics erstellen **Beschreibung:** Bevor unser API echte Daten aus einer Datenbank holt (das kommt später!), werden wir es so einrichten, dass es Daten aus einer einfachen JSON-Datei liest. Das ist eine gängige Methode, um APIs schnell zu entwickeln und zu testen. Wir erstellen eine Datei mit Beispieldaten für unsere Lern-Topics. **Anforderungen:**

- Ein `data`Unterverzeichnis muss im Service-Verzeichnis existieren. **Akzeptanzkriterien:**
- Eine Datei `data/topics.json` ist im richtigen Verzeichnis erstellt.
- Die Datei enthält gültige JSON-Daten mit mindestens zwei Topic-Objekten.

**Schritte im Klassenzimmer:**

1. **`data` Verzeichnis erstellen (ca. 1 Minute):**
   - Geht in eurem Terminal zurück zum Verzeichnis `topic_skill_service`.
   - Erstellt ein neues Unterverzeichnis namens `data`:
     ```
     mkdir data

     ```
2. **`topics.json` erstellen (ca. 5 Minuten):**
   - Öffnet euren Code-Editor.
   - Erstellt eine neue Datei namens `topics.json` *innerhalb des `data`Verzeichnisses*.
   - Fügt den folgenden JSON-Inhalt ein. **Was ist JSON?** JSON (JavaScript Object Notation) ist ein leichtgewichtiges Datenformat, das Menschen gut lesen und schreiben können und das Maschinen leicht parsen können. Es ist das Standardformat für den Datenaustausch in Web-APIs.
     - `[` und `]` bedeuten eine Liste (oder ein Array).
     - `{` und `}` bedeuten ein Objekt (oder ein Dictionary), das aus Schlüssel-Wert-Paaren besteht.
     - `"id": "t1"` ist ein Schlüssel-Wert-Paar, wobei `"id"` der Schlüssel (immer ein String) und `"t1"` der Wert (hier auch ein String) ist.
     ```json
     [
       {
         "id": "t1",
         "name": "Web Development Fundamentals",
         "description": "Kernkonzepte für die Entwicklung von Webanwendungen, einschließlich HTML, CSS und JavaScript."
       },
       {
         "id": "t2",
         "name": "Frontend Development",
         "description": "Fokus auf die Benutzeroberfläche und Interaktion, wie React, Vue oder Angular."
       },
       {
         "id": "t3",
         "name": "Backend Development",
         "description": "Server-seitige Logik, Datenbanken und APIs, z.B. mit Python Flask oder Node.js Express."
       }
     ]
     ```
   - Speichert die Datei.
   - Navigiert in eurem Terminal zurück zum Hauptverzeichnis des Services:
     ```
     cd ..

     ```
   - **Überprüfung:** Ihr solltet jetzt eine Datei `topics.json` im Ordner `data` haben.

### Ticket: PLPG-API-6

**Titel:** GET /topics Endpunkt implementieren (Initial) **Beschreibung:** Jetzt implementieren wir den Kern unseres ersten API-Endpunkts. Wenn jemand eine `GET`-Anfrage an die Adresse `/topics` sendet, wird unser Flask-Service die Daten aus der `topics.json`-Datei lesen und sie als JSON-Antwort zurücksenden. **Anforderungen:**

- Die Datei `app.py` und der Ordner `data` mit `topics.json` müssen existieren.
- Die Python-Module `Flask`, `json`, `os` und die `jsonify`Funktion müssen in `app.py` importiert sein.**Akzeptanzkriterien:**
- Beim Aufruf von `http://127.0.0.1:5000/topics` wird eine JSON-Liste der Topics zurückgegeben.
- Die Antwort ist korrekt formatiert und enthält die Daten aus `topics.json`.

**Schritte im Klassenzimmer:**

1. **`app.py` aktualisieren (ca. 10 Minuten):**

   - Öffnet eure `app.py`Datei in eurem Code-Editor.
   - Wir müssen einige Zeilen hinzufügen oder ändern:

   ```python
   # app.py
   import json # Dieses Modul hilft uns, mit JSON-Daten zu arbeiten (lesen und schreiben)
   import os   # Dieses Modul hilft uns, mit Dateipfaden zu arbeiten (z.B. um sicherzustellen, dass unser Skript die Daten findet, egal wo es ausgeführt wird)
   from flask import Flask, jsonify # jsonify ist eine spezielle Flask-Funktion, die Python-Listen/Dictionaries automatisch in eine JSON-Antwort umwandelt und den richtigen HTTP-Header setzt.

   app = Flask(__name__)

   # Definieren des Pfades zum 'data'-Verzeichnis relativ zur aktuellen Datei.
   # os.path.dirname(__file__) gibt den Ordner zurück, in dem app.py liegt.
   # os.path.join verbindet Pfadsegmente plattformunabhängig (funktioniert auf Windows, Linux, macOS).
   DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
   TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')

   # Hilfsfunktion zum Lesen einer JSON-Datei
   # Diese Funktion ist robust: Sie prüft, ob die Datei existiert, und fängt Fehler ab.
   def read_json_file(filepath):
       # Überprüfen, ob die Datei unter dem angegebenen Pfad existiert.
       if not os.path.exists(filepath):
           # Wenn die Datei nicht existiert, geben wir eine leere Liste zurück.
           # Das ist wichtig, damit unsere App nicht abstürzt, wenn die Datei z.B. noch nicht erstellt wurde.
           return []
       try:
           # Öffne die Datei im Lesemodus ('r') mit UTF-8-Kodierung (wichtig für Sonderzeichen).
           with open(filepath, 'r', encoding='utf-8') as f:
               # json.load(f) liest den Inhalt der Datei und wandelt ihn von JSON-Text in eine Python-Liste/Dictionary um.
               return json.load(f)
       except json.JSONDecodeError:
           # Dieser Fehler tritt auf, wenn die JSON-Datei syntaktisch ungültig ist (z.B. fehlende Kommas, falsche Klammern).
           print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
           return []
       except Exception as e:
           # Ein allgemeiner Fehlerfang für alle anderen unerwarteten Probleme beim Lesen der Datei.
           print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
           return []

   # Die bestehende Hello World Route
   @app.route('/')
   def hello_world():
       return 'Hello from Topic & Skill Service!'

   # Neue Route für /topics
   # @app.route('/topics', methods=['GET']) bedeutet:
   # Wenn eine HTTP GET-Anfrage an die URL /topics gesendet wird,
   # dann rufe die Funktion 'get_topics' auf.
   @app.route('/topics', methods=['GET'])
   def get_topics():
       # Rufe unsere Hilfsfunktion auf, um die Topics aus der JSON-Datei zu lesen.
       topics = read_json_file(TOPICS_FILE)
       # Verwende jsonify, um die Python-Liste 'topics' in eine standardisierte JSON-Antwort umzuwandeln
       # und diese an den Client (z.B. den Browser oder Postman) zurückzusenden.
       return jsonify(topics)

   if __name__ == '__main__':
       app.run(debug=True, port=5000)

   ```

2. **Flask App neu starten (ca. 1 Minute):**
   - Geht zurück zu eurem Terminal, wo der Flask-Server läuft.
   - Drückt `Ctrl+C` (oder `Strg+C` auf Windows), um den Server zu stoppen.
   - Startet ihn dann erneut mit:
     ```
     python app.py

     ```
   - Da `debug=True` gesetzt ist, würde Flask bei Codeänderungen auch automatisch neu starten. Aber ein manueller Neustart ist eine gute Angewohnheit, um sicherzustellen, dass alle Änderungen übernommen werden.

### Ticket: PLPG-API-7

**Titel:** GET /topics Endpunkt mit Postman testen **Beschreibung:** Jetzt ist der Moment der Wahrheit! Wir werden Postman verwenden, um unseren neu implementierten `/topics`-Endpunkt aufzurufen und zu überprüfen, ob er die korrekten JSON-Daten liefert. Postman ist wie ein "Super-Browser" für APIs, der uns viel mehr Kontrolle über unsere Anfragen gibt als ein normaler Webbrowser. **Anforderungen:**

- Postman muss auf eurem Computer installiert sein.
- Der Flask-Server muss laufen (überprüft das Terminal-Fenster!).
- Der `/topics`Endpunkt muss implementiert sein. **Akzeptanzkriterien:**
- Postman zeigt eine HTTP-Statuscode-Antwort von `200 OK` an.
- Der Antwort-Body enthält die JSON-Daten aus `topics.json`.

**Schritte im Klassenzimmer:**

1. **Postman öffnen (ca. 1 Minute):**
   - Startet die Postman-Anwendung auf eurem Computer.
2. **Neue Anfrage erstellen (ca. 1 Minute):**
   - In Postman seht ihr wahrscheinlich einen großen `+` Button (New Tab) oder einen "New" Button in der Seitenleiste. Klickt darauf und wählt "HTTP Request". Es öffnet sich ein neuer Tab für eure Anfrage.
3. **Anfrage konfigurieren (ca. 2 Minuten):**
   - **Methode wählen:** Links neben dem URL-Eingabefeld seht ihr ein Dropdown-Menü, das standardmäßig auf `GET` eingestellt sein sollte. Lasst es auf `GET`, da wir einen GET-Endpunkt testen.
   - **URL eingeben:** Im großen URL-Eingabefeld (wo "Enter request URL" steht) gebt die vollständige Adresse eures Endpunkts ein:
     ```
     http://127.0.0.1:5000/topics

     ```
   - **Keine weiteren Einstellungen:** Für diesen einfachen GET-Request sind keine weiteren Einstellungen (wie Header oder Body) erforderlich.
4. **Anfrage senden und Ergebnis prüfen (ca. 3 Minuten):**
   - Klickt auf den blauen "Send"-Button rechts neben dem URL-Feld.
   - **Überprüft den Statuscode:** Unterhalb des URL-Feldes seht ihr den "Status". Er sollte `200 OK` (oder nur `200`) anzeigen. **Was bedeutet das?** `200 OK` ist ein HTTP-Statuscode, der bedeutet, dass die Anfrage erfolgreich war und der Server die angeforderten Daten zurückgegeben hat.
   - **Überprüft den Antwort-Body:** Im unteren Bereich von Postman seht ihr verschiedene Tabs. Klickt auf den Tab "Body" und wählt dann "Pretty" (für eine schön formatierte Ansicht). Ihr solltet nun die JSON-Liste eurer Topics sehen, genau wie in eurer `topics.json`Datei.

**Herzlichen Glückwunsch!** Ihr habt erfolgreich euren ersten Microservice-Endpunkt implementiert und mit einem professionellen Tool getestet! Das ist ein riesiger Meilenstein in eurem Projekt und zeigt, dass euer Backend funktioniert.
