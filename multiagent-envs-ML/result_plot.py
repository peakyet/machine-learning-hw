import numpy as np
import matplotlib.pyplot as plt

# ma_reward = np.loadtxt("./saved_models/ma_reward_20230517-150629.txt")
# reward = np.loadtxt("./saved_models/reward_20230517-150629.txt")
#ma_reward = np.loadtxt("./saved_models/SpaceInvaders/ma_reward_20230519-101302.txt")
#reward = np.loadtxt("./saved_models/SpaceInvaders/reward_20230519-101302.txt")

reward = np.loadtxt("ppo/saved_models/SpaceInvaders/save_PPO_model/img2obs_train/ma_reward_20230607-103436.txt")

#plt.plot(ma_reward, label="ma_reward")
plt.plot(reward, label = "reward")
plt.legend()
plt.grid()
plt.show()