import re

from utils.new_atributes import new_atributes
import re


def formatQuestions_EconomicPartner(dict):
	new_atributes(dict, 'socioEconomico_Questionario')
	index = 1
	for keys in list(dict.keys()):
		x = re.search('qe_i\d+', keys)
		if (x):
			chave = x.string
			if index < 10:
				dict['socioEconomico_Questionario'].update(
					{'qe_i' + '0' + str(index): dict[chave]}
				)
				del dict[keys]
			else:
				dict['socioEconomico_Questionario'].update(
					{'qe_i' + str(index): dict[chave]})
				del dict[keys]
			index += 1
	return dict
