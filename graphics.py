import pygame

from constants import button_english, button_swedish, button_30s, button_60s, button_120s, button_start
from constants import button_back
from constants import button_menu, button_again

# Draws the typing text and colors each letter depending on its state:
# grey = not typed yet, green = correct, red = wrong.
def draw_text(screen, letters, errors, letter_index, font, x, y):
    for i, letter in enumerate(letters):
        if i >= letter_index:
            color = (150, 150, 150)
        elif errors[i]:
            color = (200, 50, 50)
        else :
            color = (150, 220, 150)
        
        surface = font.render(letter, True, color)
        screen.blit(surface, (x, y))
        x += font.size(letter)[0]

# Draws the main menu buttons.
# The selected language/time button is highlighted.
def draw_menu(screen, font, language, time_limit):

    for rect, label, active in [ (button_english, "english", language == "english"),
                                (button_swedish, "swedish", language == "swedish"),
                                (button_30s, "30s", time_limit == 30),
                                (button_60s, "60s", time_limit == 60),
                                (button_120s, "120s", time_limit == 120),
                                (button_start, "start", False)
                                ]:
        color = (80, 180, 80) if active else (60, 60, 60)
        pygame.draw.rect(screen, color, rect, border_radius=6)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# Draws the result screen after the test is finished.
def draw_results(screen, font, error_points, wpm):
    
    for rect, label in [ (button_menu, "main menu"),
                        (button_again, "try again")
                        ]:
        color = (60, 60, 60)
        pygame.draw.rect(screen, color, rect, border_radius = 6)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    error_surface = font.render(f"Errors: {error_points}", True, (255, 255, 255))
    wpm_surface = font.render(f"Words per minute: {wpm: .0f}", True, (255, 255, 255))

    screen.blit(error_surface, (300, 300))
    screen.blit(wpm_surface, (250, 25))


# Draws a button that can be used to return to the menu.
def draw_back(screen, font):
    color = (60, 60, 60)
    pygame.draw.rect(screen, color, button_back, border_radius=6)
    text = font.render("< back to menu", True, (255, 255, 255))
    screen.blit(text, (button_back.centerx - text.get_width() // 2, button_back.centery - text.get_height() // 2))

# Draws two lines of text at a time.
# visible_line decides which line is shown at the top.
def draw_lines(screen, lines, errors, letter_index, font, x, y, visible_line):
    y_spacing = 35

    for line_number in range (visible_line, min(visible_line + 2, len(lines))):
        line = lines[line_number]

        draw_x = x
        draw_y = y + (line_number - visible_line) * y_spacing

        line_start_index = sum(len(previous_line) for previous_line in lines[:line_number])

        for i, letter in enumerate(line):
            global_index = line_start_index + i

            if global_index >= letter_index:
                color = (150, 150, 150)
            elif errors[global_index]:
                color = (200, 50, 50)
            else:
                color = (150, 220, 150)

            surface = font.render(letter, True, color)
            screen.blit(surface, (draw_x, draw_y))
            draw_x += font.size(letter)[0]

    # Draws a cursor line at the current typing position.
    cursor_index = letter_index

    for line_number in range(visible_line, min(visible_line + 2, len(lines))):
        line_start_index = sum(len(previous_line) for previous_line in lines[:line_number])
        line_end_index = line_start_index + len(lines[line_number])

        if line_start_index <= cursor_index <= line_end_index:
            cursor_x = x + font.size(lines[line_number][:cursor_index - line_start_index])[0]
            cursor_y = y + (line_number - visible_line) * y_spacing

            pygame.draw.line(
                screen,
                (255, 255, 255),
                (cursor_x, cursor_y),
                (cursor_x, cursor_y + font.get_height()),
                2
            )









    
