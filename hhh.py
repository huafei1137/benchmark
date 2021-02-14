import os
files=os.listdir('./')
for src in files:
	if "qasm" not in src:
		continue
	tar = src.replace(".qasm",'.scaffold')
	with open(src, 'r') as f:
   		lines = f.readlines()

	with open(tar, 'w') as f:
		newnewline = '#include <math.h>\n'
		f.write(newnewline)
		newnewline = 'int main(){\n'
		f.write(newnewline)
		for line in lines[1:]:
			line = line.rstrip('\n')
			if line.startswith('qreg '):
				newline = 'qbit ' + line[5:-1] + ';\n'
				f.write(newline)
			if line.startswith('h '):
				newline = 'H (' + line[2:-1] + ');\n'
				f.write(newline)
			if line.startswith('cx '):
				newline = 'CNOT (' + line[3:-1] + ');\n'
				f.write(newline)
		f.write('}\n')
#src = 'bv_n10.qasm'
#tar = 'test.scaffold'


