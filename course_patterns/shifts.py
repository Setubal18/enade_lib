def shiftsPatterns2004_2010(dict):
	try:
		if int(dict['in_matut']) == 1:
			dict["varCursoTurnos"].update({'varCursoMatutino': True})
			del dict['in_matut']
		else:
			dict["varCursoTurnos"].update({'varCursoMatutino': False})
			del dict['in_matut']

		if int(dict['in_vesper']) == 1:
			dict["varCursoTurnos"].update({'varCursoVespertino': True})
			del dict['in_vesper']
		else:
			dict["varCursoTurnos"].update({'varCursoVespertino': False})
			del dict['in_vesper']

		if int(dict['in_noturno']) == 1:
			dict["varCursoTurnos"].update({'varCursoNoturno': True})
			del dict['in_noturno']
		else:
			dict["varCursoTurnos"].update({'varCursoNoturno': False})
			del dict['in_noturno']

	except ValueError:
		dict["varCursoTurnos"].update({'faltandoTurno': True})
		del dict['in_noturno']
		del dict['in_vesper']
		del dict['in_matut']

	return dict


def shiftsPatterns2015_2018(dict):
	try:
		if int(dict['co_turno_graduacao']) == 1:
			dict["varCursoTurnos"].update({'varCursoMatutino': True})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 2:
			dict["varCursoTurnos"].update({'varCursoVespertino': True})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 3:
			dict["varCursoTurnos"].update({'varCursoIntegral': True})
			del dict['co_turno_graduacao']
		elif int(dict['co_turno_graduacao']) == 4:
			dict["varCursoTurnos"].update({'varCursoNoturno': True})
			del dict['co_turno_graduacao']
	except ValueError:
		dict["varCursoTurnos"].update({'faltandoTurno': True})
	return dict
