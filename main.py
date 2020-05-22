from utils.change_vars import lowerVars, updatedVars
from utils.covert_to_dict import transformDict
from utils.read_archive import readArchive
from utils.new_atributes import new_atributes
from course_patterns.course import patternShifts
from economic_questions.economic_questions import formatQuestions_EconomicPartner

path = 'Dados/2017exp.txt'


def execute():
	keys, data = readArchive(path)
	keys = lowerVars(keys)
	keys = updatedVars(keys)
	enadeData = transformDict(keys, data)
	print(enadeData)

	for dict in enadeData:
		dict = new_atributes(dict)
		dict = patternShifts(dict)
		dict = formatQuestions_EconomicPartner(dict)
		print(dict)


execute()
