import re

def version_2004_2010(versao_2004_2010, i, dict):
	dict['percepcao_prova'].update(
		{' co_rs_i' + str(i): dict[versao_2004_2010]}
	)
	return dict


def version_2011Plus(versao_2011plus, dict):
	dict['percepcao_prova'].update(
		{versao_2011plus: dict[versao_2011plus]}
	)
	return dict


def quantity_questions(dict):
	for keys in list(dict.keys()):
		nu_que_qip = re.search('nu_que_qip', keys)
		if nu_que_qip:
			dict['percepcao_prova'].update(
				{nu_que_qip.string: dict[nu_que_qip.string]}
			)
		else:
			leng = len(dict['percepcao_prova'])
			dict['percepcao_prova'].update(
				{
					'nu_que_qip': str(leng)
				}
			)
		return dict