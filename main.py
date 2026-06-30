"""
GalaxyLoft — Main Entry Point
Run this file to start the game: python main.py
"""

import sys
import os

# Add src to path so all imports work cleanly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import pygame
from src.systems.game_manager import GameManager

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("GalaxyLoft")

    game = GameManager()
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
