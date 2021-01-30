import random
import player
import sys

class bandit:
	random_msg_prob = 0.0
	def __init__(self,init_type_weights):
		self.msg_type_weights = init_type_weights

	def get_message(self):
		'''Roll a a random variable and return a type from the appropriate interval'''
		if random.random() < bandit.random_msg_prob:
			#print('random msg')
			return(random.choice(list(self.msg_type_weights.keys())))
		msg_probs = self.get_weights_to_probs()
		#print(msg_probs)
		roll = random.random()
		for t in msg_probs.keys():
			if msg_probs[t][0] < roll and msg_probs[t][1] >= roll:
				return(t)
		return(t)

	def get_weights_to_probs(self):
		weight_total = sum(self.msg_type_weights.values())
		msg_type_probs = {}
		p_min = 0
		for t in self.msg_type_weights.keys():
			msg_type_probs[t] = (p_min,self.msg_type_weights[t]/weight_total + p_min)
			p_min += self.msg_type_weights[t]/weight_total
		return(msg_type_probs)

	def adjust_type_weight(self,t,value = 1,up=True):
		#print(self.msg_type_weights)
		#print(t)
		if up:
			self.msg_type_weights[t] += value
		else:
			self.msg_type_weights[t] -= value
		return(None)

	def adjust_random_msg_prob(self,fraction):
		if fraction < 0: 
			print("Message probability can't go below zero")
			return(None)
		elif fraction * bandit.random_msg_prob >= 1:
			print("Message probability can't go above or beyond 1")
			return(None)
		bandit.random_msg_prob = fraction*bandit.random_msg_prob

def main():
	players = []
	type_values = {'a':4,'b':1,'c':18,'d':98}
	types = {'a':(0,0.2),'b':(0.2,0.7),'c':(0.7,0.99),'d':(0.99,1)} #,'e'] #,'f','g','h']
	msg_weights = {'a':50000,'b':50000,'c':50000,'d':50000}
	myBandit = bandit(msg_weights)
	for i in range(10000):  # Generate 10,000 players according to types distribution
		type_p = random.random()
		for t in types.keys():
			if types[t][0] < type_p and types[t][1] >= type_p:
				break
		player_type1 = t #.pop(1)
		#player_type2 = t.pop(1)
		value = random.random()
		#player_type1_prob = random.random()
		players.append(player.player({player_type1:1},type_values[player_type1]))
		#players.append(player.player({player_type1:player_type1_prob,player_type2:1-player_type1_prob},value))
		#t.append(player_type1)
		#t.append(player_type2)
	i = 0
	serves = {}  # Times a message of type m is served
	clicks = {}  # Times a message appears to induce a click
	for t in msg_weights.keys():
		serves[t] =0
		clicks[t] = 0
	#print(player.player.type_freqs)
	while True:
		p = random.choice(players) # A player steps up
		m = myBandit.get_message() # A message is chosen for the player
		#print(m)
		#print(clicks)
		serves[m] += 1
		if p.get_type_probability(m) > 0: # Does the player click?
		 	clicks[m] += 1
		 	myBandit.adjust_type_weight(m,p.get_remaining_value())  
		else: 
			myBandit.adjust_type_weight(m,p.get_remaining_value(),False)
		i+=1
		#print(p)
		#print(m)
		#print(myBandit.msg_type_weights)
		if i % 100000 == 0:
			print(serves)
			#print(clicks)
			#print(myBandit.msg_type_weights)
			#print(type_values)
			for t in msg_weights.keys():
				serves[t] =0
				clicks[t] = 0
		if i % 300000 == 0:
			print(type_values)
			print(myBandit.msg_type_weights)
			#sys.exit()
			
			print("Clicks: " + str(clicks))


if __name__ == "__main__":
	main()
	







