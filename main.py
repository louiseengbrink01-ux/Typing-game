import pygame

pygame.init()

clock = pygame.time.Clock()

from word_handler import load_words, get_lines, get_char_offset

from graphics import draw_text, draw_results, draw_lines, draw_menu
from constants import button_english, button_swedish, button_30s, button_60s, button_120s, button_start
from constants import button_menu, button_again

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.font.init()
font = pygame.font.SysFont("monospace", 20)

def make_lines(words, words_per_line):
    lines = []

    for i in range(0, len(words), words_per_line):
        line = " ".join(words[i:i + words_per_line]) + " "
        lines.append(line)

    return lines

language = "english"
words_list = load_words(language)

current_line_index = 0 
words_per_line = 8
visible_line = 0

line1, line2 = get_lines(words_list, current_line_index, words_per_line)

def reset_game():
    global letter_index, current_line_index
    global errors, error_points, wpm, start_time, words_typed
    global text, words_list, letters, lines, visible_line

    # words = load_words(language)
    # text = build_text(words)
    # letters = list(text)
    errors = [False] * len(letters)

    visible_line = 0
    letter_index = 0
    error_points = 0
    wpm = 0
    words_typed = 0
    current_line_index = 0
    start_time = None

language = "english"
time_limit = 60
TEXT_TEST = ""
game_state = "menu"
letters = []
letter_index = 0 
# print(letters)

lines = []
wpm = 0
error_points = 0
errors = []

start_time = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if game_state == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_english.collidepoint(event.pos):
                    language = "english"

                elif button_swedish.collidepoint(event.pos):
                    language = "swedish"
                
                elif button_30s.collidepoint(event.pos):
                    time_limit = 30

                elif button_60s.collidepoint(event.pos):
                    time_limit = 60

                elif button_120s.collidepoint(event.pos):
                    time_limit = 120
            
                elif button_start.collidepoint(event.pos):
                    words_list = load_words(language)
                    lines = make_lines(words_list, words_per_line)
                    text = "".join(lines)
                    letters = list(text)
                    errors = [False] * len(letters)
                    letter_index = 0
                    error_points = 0
                    wpm = 0
                    visible_line = 0
                    game_state = "game"
                    start_time = pygame.time.get_ticks()
        
        
        elif game_state == "game":

            # Detecting key presses:
            # Check if a key has been pressed down -> Move forward in list.
            # Simultaneously check if the right key pressed -> If not: mark as error.

            if event.type == pygame.KEYDOWN:

                # Allowing backspace:
                # If you press it the index goes down one step.
                # And any potential error is undone.
                # Not allowed if you're at the first letter obvi.

                if event.key == pygame.K_BACKSPACE:
                    if letter_index > 0:
                        letter_index -= 1
                        errors[letter_index] = False

                        line_start_index = sum(len(line) for line in lines[:visible_line])

                        if letter_index < line_start_index and visible_line > 0:
                          visible_line -= 1

                elif letter_index < len(letters):

                    expected_letter = letters[letter_index]
                    typed_letter = event.unicode

                    if expected_letter != typed_letter:
                        errors[letter_index] = True
                        
                    letter_index += 1
                    line_end_index = sum(len(line) for line in lines[:visible_line + 1])

                    if letter_index >= line_end_index and visible_line < len(lines) - 2:
                       visible_line += 1
        
        elif game_state == "results":
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_menu.collidepoint(event.pos):
                    reset_game()
                    game_state = "menu"

                elif button_again.collidepoint(event.pos):
                     reset_game()
                     words_list = load_words(language)
                     lines = make_lines(words_list, words_per_line)
                     text = "".join(lines)
                     letters = list(text)
                     errors = [False] * len(letters)
  
                     letter_index = 0
                     visible_line = 0
                     error_points = 0
                     wpm = 0
  
                     game_state = "game"
                     start_time = pygame.time.get_ticks()
          

    # Gives the error count as number.
    error_points = sum(errors) 

    screen.fill((30, 30, 30))

    if game_state == "menu":
        draw_menu(screen, font, language, time_limit)

    elif game_state == "game":
       
        draw_lines(screen, lines, errors, letter_index, font, 100, 280, visible_line)

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        time_left = max(0, time_limit - elapsed_time)

        timer_surface = font.render(f"Time {int(time_left)}s ", True, (255, 255, 255))
        screen.blit(timer_surface, (10,10))

        correct_letters = sum(1 for i in range(letter_index) if not errors[i])

        words_typed = correct_letters / 5
        elapsed_minutes = elapsed_time / 60

        if elapsed_minutes > 0:
            wpm = words_typed / elapsed_minutes
        else:
            wpm = 0
        
        wpm_surface = font.render(f"Words per minute: {int(wpm)}", True, (255, 255, 255))
        wpm_width = wpm_surface.get_width()
        wpm_x = SCREEN_WIDTH - wpm_width - 10  
        wpm_y = 10

        screen.blit(wpm_surface, (wpm_x, wpm_y))

        if time_left <= 0:
            game_state = "results"

        # Or draw_lines

    elif game_state == "results":
         draw_results(screen, font, error_points, wpm)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

