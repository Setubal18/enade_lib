from situations.discursive_situation import format_disc_situation
from utils.change_vars import lowerVars, updatedVars
from utils.covert_to_dict import transformDict
from utils.read_archive import readArchive
from course_patterns.course import patternShifts
from economic_questions.economic_questions import formatQuestions_EconomicPartner
from perception_of_proof.format_Proof_Perception import formatQuestions_proofPerception
from grades.format_grades import format_grades
from situations.presence_types import presences
from vectors.group_vectors import agroup_vectors
from institution_student.agroup import institution, students

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
		patternShifts(dict)
		formatQuestions_EconomicPartner(dict)
		formatQuestions_proofPerception(dict)
		format_grades(dict)
		format_disc_situation(dict)
		presences(dict)
		agroup_vectors(dict)
		institution(dict)
		students(dict)
		print(dict)


execute()
