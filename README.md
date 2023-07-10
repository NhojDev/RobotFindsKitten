# RobotFindsKitten

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install to tcod

```bash
pip install tcod
```

## Usage
Open the folder in a terminal command line.

Enter the following line.

```bash
python main.py
```

## Questions and Answers

Question 1: Pick a player experience and feeling to target for this simple game. For example, you might want to make it energizing instead of zenlike, make it a hard grind or a quick jaunt, etc.

**I wanted to make the experience sort of a grind and mystery/uncanny type of vibe.**

Question 2: What choices can you make in objects to enhance this experience? This could include the object's symbol as well as its description.

**To make it more of a grind the symbols for the objects can be randomized to the kitten won't be the same every time the same is loaded. As for making it more of mystery/uncanny, I was thinking of having some object that just doesn't really belong with the other objects. An example could be that this object's description and symbol could be consistant throughout the different games, possibly causing the player to think "hmm that's weird, I wonder if it's intentional".**

After answering Question 2, adapt your object choices in your RFK implementation.

Question 3: What one small and simple enhancement to the game mechanics might enhance the experience you are trying to provide? For example, you might alter the movement commands somehow, add a timer, or whatever — sky's the limit as long as it's really easy. (Your game should still be close to the style of RFK after this enhancement. This is not an invitation to create a new game.)

**I want to add a fog around the player so that it both increases the grind aspect and the mystery/uncanny experience that I'm trying to emulate.**

After answering Question 3, make your enhancement.

Question 4: How confident are you that your game is (relatively) bug-free?

**Somewhat confident, since the source code that I referenced is pretty solid in it's implementation. However, I would not be surprise if bugs do pop up since I did make modfications to the code to make it more Robot Finds Kitten style.**

After answering Question 4, do whatever testing and inspection needs to be done to discover and eliminate bugs. Then have at least one player play the game, making notes as they go.

Question 5: What was the playtester's experience? Did it match your expectations?

**The player felt frustration and grind. Which matches **

Question 6: How does all this correlate with what you've read so far in The Book?

Question 7: What would a "AAA" version of your game look like? Is what you have done here helpful in visualizing that? Is the playtesting you've done relevant?

## Reference

Source Code was referenced from [Yet Another Roughlike Tutorial](http://rogueliketutorials.com/tutorials/tcod/v2/)