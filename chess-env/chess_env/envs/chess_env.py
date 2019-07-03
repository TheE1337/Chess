import gym, chess
from gym import error, spaces, utils
from gym.utils import seeding
class chessEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
    self.state = chess.Board()
    self.counter = 0
	self.done = 0
	self.add = [0, 0]
	self.reward = 0.0

  def step(self, action):
    if self.state.isCheckmate:
        if self.state.turn:
            return 1.0
        else
            return -1.0

  def reset(self):
    ...
  def render(self, mode='human', close=False):
    ...
