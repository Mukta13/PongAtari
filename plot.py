import matplotlib.pyplot as plt
import pickle
import numpy as np


#with (open("all_rewards_file.pkl", "rb")) as openfile1:
data1 = pickle.load(open('losses_file.pkl', 'rb'))
frames1, losses = zip(*data1)
print(losses)
plt.scatter(frames1, losses)
plt.xlabel('# of frames')
plt.ylabel('losses')
plt.show()


#with (open("all_rewards_file.pkl", "rb")) as openfile2:
   # data2 = pickle.load(openfile2)
