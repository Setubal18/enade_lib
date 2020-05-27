import re


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


def find_attribute_and_update(dict, regex, name):
	for keys in list(dict.keys()):
		found = re.search(regex, keys)
		if found:
			dict = format_dict(dict, name, found.string)
	return dict
