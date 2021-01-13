import random

class player:
	type_freqs = {}
	num_players = 0
	def __init__(self, player_types, player_value):
		self.types = player_types
		self.value = player_value
		player.num_players += 1
		for t in self.types:
			if t in player.type_freqs and self.types[t] > 0:
				player.type_freqs[t] += 1
			else:
				player.type_freqs[t] = 1
		self.update_types()

	def update_types(self):
		type_diff =  set(player.type_freqs.keys()).difference(set(self.types.keys()))
		for td in type_diff:
			self.types[td] = 0

	def get_type_probability(self,player_type):
		self.update_types()
		return(types[player_type])

	def get_remaining_value(self):
		return(self.value)

	def decrement_value(self,decrement):
		self.value = self.value if decrement > self.value else self.value - decrement

	def __str__(self):
		self.update_types()
		#print('test')
		return("Value: " + str(self.value) + " Type probabilities: " + str(self.types))


if __name__ == "__main__":
	#player_1 = player({'a':0.25,'b':0.75},2)
	#player_2 = player({'b':0.9,'c':0.1},1)
	#print("Hellow")
	#player_1.decrement_value(1)
	#player_2.decrement_value(3)
	#print(player_1)
	#print(player_2)
	players = []
	types = ['a','b','c','d','e','f','g','h']
	for i in range(10000):
		t = types
		random.shuffle(t)
		#print(t)
		player_type1 = t.pop(1)
		player_type2 = t.pop(1)
		value = random.random()
		player_type1_prob = random.random()
		players.append(player({player_type1:player_type1_prob,player_type2:1-player_type1_prob},value))
		t.append(player_type1)
		t.append(player_type2)
	#for p in players:
		#print(p)
	print(player.num_players)
	print(player.type_freqs)

	



