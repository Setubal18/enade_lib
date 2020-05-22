def generateCode(arrayMaps):
	for index in range(len(arrayMaps)):
		dict = arrayMaps[index]
		dict['index'] = dict.get('nu_ano') + str(index)
	return arrayMaps
