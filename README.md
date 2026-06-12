# Monkeytype-Inspired Typing Game

A first-year group project developed at KTH Royal Institute of Technology using Python and Pygame.

## Description

This program is a Monkeytype-inspired typing game built in Python with Pygame. The user can choose between Swedish and English, select a time limit of 30, 60, or 120 seconds, and practice typing words as quickly and accurately as possible. The program calculates the number of correctly typed words per minute (WPM) and the number of mistakes.

## Project Structure

The code is divided into the following files:

- `main.py` contains the main game logic, including the menu, keyboard input, timer, WPM calculation, and switching between different game states.
- `graphics.py` handles everything drawn on the screen, such as text, buttons, results, and the typing cursor.
- `constants.py` contains fixed values, such as button positions and sizes.
- `word_handler.py` reads and shuffles words from the text files `words.txt` and `words_sv.txt`.

The program uses Pygame’s main loop to handle user input, update the game state, and redraw the screen.

## How to Run

Python and Pygame must be installed to run the program.

Run the game with:

```bash
python main.py
```

In the menu, the user selects a language and a time limit, then clicks start. When the game begins, the user types the words shown on the screen until the time runs out. Correct letters are highlighted in green, and incorrect letters are highlighted in red. When the time is over, a result screen displays the user’s WPM and number of mistakes.

## Use of AI

AI was used as a support tool for debugging and solving coding problems when parts of the program did not work as expected.

---

# Svensk version

## Beskrivning

Detta program är ett Monkeytype-inspirerat skrivspel byggt i Python med Pygame. Användaren kan välja språk (svenska eller engelska), tidsgräns (30s, 60s eller 120s) och spelet går ut på att skriva så snabbt och korrekt som möjligt de ord som visas på skärmen. Programmet räknar ut antal korrekt skrivna ord per minut (WPM) och antal misstag.

## Programmets uppbyggnad

Koden är uppdelad i följande filer:

- `main.py` innehåller spelets huvudlogik, till exempel meny, tangenttryckningar, timer, WPM-beräkning och byte mellan olika spellägen.
- `graphics.py` ansvarar för allt som ritas ut på skärmen, som text, knappar, resultat och skrivmarkören.
- `constants.py` innehåller fasta värden, till exempel knapparnas positioner och storlekar.
- `word_handler.py` läser in och blandar orden från textfilerna `words.txt` och `words_sv.txt`.

Programmet använder Pygames huvudloop för att läsa in användarens input, uppdatera spelets tillstånd och rita om skärmen.

## Användning

För att köra programmet måste Python och Pygame vara installerat.

Starta spelet genom att köra:

```bash
python main.py
```

I menyn väljer användaren språk och tidsgräns. Klicka sedan på start. När spelet börjar ska användaren skriva orden som visas på skärmen tills tiden gått ut. Rätt bokstäver markeras grönt och fel bokstäver markeras rött. När tiden är slut visas en resultatsida med WPM och antal fel.

## Användning av AI

AI användes som stöd för felsökning och för att lösa kodproblem när delar av programmet inte fungerade som förväntat.
