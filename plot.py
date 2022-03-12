import matplotlib.pyplot as plt
import pickle
import numpy as np


#with (open("losses_file.pkl", "rb")) as openfile1:
data1 = pickle.load(open('losses_file.pkl', 'rb'))
frames1, losses = zip(*data1)

plt.scatter(frames1, losses)
plt.xlabel('# of frames')
plt.ylabel('losses')
plt.show()
plt.savefig('losses1.png')

#with (open("all_rewards_file.pkl", "rb")) as openfile2:
   # data2 = pickle.load(openfile2)
data2 = pickle.load(open('all_rewards_file.pkl', 'rb'))
frames2, rewards = zip(*data2)
plt.scatter(frames2, rewards)
plt.xlabel('# of frames')
plt.ylabel('rewards')
plt.show()
plt.savefig('rewards1.png')
