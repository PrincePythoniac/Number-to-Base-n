'''
program to convert decimal to bases
'''
while True:
	x = int(input('Enter Number :'))
	n = x
	y = int(input('Enter Base :'))
	m = str(y)
	z = []
	while x != 0:
		q = x % y
		z.append(q)
		z.reverse()
		x = x // y
	Z = str(z)
	p = ''
	for i in z:
		i = str(i)
		p += i
	s= m.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')
	
	print('------------------------')
	print(f'The Base {y} representation of {n} is ({p}){m.translate(s)}')
	print('------------------------')


