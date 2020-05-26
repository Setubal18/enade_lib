def shiftsPatterns2004_2010(dict):
	try:
		if int(dict['in_matut']) == 1:
			dict["varCursoTurnos"].update({'varCursoMatutino': 1})
			del dict['in_matut']
		else:
			dict["varCursoTurnos"].update({'varCursoMatutino': 0})
			del dict['in_matut']

		if int(dict['in_vesper']) == 1:
			dict["varCursoTurnos"].update({'varCursoVespertino': 2})
			del dict['in_vesper']
		else:
			dict["varCursoTurnos"].update({'varCursoVespertino': 0})
			del dict['in_vesper']

		if int(dict['in_noturno']) == 1:
			dict["varCursoTurnos"].update({'varCursoNoturno': 4})
			del dict['in_noturno']
		else:
			dict["varCursoTurnos"].update({'varCursoNoturno': 0})
			del dict['in_noturno']

	except ValueError:
		dict["varCursoTurnos"].update({'faltandoTurno': 0})
		del dict['in_noturno']
		del dict['in_vesper']
		del dict['in_matut']

	return dict


def shiftsPatterns2015_2018(dict):
	try:
		if int(dict['co_turno_graduacao']) == 1:
			dict["varCursoTurnos"].update({'varCursoMatutino': 1})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 2:
			dict["varCursoTurnos"].update({'varCursoVespertino': 2})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 3:
			dict["varCursoTurnos"].update({'varCursoIntegral': 3})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 4:
			dict["varCursoTurnos"].update({'varCursoNoturno': 4})
			del dict['co_turno_graduacao']
	except ValueError:
		dict["varCursoTurnos"].update({'faltandoTurno': 0})
	return dict
