from .shifts import shiftsPatterns2004_2010, shiftsPatterns2010_2018


def patternShifts(dict):
	tipos = ['in_matut', 'in_vesper', 'in_noturno']
	if tipos in dict:
		shiftsPatterns2004_2010(dict)

	if 'co_turno_graduacao' in dict:
		shiftsPatterns2010_2018(dict)

	return dict
