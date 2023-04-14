def func1() : 
	global a
	a = 10
	print("punc1()에서 a의 값 ", a)

def func2() :
	print("punc2()에서 a의 값 ", a)

a = 20

func1()
func2()