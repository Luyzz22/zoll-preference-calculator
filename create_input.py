"""
Hilfsskript: Erstellt eine Beispiel-Input.xlsx für Tests
"""

import pandas as pd

# Beispieldaten erstellen
daten = {
    'Warennummer': [
        '8708.29.10',
        '8708.29.10', 
        '8708.29.10',
        '8708.29.10',
        '8708.29.10'
    ],
    'Lieferland': [
        'Deutschland',
        'China',
        'Polen',
        'Frankreich',
        'USA'
    ],
    'Materialkosten_Gesamt': [
        1000,
        1500,
        800,
        1200,
        2000
    ],
    'EU_Anteil': [
        700,   # 70% -> JA
        600,   # 40% -> NEIN
        500,   # 62.5% -> JA
        900,   # 75% -> JA
        400    # 20% -> NEIN
    ]
}

# DataFrame erstellen
df = pd.DataFrame(daten)

# Als Excel speichern
dateiname = "Input.xlsx"
df.to_excel(dateiname, index=False)

print(f"✅ {dateiname} erfolgreich erstellt!")
print(f"   5 Testzeilen mit verschiedenen Szenarien")
print(f"\nStarte nun das Hauptprogramm mit:")
print(f"   python3 preferences.py")