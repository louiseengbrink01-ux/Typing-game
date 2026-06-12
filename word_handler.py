import random

def load_words(language):
    filename = "words_sv.txt" if language == "swedish" else "words.txt"
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
    
    random.shuffle(words)
    return words

def get_lines(words, current_line_index, words_per_line):
    line_start = current_line_index * words_per_line
    line1 = words[line_start : line_start + words_per_line]
    line2 = words[line_start + words_per_line : line_start + words_per_line * 2]
    return line1, line2

def get_char_offset(words, current_line_index, words_per_line):
    line_start_word = current_line_index * words_per_line
    chars_before = len(" ".join(words[: line_start_word]))
    if line_start_word > 0:
        chars_before += 1
    return chars_before