from utils.globals import re
from utils.format_dict import format_dict
from utils.new_atributes import new_atributes


def grades_ce_discursive_indiv(dict):
	dict['notas_ce_d_indi'] = {}
	for keys in list(dict.keys()):
		nt_ce = re.search('nt_ce_d\d+', keys)
		if nt_ce:
			nt_ce = nt_ce.string
			dict['notas_ce_d_indi'].update(
				{keys: dict[nt_ce]}
			)
			del dict[keys]

	return format_dict(dict, 'notas_ce_d_indi', 'notas')


def grades_ce_geral(dict):
	dict['notas_ce'] = {}
	for keys in list(dict.keys()):
		nt_ce = re.search('((nt_\w+ce)|(nt_ce_\w+))', keys)
		if nt_ce:
			nt_ce = nt_ce.string
			dict['notas_ce'].update(
				{keys: dict[nt_ce]}
			)
			del dict[keys]
	return format_dict(dict, 'notas_ce', 'notas')


def grades_fg(dict):
	dict['notas_fgs'] = {}
	for keys in list(dict.keys()):
		nt_fg = re.search('((nt_\w+fg)|(nt_fg_\w+))', keys)
		if nt_fg:
			nt_fg = nt_fg.string
			dict['notas_fgs'].update(
				{keys: dict[nt_fg]}
			)
			del dict[keys]
	return format_dict(dict, 'notas_fgs', 'notas')


def format_grades(dict):
	new_atributes(dict,'notas')
	grades_ce_discursive_indiv(dict)
	grades_ce_geral(dict)
	grades_fg(dict)
	format_dict(dict, 'nt_ger', 'notas')
	return dict
