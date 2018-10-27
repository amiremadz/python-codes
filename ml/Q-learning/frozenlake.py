import numpy as np
import gym
import random
import time

# moves: left, right, up, down
# states:
## S: safe
## F: frozen
## H: hole - game over
## G: goal - game over
# environment:
## SFFF
## FHFH
## FFFH
## HFFG

env = gym.make("FrozenLake-v0")

# Q-table
state_space_size  = env.observation_space.n  # number of rows: size of state space in environment
action_space_size = env.action_space.n       # number of cols: size of action space
print(state_space_size, action_space_size)

q_table = np.zeros((state_space_size, action_space_size))

print("\n********Q-table********")
print(q_table)

# Initializing Q-learning parameters
num_episodes          = 10000
max_steps_per_episode = 100

learning_rate = 0.1   # alpha
discount_rate = 0.99  # gamma

# epsilon-greedy policy
exploration_rate       = 1 # epsilon
max_exploration_rate   = 1
min_exploration_rate   = 0.01
exploration_decay_rate = 0.001

rewards_all_episodes = []

# Q-learning algorithm
for episode in range(num_episodes):
    # initialize new episode params
    state = env.reset()
    done = False
    rewards_current_episode = 0

    if episode % 1000 == 0:
        print("episode: ", episode)

    for step in range(max_steps_per_episode):
        # exploration-explotation trade-off
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            # choose action via explotation
            # i.e. chosse action with highest Q-value for currrent state
            action = np.argmax(q_table[state, :])
        else:
            # choose action via exploration
            # i.e. sample action randomly
            action = env.action_space.sample()
        #print("action: ", action)    

        # take new action
        new_state, reward, done, info = env.step(action) 
        #print("info: ", info)

        # update Q-table for Q(s, a)
        q_table[state, action] = (1 - learning_rate) * q_table[state, action] + learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))

        # transition to new state
        state = new_state

        # add new reward
        rewards_current_episode += reward

        if done:
            break

    # exploration rate decay
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)

    # add current episode reward to total rewards list
    rewards_all_episodes.append(rewards_current_episode)

# calculate and print average reward per thousand episodes
num = 1000
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes / num)

count = num
print("\n*********Average reward per thousand episodes**********")
for rewards in rewards_per_thousand_episodes:
    print(count, ": ", str(sum(rewards / num)))
    count += num

print("\n********Updated Q-table*********")
print(q_table)
