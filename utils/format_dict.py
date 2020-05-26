def format_dict(dict,son_name,father_name):
	for key in list(dict.keys()):
		if key == son_name:
			dict[father_name].update({
				key:dict[son_name]
			})
			del dict[key]

	return dict