from database.save import create_one, create_many


def save(dados):
	choose = input('Deseja cadastrar varios de uma vez? (y/n) :')
	if choose.lower() == 'n':
		create_one(dados)
	elif choose.lower() == 'y':
		create_many(dados)
