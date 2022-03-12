import matplotlib.pyplot as plt
import pickle
import numpy

frames = pickle.load("frames.pkl")
losses= pickle.load("losses_file.pkl")
plt.scatter(frames, losses)
plt.xlabel('# of frames')
plt.ylabel('losses')
plt.show()
plt.savefig('losses.png')
rewards = pickle.load("all_rewards_file.pkl")
plt.sactter(frames, rewards)
plt.xlabel('# of frames')
plt.ylabel('rewards')
plt.show()
plt.savefig('rewards.png')
