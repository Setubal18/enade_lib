from utils.format_dict import find_attribute_and_update


def number_itens(dict):
	find_attribute_and_update(dict, '(nu_item)\w+', 'num_itens')
	return dict
