#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def most_frequent_chars(filename: str) -> str:
    return by_freq(apro_file(filename))

def apro_file(filename):
    next_file = filename
    words = []
    while not words or filename != next_file:
        with open (next_file, encoding='utf8') as file:
            next_file=file.readline().strip()
            words.extend(file.read().split())
        if next_file==filename:
            break
    return words

def by_freq(words):
    
    freq = {}
    for word in words:
        for position, letter in enumerate(word):
            freq[position] = freq.get(position, {})
            freq[position][letter] = freq[position].get(letter, 0) + 1
    result = []
    for position in freq:
        result.append(min(freq[position].items(), 
            key=lambda x: (-x[1], x[0]))[0])
    return "".join(result)






