from utils.globals import re
from utils.format_dict import format_dict, find_attribute_and_update
from utils.new_atributes import new_atributes


def grades_ce_discursive_indiv(dict):
	return find_attribute_and_update(dict, 'nt_ce_d\d+', 'notas_ce_d_indi')


def grades_ce_geral(dict):
	return find_attribute_and_update(dict, '((nt_\w+ce)|(nt_ce_\w+))', 'notas_ce')


def grades_fg(dict):
	return find_attribute_and_update(dict, '((nt_\w+fg)|(nt_fg_\w+))', 'notas_fgs')


def format_grades(dict):
	grades_ce_discursive_indiv(dict)
	grades_ce_geral(dict)
	grades_fg(dict)
	format_dict(dict, 'notas', 'nt_ger', 'notas_fgs', 'notas_ce', 'notas_ce_d_indi')
	return dict
