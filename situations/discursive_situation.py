from utils.globals import re
from utils.new_atributes import new_atributes
from utils.format_dict import format_dict


def format_disc_situation(dict):
	new_atributes(dict, 'tp_sce')
	new_atributes(dict, 'tp_sfg')
	for keys in list(dict.keys()):
		tp_sce_d = re.search('tp_sce_d\d+', keys)
		tp_sfg_d = re.search('tp_sfg_d\d+', keys)
		if tp_sce_d:
			dict = tp_sce(dict, tp_sce_d.string)
			del dict[keys]
		elif tp_sfg_d:
			dict = tp_sfg(dict, tp_sfg_d.string)
			del dict[keys]

	return format_dict(dict, 'sitacao_questionario_discursivo', 'tp_sce', 'tp_sfg')


def tp_sce(dict, tp_sce):
	dict['tp_sce'].update(
		{tp_sce: dict[tp_sce]}
	)
	return dict


def tp_sfg(dict, tp_sfg):
	dict['tp_sfg'].update(
		{tp_sfg: dict[tp_sfg]}
	)
	return dict
