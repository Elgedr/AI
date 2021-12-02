import gym as gym
env = gym.make('CartPole-v0')

for i_episode in range(200):
    observation = env.reset()
    for t in range(200):
        env.render()

        # random action - replace this with picking the action from the q-table using the epsilon greedy policy
        action = env.action_space.sample()

        next_observation, reward, done, info = env.step(action)
        if done:
            reward = -reward   # simulation ended before step 200, penalty

        # train the Q-table here
        #  Q[s,a] += alpha * (r + gamma * Q[s',a'] - Q[s,a])
        #  s: observation
        #  a: action
        #  r: reward
        #  s': next_observation
        #  a': best action in state s',
        #      you will have to find the highest value in Q-table

        observation = next_observation
        if done:
            print("Episode {} finished after {} timesteps".format(i_episode, t+1))
            break
env.close()