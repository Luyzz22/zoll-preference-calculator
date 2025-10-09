markdown# 🎯 Präferenzkalkulations-Tool für Zollabwicklung

Automatisiertes Python-Tool zur Berechnung des EU-Präferenzursprungs gemäß Zollrecht.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 📸 Beispiel-Output

Farbcodierte Excel-Datei:
- ✅ **Grüne Zeilen** = Präferenzberechtigt (≥50% EU-Anteil)
- ❌ **Rote Zeilen** = Nicht präferenzberechtigt (<50% EU-Anteil)

## ✨ Features

- ✅ Automatische Berechnung des EU-Anteils in Prozent
- ✅ Bestimmung der Präferenzberechtigung (≥50% EU-Anteil = JA)
- ✅ Farbcodierung: Grüne Zeilen (präferenzberechtigt), Rote Zeilen (nicht präferenzberechtigt)
- ✅ Fehlerbehandlung und benutzerfreundliche Ausgaben
- ✅ DSGVO-konform (lokale Verarbeitung, keine Cloud)

## 📋 Voraussetzungen

- Python 3.8 oder höher
- macOS, Windows oder Linux

## 🚀 Installation (Mac)

### Schritt 1: Python prüfen

Öffne Terminal und prüfe, ob Python installiert ist:
```bash
python3 --version
Falls nicht installiert:
bash# Homebrew installieren (falls noch nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python installieren
brew install python3
Schritt 2: Repository herunterladen
bash# Repository klonen
git clone https://github.com/luisschenk/zoll-preference-calculator.git
cd zoll-preference-calculator

# Oder ZIP herunterladen und entpacken
Schritt 3: Abhängigkeiten installieren
bashpip3 install -r requirements.txt
Schritt 4: Beispiel-Input erstellen (optional)
bashpython3 create_input.py
Dies erstellt eine Input.xlsx mit 5 Testzeilen.
📖 Verwendung
Input-Datei vorbereiten
Erstelle eine Excel-Datei Input.xlsx mit folgenden Spalten:
WarennummerLieferlandMaterialkosten_GesamtEU_Anteil8708.29.10Deutschland10007008708.29.10China1500600............
Spalten-Erklärung:

Warennummer: Zolltarifnummer (z.B. HS-Code)
Lieferland: Ursprungsland der Ware
Materialkosten_Gesamt: Gesamte Materialkosten in EUR
EU_Anteil: Kosten der EU-Materialien in EUR

Script ausführen
bashpython3 preferences.py
Output-Datei
Das Tool erstellt Output.xlsx mit zusätzlichen Spalten:

EU_Anteil_Prozent: Berechneter EU-Anteil in %
Präferenzursprung: JA oder NEIN
Status: Beschreibung (Präferenzberechtigt / Nicht präferenzberechtigt)

Formatierung:

✅ Grüne Zeilen = Präferenzberechtigt (≥50% EU-Anteil)
❌ Rote Zeilen = Nicht präferenzberechtigt (<50% EU-Anteil)

🔍 Beispiel
Input:
Warennummer  | Lieferland  | Materialkosten_Gesamt | EU_Anteil
8708.29.10   | Deutschland | 1000                 | 700
8708.29.10   | China       | 1500                 | 600
8708.29.10   | Polen       | 800                  | 500
Output:
Warennummer  | Lieferland  | Materialkosten_Gesamt | EU_Anteil | EU_Anteil_Prozent | Präferenzursprung | Status
8708.29.10   | Deutschland | 1000                 | 700       | 70.0%            | JA               | Präferenzberechtigt
8708.29.10   | China       | 1500                 | 600       | 40.0%            | NEIN             | Nicht präferenzberechtigt
8708.29.10   | Polen       | 800                  | 500       | 62.5%            | JA               | Präferenzberechtigt
🛠️ Technische Details
Verwendete Libraries:

pandas: Excel-Verarbeitung und Datenanalyse
openpyxl: Excel-Formatierung (Farben)

Berechnung:
pythonEU_Anteil_Prozent = (EU_Anteil / Materialkosten_Gesamt) × 100
Präferenzursprung = "JA" wenn EU_Anteil_Prozent ≥ 50%, sonst "NEIN"
🔐 Datenschutz & Compliance

✅ 100% lokal: Alle Daten bleiben auf Ihrem Computer
✅ Keine Cloud: Kein Upload zu externen Servern
✅ DSGVO-konform: Keine personenbezogenen Daten verarbeitet
✅ Open Source: Code ist vollständig einsehbar

🛠️ Troubleshooting
"ModuleNotFoundError: No module named 'pandas'"
bashpip3 install pandas openpyxl
"FileNotFoundError: Input.xlsx not found"
Stelle sicher, dass Input.xlsx im selben Ordner wie preferences.py liegt.
Farben werden nicht angezeigt
Manche Excel-Versionen zeigen Formatierungen erst nach erneutem Öffnen der Datei. Alternativ: Mit LibreOffice oder Numbers öffnen.
Fehler bei Python 3.13+
Falls pandas==2.1.0 nicht installiert werden kann:
bashpip3 install pandas openpyxl
# (installiert automatisch kompatible Versionen)
📊 Anwendungsfälle
Dieses Tool eignet sich für:

Exporteure/Importeure: Schnelle Prüfung der Präferenzberechtigung
Zolldienstleister: Massenverarbeitung von Präferenzkalkulationen
Compliance-Abteilungen: Automatisierte Ursprungsprüfung
Steuerberater/Wirtschaftsprüfer: Unterstützung bei Mandantenberatung

📄 Rechtlicher Hinweis
Dieses Tool dient der Effizienzsteigerung bei Präferenzkalkulationen. Die Ergebnisse sind ohne Gewähr und ersetzen keine rechtliche Beratung durch einen Zollberater oder die Zollverwaltung. Für verbindliche Auskünfte wenden Sie sich bitte an die zuständige Zollbehörde.
🔄 Roadmap
Geplante Features (v2.0):

 Web-Interface für einfachere Bedienung
 Unterstützung für mehrere Freihandelsabkommen (EPA, CETA, etc.)
 Automatischer Import aus SAP
 PDF-Report-Generierung
 API-Schnittstelle

🤝 Beitragen
Feedback und Verbesserungsvorschläge sind willkommen! Kontaktieren Sie mich gerne unter Luis@schenk.com
👤 Autor
Luis Schenk
Wirtschaftsjurist | Customs & Trade Compliance Specialist
📧 Luis@schenk.com
📍 Weinheim, Rhein-Neckar-Region, Deutschland
💼 Verfügbar: 15-20h/Woche (Werkstudent), ab 2025 Vollzeit
🎯 Services

KI-gestützte Zoll-Automatisierung: Präferenzkalkulationen, Lieferantenerklärungen, Sanktionslistenscreening
Mehrsprachige Legal-Tech: Vertragsübersetzungen und Dokumentenanalyse (DE/EN/ES/FR/IT)
SAP/Excel-Integration: Python-basierte Workflow-Automatisierung
Custom-GPT-Entwicklung: KI-Assistenten für Compliance und Zollabwicklung

💼 Berufserfahrung

Vibracoustic SE: Werkstudent Customs & Foreign Trade
AHK London: Praktikum Tax Department
Roche, Daimler: Logistik & Produktion

🔗 Portfolio

Custom GPT: Zoll-Assistent
Custom GPT: Legal Translator
Freelance.de Profil

📄 Lizenz
MIT License - Dieses Tool ist für kommerzielle und private Nutzung frei verwendbar.
Version: 1.0.0
Letzte Aktualisierung: Oktober 2025
GitHub: https://github.com/luisschenk/zoll-preference-calculator
