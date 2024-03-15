# https://gymnasium.farama.org/environments/toy_text/frozen_lake/
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
"""
Action Space
0: move left
1: move down
2: move right
3: move up
"""

"""
Instructions
play 1000 games
plot % of wins grouped over 10 games
"""

env = gym.make('FrozenLake-v1', map_name='4x4', is_slippery=False)
observation, info = env.reset()
win_percent = []
scores = []
for i in range(1000):
    done = False
    score = 0
    truncated = False
    print(i)
    while not done:
        action = env.action_space.sample()
#        print(f'action : {action}')
        observation, reward, done, truncated, info = env.step(action)
        score += reward
        print(f'observation : {observation}')
    scores.append(score)
    if i % 10 == 0:
        avg = np.mean(scores[-10:])
        win_percent.append(avg)
plt.plot(win_percent)
plt.show()
env.close()

# as expected, the agent always fails

