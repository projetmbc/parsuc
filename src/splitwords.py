from pathlib import Path

from spellchecker import SpellChecker
import re

spell = SpellChecker(language='fr')

text = """
Voici un exemple ping-pong de texte avec des mots et des formules mathématiques.
`E` = mc^2 est une formule célèbre. Le mot 'celebre' est mal orthographié.
Un autre exemple est a^2 + b^2 = c^2. Fin du texte avec erreur de 'ortografe'.
"""

NOT_WORD_LIKE_PATTERN = re.compile(r'[^àéèa-zA-Z-]')

def isword(word):
    return not bool(NOT_WORD_LIKE_PATTERN.search(word))

def correct_word(word):
    corrected_word = spell.candidates(word)
    return corrected_word


new_text = []

PUNCTUATIONS = "'\",;.:'"

for p in PUNCTUATIONS:
    text = text.replace(p, f" {p} ")

for line in text.split('\n'):
    new_line = []

    if line.strip():
        for word in line.split(' '):
            if word.strip():
                if not isword(word):
                    word = f"`{word}`"

                else:
                    corrected_words = correct_word(word)

                    print(word, corrected_words)
                    # exit()

                    word = f"[[{'|'.join(corrected_words)}]]"

            new_line.append(word)

    new_text.append(' '.join(new_line))

new_text = '\n'.join(new_text)

for p in PUNCTUATIONS:
    new_text = new_text.replace(f" {p} ", p)

new_text = new_text.replace("` `", " ")

print(new_text)
