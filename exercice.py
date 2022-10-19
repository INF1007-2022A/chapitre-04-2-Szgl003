#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):

 name = name.split("-")[0]

 nom_maj = name[0].upper() + name[1:].lower()

 return "Bonjour, " + nom_maj

def get_random_sentence(animals, adjectives, fruits):

 phrase = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."
 words = []

 for word_set in (animals, adjectives, fruits):
	 words += [word_set[random.randrange(0,len(word_set))]]


 return phrase % tuple(words)

def encrypt(text, shift):
	result = ""
	for letter in text:
		encrypted_letter = letter
		if letter.isalpha():
			index = ord(letter.upper()) - ord("A")
			encrypted_index = (index + shift) % 26
			encrypted_letter = chr(ord("A") + encrypted_index)
		result += encrypted_letter
	return result


def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
