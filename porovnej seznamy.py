lines1:("Jablko je červené", "Banán je žlutý", "Hruška je zelená", "Meruňka je oranžová", "Třešeň je červená",)
Lines2:("Jablko je červené", "Banán je žlutý", "Hruška je modrá", "Meruňka je oranžová", "Třešeň je fialová",)

# Otevřeme oba soubory
with open('soubor1.txt', 'r', encoding='utf-8') as file1, open('soubor2.txt', 'r', encoding='utf-8') as file2:
    # Načteme řádky z obou souborů
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Porovnáme řádky
for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
    if line1.strip() != line2.strip():
        print(f"Neshoda na řádku {i}:")
        print(f"Soubor 1: {line1.strip()}")
        print(f"Soubor 2: {line2.strip()}")

# Pokud jeden soubor má více řádků než druhý
if len(lines1) > len(lines2):
    print("\nSoubor 1 obsahuje další řádky:")
    for line in lines1[len(lines2):]:
        print(line.strip())
elif len(lines2) > len(lines1):
    print("\nSoubor 2 obsahuje další řádky:")
    for line in lines2[len(lines1):]:
        print(line.strip())
