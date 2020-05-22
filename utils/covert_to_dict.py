def transformDict(keys, data):
	arrayMap = []
	for array in (data):
		map = {}
		for values in range(len(array)):
			map[keys[values]] = array[values]
		arrayMap.append(map)
	return arrayMap