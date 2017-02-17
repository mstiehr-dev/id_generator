import string
import random

def id_generator(size=40):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def pcid_generator():
	parts = []
	parts.append(id_generator(8))
	parts.append(id_generator(4))
	parts.append(id_generator(4))
	parts.append(id_generator(4))
	parts.append(id_generator(12))
	parts.append(id_generator(8))
	parts.append("EBJ")
	
	return '-'.join(parts)
	
	

if __name__ == '__main__':
	print(pcid_generator())
