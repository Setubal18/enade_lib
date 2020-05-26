def format_dict(dict, father_name, *sons_names, ):
	try:
		for key in list(dict.keys()):
			if key in sons_names:
				dict[father_name].update({
					key: dict[key]
				})
				del dict[key]
		return dict
	except KeyError:
		dict[father_name] = {}
		for key in list(dict.keys()):
			if key in list(sons_names):
				dict[father_name].update({
					key: dict[key]
				})
				del dict[key]
		return dict