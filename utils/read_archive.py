import csv


def readArchive(rota):
	data = []
	try:
		if rota.endswith('.csv'):
			with open(rota, 'r', newline='') as file:
				read = csv.reader(file)
				for row in read:
					data.append(row)
			file.close()
			keys = data[0]
			data.pop(0)
			return keys, data

		elif rota.endswith('.txt'):
			with open(rota, 'r', newline='') as file:
				read = csv.reader(file, delimiter=';')
				for row in read:
					data.append(row)
			file.close()
			keys = data[0]
			data.pop(0)
			return keys, data
	except:
		print('Formato invalido')
