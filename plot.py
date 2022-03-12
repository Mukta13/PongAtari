import matplotlib.pyplot as plt
import pickle
import numpy as np

#losses= pickle.load(open("losses_file.pkl", "rb"))
with (open("losses_file.pkl", "rb")) as openfile:
    data1 = pickle.load(openfile)
frames, losses = zip(*data1)
plt.scatter(frames, losses)
plt.xlabel('# of frames')
plt.ylabel('losses')
plt.show()
plt.savefig('losses.png')
#rewards = zip(pickle.load(open("all_rewards_file.pkl", "rb")))
with (open("all_rewards_file.pkl", "rb")) as openfile:
    data2 = pickle.load(openfile)
frames, rewards = zip(*data2)
plt.scatter(frames, rewards)
plt.xlabel('# of frames')
plt.ylabel('rewards')
plt.show()
plt.savefig('rewards.png')
