from gym.envs.registration import register
register(
    entry_point='chess_env.envs:chessEnv',
    id='chess-v0',
)
