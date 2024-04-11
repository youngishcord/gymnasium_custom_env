import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces
from gymnasium.envs.registration import register


register(
    id='test',
    entry_point='world:TestWorld',
)


class TestWorld(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 1}

    def __init__(self, render_mode=None, size=5):
        pass

    def reset(self, seed=None, options=None):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def seed(self):
        """Это нам не надо походу"""
        pass

