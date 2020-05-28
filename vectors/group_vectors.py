from utils.format_dict import find_attribute_and_update


def agroup_vectors(dict):
	return find_attribute_and_update(dict, '(ds_vt_)|(vt_)\w+', 'vetores')
