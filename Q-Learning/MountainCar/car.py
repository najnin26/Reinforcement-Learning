import gymnasium as gym

env = gym.make("MountainCar-v0", render_mode='human')
state = env.reset()

# print(env.observation_space.high)
# print(env.observation_space.low)

done = False
while not done:
    action = 2
    new_state, reward, done, truncated,info = env.step(action)
    env.render()
    
env.close()