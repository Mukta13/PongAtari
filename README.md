# PongAtari
In this program, the AI is learning to play the Pong Atari game. Trained a model to learn to play Pong without human knowledge of the game. Used the OpenAI gym to run and interact with the Pong Atari game and the deep Q-learning algorithm.The model uses its Q network to decide what moves to take when playing the game. This network will instead push each decision it made to an experience buffer. This replay buffer will be polled from to make updates to the Q network using the loss function. The network is contained within dqn.py. The environment will keep playing games of pong until either player gets 21 points.
