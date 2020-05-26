from perception_of_proof.add_atributes import version_2004_2010, version_2011Plus, quantity_questions
from utils.globals import re
from utils.new_atributes import new_atributes

def formatQuestions_proofPerception(dict):
	index = 1
	new_atributes(dict,'percepcao_prova')
	for keys in list(dict.keys()):
		versao_2004_2010 = re.search('qp_i\d+', keys)
		versao_2011plus = re.search('co_rs_i\d+', keys)

		if versao_2004_2010:
			dict = version_2004_2010(versao_2004_2010.string, index, dict)
			del dict[keys]
			index += 1

		elif versao_2011plus:
			version_2011Plus(versao_2011plus.string, dict)
			del dict[keys]
			index += 1

	quantity_questions(dict)
	return dict



