from entity import Entity
import numpy as np

player = Entity(char="#", color=(255, 255, 255), name="Player", blocks_movement=True)

statue = Entity(char="o", color=np.random.random(size=3) * 256, name="statue", blocks_movement=True, desc = "A strange weeping angel statue.")
kitten = Entity(char="T", color=np.random.random(size=3) * 256, name="kitten", blocks_movement=True, desc = "You've found the kitten!", success= True)
yarn = Entity(char="o", color=np.random.random(size=3) * 256, name="yarn", blocks_movement=True, desc = "A normal ball of yarn.")
cat_toys = Entity(char="o", color=np.random.random(size=3) * 256, name="yarn", blocks_movement=True, desc = "A pile of random cat toys.")
fish_bones = Entity(char="o", color=np.random.random(size=3) * 256, name="yarn", blocks_movement=True, desc = "Fish bones.")