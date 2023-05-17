#!/usr/bin/env python3
def character_frequency(filename):
    try:
        characters = {}
        with open(filename) as f:
            for line in f:
                for char in line:
                    characters[char] = characters.get(char, 0) + 1
        return characters
    except OSError:
        return None
