from utils.format_dict import find_attribute_and_update


def presences(dict):
	return find_attribute_and_update(dict,'tp_pr?\w+','atributos_presencas')
