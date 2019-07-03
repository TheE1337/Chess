import gym, chess
from gym import error, spaces, utils
from gym.utils import seeding
class chessEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
    self.state = chess.Board()

  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human', close=False):
    ...
