class Base:
	first_name = "Gopish"
	_last_name = "Monga"
	__nick_name = "Gopu"

base = Base()
print("{} {} {}".format(base.first_name,base._last_name,base._Base__nick_name))