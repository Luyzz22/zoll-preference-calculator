# 🎯 Präferenzkalkulations-Tool für Zollabwicklung

Automatisiertes Python-Tool zur Berechnung des EU-Präferenzursprungs gemäß Zollrecht.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 📸 Screenshot

*Beispiel-Output mit farbcodierten Ergebnissen (grün = präferenzberechtigt, rot = nicht präferenzberechtigt)*

## 🚀 Quick Start
```bash
# Packages installieren
pip3 install -r requirements.txt

# Beispiel-Input erstellen
python3 create_input.py

# Tool ausführen
python3 preferences.py

# Ergebnis öffnen
open Output.xlsx
# Präferenzkalkulations-Tool für Zollabwicklung

Automatisiertes Python-Tool zur Berechnung des EU-Präferenzursprungs gemäß Zollrecht.

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
