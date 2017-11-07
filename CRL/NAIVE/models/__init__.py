from linear import NaiveLinearCQN
from linear_large import NaiveLinearLargeCQN

def get_new_model(name, state_size, action_size, reward_size):
	if name == 'linear':
		return NaiveLinearCQN(state_size, action_size, reward_size)
	if name == 'linear_large':
		return NaiveLinearLargeCQN(state_size, action_size, reward_size)
	else:
		print "model %s doesn't exist."%(name)
		return None