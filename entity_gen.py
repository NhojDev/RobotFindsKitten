from entity import Entity
import random
import string

player = Entity(char="#", color=(255, 255, 255), name="Player", blocks_movement=True)

statue = Entity(char="▒", name="statue", blocks_movement=True, desc = "A strange weeping angel statue.")
kitten = Entity(char = random.choice(string.ascii_letters + string.punctuation + string.digits), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), name="kitten", blocks_movement=True, desc = "You've found the kitten!", success= True)
yarn = Entity(char = random.choice(string.ascii_letters + string.punctuation + string.digits), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), name="yarn", blocks_movement=True, desc = "A normal ball of yarn.")
cat_toys = Entity(char = random.choice(string.ascii_letters + string.punctuation + string.digits), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), name="cat_toys", blocks_movement=True, desc = "A pile of random cat toys.")
fish_bones = Entity(char = random.choice(string.ascii_letters + string.punctuation + string.digits), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), name="fish_bones", blocks_movement=True, desc = "Fish bones.")