from entity import Entity

player = Entity(char="#", color=(255, 255, 255), name="Player", blocks_movement=True)

statue = Entity(char="o", color=(63, 127, 63), name="statue", blocks_movement=True, desc = "A strange weeping angel statue.")
kitten = Entity(char="T", color=(0, 127, 0), name="kitten", blocks_movement=True, desc = "You've found the kitten!", success= True)
yarn = Entity(char="o", color=(63, 127, 63), name="yarn", blocks_movement=True, desc = "A normal ball of yarn.")
cat_toys = Entity(char="o", color=(63, 127, 63), name="yarn", blocks_movement=True, desc = "A pile of random cat toys.")