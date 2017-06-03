favourite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name,language in sorted(favourite_languages.items()):
	print(name.title() +
		"'s favorite languages is " +
		language.title() +
		'.')

print('\n')

for name,language in favourite_languages.items():
	print(name.title() +
		"'s favorite languages is " +
		language.title() +
		'.')
