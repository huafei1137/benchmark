src = 'bv_n10.qasm'
tar = 'test.scaffold'


with open(src, 'r') as f:
   	lines = f.readlines()

with open(tar, 'w') as f:
	for line in lines[2:]:
		line = line.rstrip('\n')
		if line.startswith('h '):
			newline = 'H (' + line[2:-1] + ');\n'
			f.write(newline)
		if line.startswith('cx '):
			newline = 'CNOT (' + line[3:-1] + ');\n'
			f.write(newline)
