from utils.format_dict import format_dict


def institution(dict):
	format_dict(dict, 'instituicao', 'co_ies',
	            'co_categad',
	            'co_orgacad',
	            'co_group',
	            'co_curso',
	            'co_modalidade',
	            'co_munic_curso',
	            'co_uf_curso',
	            'co_regiao_curso')


def students(dict):
	format_dict(dict,'estudante',
	            'nu_idade',
	            'tp_sexp',
	            'ano_fim_em',
	            'ano_grad',
	            'varCursoTurnos',
	            'tp_inscricao_adm',
	            'tp_inscricao'
	            )