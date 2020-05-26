from utils.change_vars import lowerVars, updatedVars
from utils.covert_to_dict import transformDict
from utils.read_archive import readArchive
from utils.new_atributes import new_atributes
from course_patterns.course import patternShifts
from economic_questions.economic_questions import formatQuestions_EconomicPartner
from perception_of_proof.format_Proof_Perception import formatQuestions_proofPerception
from grades.format_grades import format_grades
path = 'Dados/2018exp.txt'
#2004exp.csv
#2013exp.txt
#2018exp.txt
#2011exp.txt

def execute():
	keys, data = readArchive(path)
	keys = lowerVars(keys)
	keys = updatedVars(keys)
	enadeData = transformDict(keys, data)

	for dict in enadeData:
		print('before',dict)
		patternShifts(dict)
		formatQuestions_EconomicPartner(dict)
		formatQuestions_proofPerception(dict)
		format_grades(dict)
		print(dict)


execute()
