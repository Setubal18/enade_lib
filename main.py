from database.save import create_many
from utils.read_archive import readArchive
from utils.format_dict import format_dict, format_array_dict
from course_patterns.course import patternShifts
from economic_questions.economic_questions import formatQuestions_EconomicPartner
from perception_of_proof.format_Proof_Perception import formatQuestions_proofPerception
from grades.format_grades import format_grades
from vectors.group_vectors import agroup_vectors
from institution_student.agroup import institution, students
import situations
import database


def execute():
	path = input('caminho:', )
	keys, data = readArchive(path)
	enadeData = format_array_dict(keys, data)

	for dict in enadeData:
		format_dict(dict, 'tempo', 'nu_ano')
		patternShifts(dict)
		formatQuestions_EconomicPartner(dict)
		formatQuestions_proofPerception(dict)
		format_grades(dict)
		situations.exec(dict)
		agroup_vectors(dict)
		institution(dict)
		students(dict)
	database.save(enadeData)



i = 'y'
while i.lower() == 'y':
	execute()
	print('Deseja salvar outro arquivo?(y = sim n = não)')
	i = input('(y/n) = ')
