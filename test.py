def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += digit_letters[digit_value]
		abs_value //= base

	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result += "-"
	return result[::-1]

if __name__ == "__main__":
    print(format_base(7, 2, "0123456789ABCDEF"))