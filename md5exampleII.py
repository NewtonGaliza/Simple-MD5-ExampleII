import hashlib

def md5hasher(data):
     md5hash = hashlib.md5()
     md5hash.update(data.encode('utf8'))
     return md5hash.digest()
     
a = input('File:')
with open(a, 'r') as arc:
	m = arc.readline()
	md5hasher(m)

with open(a+'.md5', 'w') as out:
	b = str(md5hasher(m))
	out.write(b)
