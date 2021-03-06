from .shifts import shiftsPatterns2004_2010, shiftsPatterns2015_2018
from utils.new_atributes import new_atributes

def patternShifts(dict):
	new_atributes(dict,'varCursoTurnos')
	condition = True if 'in_matut' in dict and \
	                      'in_vesper' in dict and \
	                      'in_noturno' in dict else False
	if condition:
		dict = shiftsPatterns2004_2010(dict)

	elif 'co_turno_graduacao' in dict:
		dict = shiftsPatterns2015_2018(dict)

	return dict
