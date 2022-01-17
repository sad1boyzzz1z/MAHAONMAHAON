def phhhysics():
	a = input("Введите начальную скорость")
	if (type(a)!='int') or (a == 0):
		print('НЕПРАВИЛЬНО')
	b  = input("Введите конечную скорость") 
	if (type(b)!='int') or (b == 0):
		print('НЕПРАВИЛЬНО')
	c  = input("Введите времвяя") 
	if (type(c)!='int') or (c == 0):
		print('НЕПРАВИЛЬНО')
	uskorenie = b-c
	uskoritog = uskorenie/c
	return uskoritog
def decorator(phhhysics):
	def rasstoyanie(uskoritog):
		phhhysics()
		RASSTOYANIEE = (b-a)/(2*uskoritog)
	return rasstoyanie
phhhysics = decorator(phhhysics())
phhhysics()
input("sjjdjdjdjdjd")