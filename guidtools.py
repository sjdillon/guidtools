#!python
#==========================================================#
# guidtools.py 
# helper functions to convert guids between oracle and sql/windows
# tests
# print oguid_o2ss("1B35E504BC0C174DA8226AB6BBEB0408")
# print guid_mover("04E5351B-0CBC-4D17-A822-6AB6BBEB0408")
# print guid("1B35E504BC0C174DA8226AB6BBEB0408")
# print guid("04E5351B-0CBC-4D17-A822-6AB6BBEB0408")
# print test_guid_conversion("04E5351B-0CBC-4D17-A822-6AB6BBEB0408")
#==========================================================#
def substr(instring, offset, length):
	"""substring function - mimics oracle SUBSTR"""
	sliced = instring[offset-1:offset-1+length]
	return sliced

def oguid_o2ss(oguid):
	"""convert oracle guid to windows"""
	result = substr(oguid, 7, 2) + substr(oguid, 5, 2) + \
		substr(oguid, 3, 2) + substr(oguid, 1, 2) + '-' + \
		substr(oguid, 11, 2) + substr(oguid, 9, 2) + '-' + \
		substr(oguid, 15, 2) + substr(oguid, 13, 2) + '-' + \
		substr(oguid, 17, 4) + '-' + substr(oguid, 21, 12) 
	return result	

def guid_mover(guid):
	"""convert windows guid to oracle """
	result = substr(guid, 7,2)+substr(guid, 5,2)+substr(guid, 3,2)+\
		substr(guid, 1,2)+substr(guid,12,2)+substr(guid,10,2)+\
		substr(guid,17,2)+substr(guid,15,2)+substr(guid,20,4)+\
		substr(guid,25,12) 
	return result

def guid(inguid):
	"""flips a guid from to the other format"""
	if "-" in inguid:
		result=guid_mover(inguid)
	else:
		result=oguid_o2ss(inguid)
	return result	

def test_guid_conversion(guid):
	"""test: convert a guid from windows to oracle and back"""
	new_oguid= guid_mover(guid) 	
	back_to_old=oguid_o2ss(new_oguid)
	if guid == back_to_old:
		return True
	else:
		return False
		
