from utils.format_dict import find_attribute_and_update, format_dict


def format_disc_situation(dict):
	dict = find_attribute_and_update(dict, 'tp_sce_d\d+', 'tp_sce')
	dict = find_attribute_and_update(dict, 'tp_sfg_d\d+', 'tp_sfg')
	return format_dict(dict, 'sitacao_questionario_discursivo', 'tp_sce', 'tp_sfg')