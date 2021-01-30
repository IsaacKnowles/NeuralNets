import random

class player:
	'''
	Players have preferences and value. They send signals that are at worst uninformative.
	Players cannot "lie" about who they are, but they can make it harder to tell.
	We develop the best picture of them that we can, understanding that our model
	will be imperfect and subject 

	Player prefs for different products is represnted by a 
	dictionary of products (keys) pointing to the relative weight
	the players places on that product (values). 

	Player value is exactly that: A measure of how much value the players has and which
	we are trying to tap into. As we're defining a player here, we make no assumption
	about the correlation between value and preferences.  But a 
	message generator might make that assumption and model a bandit accordingly...
	'''
	type_freqs = {}
	num_players = 0
	def __init__(self, player_prefs, player_value):
		self.prefs= player_prefs  
		self.value = player_value
		self.player_signal = player_signal
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

	def get_signal(self):
		'''
		A signal is just a noisy version of player prefs.
		'''
		

	def get_type_probability(self,player_type):
		self.update_types()
		return(self.types[player_type])

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

	



