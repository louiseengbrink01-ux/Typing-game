# IndaprojektLouiseNellieElsa

## Beskrivning

Detta program är ett monkeytype-inspirerat skrivspel byggt i Python med Pygame. Användaren kan välja språk (svenska eller engelska), tidsgräns (30s, 60s eller 120s) och spelet går ut på att skriva så snabbt och korrekt som möjligt de ord som visas på skärmen. Programmet räknar ut antal korrekt skrivna ord per minut (wpm) och antal misstag.

## Programmets uppbyggnad

Koden är uppdelad i följande filer:

- `main.py` innehåller spelets huvudlogik, till exempel meny, tangenttryckningar, timer, WPM-beräkning och byte mellan olika spellägen.
- `graphics.py` ansvarar för allt som ritas ut på skärmen, som text, knappar, resultat och skrivmarkören.
- `constants.py` innehåller fasta värden, till exempel knapparnas positioner och storlekar.
- `word_handler.py` läser in och blandar orden från textfilerna `words.txt` och `words_sv.txt`.

Programmet använder Pygames huvudloop för att läsa in användarens input, uppdatera spelets tillstånd och rita om skärmen.

## Användning

För att köra programmet måste Python och Pygame vara installerat. Starta spelet genom att köra `python main.py`. I menyn väljer användaren språk och tidsgräns. Klicka sedan på start. När spelet börjar ska användaren skriva orden som visas på skärmen tills tiden gått ut. Rätt bokstäver markeras grönt. Fel bokstäver markeras rött. När tiden är slut visas en resultatsida med WPM och antal fel.

## Användning av AI

Vi använde AI för att hitta fel i koden när saker inte fungerade, och lösa vissa problem med koden. 
