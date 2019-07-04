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
  def check(board: state):
      if state.is_checkmate():
          if state.turn:
              return -1000
          else
              return 1000
      else:
          pieces = 0
          if state.is_check():
              pieces += 2
          for row in state:
              pieces += 9 * row.count('Q')
              pieces -= 9 * row.count('q')
              pieces += 5 * row.count('R')
              pieces -= 5 * row.count('r')
              pieces += 3 * row.count('K')
              pieces -= 3 * row.count('k')
              pieces += 3 * row.count('B')
              pieces -= 3 * row.count('b')
              pieces += 3 * row.count('N')
              pieces -= 3 * row.count('n')
              pieces += 1 * row.count('P')
              pieces -= 1 * row.count('p')
          return pieces

  def step(self, action):
    if self.state.isCheckmate:
        self.done = True
        self.reward = check(self.state)

    else:
        self.done = False
        self.state.push_san(action)
        self.reward = check(self.state)
    return [self.state, self.reward, self.done]





  def minimax(state, depth, a, b, maxplayer): #a: -1000, b: +1000 on initial call
      bestmove = ''
      if depth == 0 or state.is_checkmate():
          return check(state)
      if maxplayer:
          value = -1000
          for move in state.legal_moves:
              tempboard = state
              tempboard.push_san(move)
              value = max(value, minimax(tempboard, a, b, depth-1, False))
              a = max (a, value)
              if a >= b:
                  break
          return value
      else:
          value = 1000
          for move in state.legal_moves:
              tempboard = state
              tempboard.push_san(move)
              value = min(value, minimax(tempboard, a, b, depth-1, True))
              b = min(b,value)
              if a >= b:
                  break
          return value



  def reset(self):
    self.state.reset()

  def render(self, mode='human', close=False):
      #...
