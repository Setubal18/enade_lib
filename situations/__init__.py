from situations.discursive_situation import format_disc_situation
from situations.number_itens import number_itens
from situations.presence_types import presences


def exec(dict):
	format_disc_situation(dict)
	presences(dict)
	number_itens(dict)

	return dict