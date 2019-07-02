from gym.envs.registration import register
register(
    id='chess-v0',
    entry_point='chess_env.envs:chessEnv',
)