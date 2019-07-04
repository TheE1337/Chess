from gym.envs.registration import register
register(
    entry_point='chessEnv.envs:chessEnv',
    id='chess_v0',
)
