
class foo:
	pass

class pokemon:
	'this class has informatin about pokemons'

	def __init__(self,pokemon_name,pokemon_cp,pokemon_type):
		self.pokemon_name = pokemon_name
		self.pokemon_cp = pokemon_cp
		self.pokemon_type = pokemon_type
		self.__foo='private variable'

	def display_informatin(self):
		print self.__foo
		print " the pokemon name is %s \n the pokemon cp is %d \n the pokemon type is %s "%(self.pokemon_name,self.pokemon_cp,self.pokemon_type)

	def foo(self):
		return 44




if __name__ == '__main__':
	pikachu = pokemon('pikachu',100,'electricity')
	print pikachu.pokemon_name
	pikachu.display_informatin()
	print pikachu.__doc__
	print dir(pikachu)
	print dir(pokemon)




