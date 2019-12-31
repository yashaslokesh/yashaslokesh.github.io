Title: PyAdventure Basic Inventory Update
Date: 2019-12-15 06:00
Modified: 2019-12-15 06:00
Category: Python
Tags: python, pygame
Authors: Yashas Lokesh
Status: published
Summary: An update to my adventure game where I create the inventory interface and provide some basic controls for it.

## Setup

So for my yet-to-be-named adventure game, I decided that one good area to make progress in
would be creating an inventory system. In this post, I'll talk about how I created the
basic interface for the inventory, including the controls for navigating around. This
only took about 45 minutes to create from start to finish, with most of the time being spent
to get it to look *just* right.

To start off, I created the `inventory.py` file inside the `core/` package, then added some
necessary imports:

```python
import pygame
from pygame.locals import *

from random import randint

import core.constants as c
```

The first two lines import the [pygame](https://www.pygame.org/news) library and
the set of constants from `pygame.locals`. These constants are used when detecting
events or key/mouse presses, among other things.

On the next line, we import the `randint` function so we can create randomly-colored
components in the inventory window (these serve as placeholders for actual items).

Next, the constants created for the game are imported. I'm not sure what the best practice
or best way to do this is, so I just import the module as `c` so that I don't
get confused on where a particular constant comes from. 

## Classes

So the way the game is structured right now calls for creating a class for each usable
thing on the screen and then calling the `update()` method on the relevant group of
objects. If you haven't work with classes in Python before, it's really simple;
we're going to add a constructor, an `update()` method, and a `draw()` method.

Here's the basic skeleton of how we create that:

`inventory.py`:
```python
class Inventory(object):
    def __init__(self):
        pass
    
    def update(self, keydown_event):
        pass
    
    def draw(self, screen):
        pass
```

We'll set a few constants for inventory size and position on the screen.

`constants.py`:
```python
INVENTORY_SIZE = INVENTORY_WIDTH, INVENTORY_HEIGHT = (
    600,
    600,
)

INVENTORY_COORDS = INVENTORY_X, INVENTORY_Y = (
    SCREEN_WIDTH // 2 - INVENTORY_WIDTH // 2,
    SCREEN_HEIGHT // 2 - INVENTORY_HEIGHT // 2,
)
```

And now we can work on the constructor. We want the active item, i.e. the box
that the player has currently selected, to start at some constant, say `[0,0]`,
and we make this value a list so that we can alter the position of the active item later.

Next, every pygame object has to have a `Rect` associated with it. We want our `Rect`
to be static, fixed in a certain position on the screen. Using the above constants,
we can use the constructor for `Rect` and store this in the class. 

Finally, let's create a 4x4 array of RGB values that we can use to create the 
squares of the inventory. To do this, we can create an empty list and then populate
it with four lists of four RBG triples each.

All together, it could look something like this:

`inventory.py`:
```python
class Inventory(object):
    def __init__(self):
        self.active_item = [0, 0]

        self.rect = pygame.Rect(
            c.INVENTORY_X, c.INVENTORY_Y, c.INVENTORY_WIDTH, c.INVENTORY_HEIGHT
        )

        self.sample_item_colors = []

        # set rectangle colors for sample inventory
        for i in range(4):
            self.sample_item_colors.append([])
            for j in range(4):
                r, g, b = randint(50, 255), randint(50, 255), randint(50, 255)
                self.sample_item_colors[i].append((r, g, b))
```

Note that we use the `self.` syntax to indicate instance variables.
This code just sets up a rough visual look for the inventory. Next, we want to
draw this inventory to the screen. The `blit()` method of a `Surface` object will
draw one surface onto another. 

`inventory.py`:
```python
class Inventory(object):
    """ omitted code """
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (172, 237, 182), self.rect)

        item_rect = self.rect.copy()
        item_rect.size = 150, 150
        for i in range(4):
            item_rect.x = self.rect.x + (i * 150)
            for j in range(4):
                # item_rect = self.rect.copy()
                # item_rect.x, item_rect.y = item_rect.x + (i * 150), item_rect.y + (j * 150)
                item_rect.y = self.rect.y + (j * 150)
                # item_rect.size = 150, 150
                pygame.draw.rect(screen, self.sample_item_colors[i][j], item_rect)
```

This code draws a `rect` of a light-green color, almost like the color of jade. Then it copies the
rect of the inventory object and adjusts the size to draw each tile of the inventory. The 
inventory's rect is copied because it already has the correct `(x, y)` coordinates. Then, we
simply do a 4x4 loop to draw the entire inventory using the appropriate colors from 
`self.sample_item_colors`. 

There's one more component I want to add to the inventory this time, and that's a selection
box for picking whatever object you want from the screen. So the user needs to be able to hit
some buttons to scroll through our inventory and pick the appropriate item. We'll make the controls
for picking items be the arrow keys. Recall that we defined the `active_item` instance variable
earlier. We'll be mutating this list as we receive input. We can create an `update()` method
that accepts an object describing a keydown event.

`inventory.py`:
```python
class Inventory(object):
    """ omitted code """
    def update(self, keydown_event):
        if keydown_event.key == K_DOWN:
            self.active_item[1] += 1
        elif keydown_event.key == K_UP:
            self.active_item[1] += -1
        elif keydown_event.key == K_LEFT:
            self.active_item[0] -= 1
        elif keydown_event.key == K_RIGHT:
            self.active_item[0] += 1
```

To use this method, we need to pass in an appropriate event. How do we do that? All pygame events 
can be obtained using `pygame.event.get()`, and as we iterate through the returned collection, if
the type of the event is `KEYDOWN`, (so `event.type == KEYDOWN`, where `KEYDOWN` comes from
`pygame.locals`). The argument `keydown_event` should be of this type (we can add some error
throwing code to catch any errors related to this at another time).

So we then check the `key` attribute for each of the arrow keys. If the user hits the down arrow
key, we move down the `active_item` position. A problem quickly shows up if we try hitting the
button 4 or more times... this should cause the active item pointer to wrap back around
to the top of the inventory selection screen, but it just goes down forever. This
has an easy fix; when we go to the -1 or the 4 position we wrap back to the appropriate side
of the inventory square.

`inventory.py`:
```python
class Inventory(object):
def update(self, keydown_event):
    if keydown_event.key == K_DOWN:
        self.active_item[1] += 1
        if self.active_item[1] == 4:
            self.active_item[1] = 0
    elif keydown_event.key == K_UP:
        self.active_item[1] += -1
        if self.active_item[1] == -1:
            self.active_item[1] = 3
    elif keydown_event.key == K_LEFT:
        self.active_item[0] -= 1
        if self.active_item[0] == -1:
            self.active_item[0] = 3
    elif keydown_event.key == K_RIGHT:
        self.active_item[0] += 1
        if self.active_item[0] == 4:
            self.active_item[0] = 0
```

Now we actually need to use the `active_item` list to draw a selection box. Back to the `draw()`
method, we can do something similar to drawing the tiles for each item rectangle from before.
We want it to have the same size and start from the same `x, y` coordinates, but this
box will have a certain thickness. One way we can design the selection box is by making it
a frame, so that the frame encloses the selected object.

We can pick some arbitrary constant thickness that's less than half the width of the box, so less 
than or equal to 75. I'll pick 20, and add it to `constants.py` as `SELECTION_BOX_THICKNESS = 20`.

`inventory.py`:
```python
class Inventory(object):
    """ omitted code """
    def draw(self, screen: pygame.Surface):
        """ omitted draw code """
        selection_box = self.rect.copy()
        selection_box.size = 150, 150
        selection_box.x += (self.active_item[0] * 150) + (
            c.SELECTION_BOX_THICKNESS // 2
        )
        selection_box.y += (self.active_item[1] * 150) + (
            c.SELECTION_BOX_THICKNESS // 2
        )
        selection_box.width -= c.SELECTION_BOX_THICKNESS
        selection_box.height -= c.SELECTION_BOX_THICKNESS

        pygame.draw.rect(
            screen, (255, 255, 255), selection_box, c.SELECTION_BOX_THICKNESS
        )
```

Here's the extra code added in the `draw()` method. `pygame` draws the thickness of the box 
outwards, so we need to adjust the `x, y` coordinates to
start closer to actual size of the box and then adjust the `width` and `height` to constrain
the selection box to be the size of an individual item rectangle. Then, we draw
the white box onto the screen with our specified thickness.

So now our inventory code is complete, and we can go back to our main game loop in `game.py`
and configure it so that everytime a `KEYDOWN` event is encountered, we update the inventory,
and on each iteration of the loop, we draw to the screen. I made a choice to include
the inventory as part of the `Player` class, because each player has an inventory, so
to draw the inventory, we access it through our player and call the draw method with our
screen surface.

`game.py`:
```python
class Game:
    """ omitted code """
    def run(self):
        """ omitted code """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    running = False
                elif event.type == KEYDOWN:
                    self.player.inventory.update(event)

            self.player.inventory.draw(self.screen)

            pygame.display.flip()
```

What if the player is just interacting
with the other parts of the game, not the inventory? Then we shouldn't be updating the selection
box's location or seeing the inventory at all. We can add another local variable in `run()` named
`inventory_active` which will have the initial value `False`, 
and on iteration of the game loop, we watch for a certain keypress, maybe the `I` key, to
activate/deactivate the inventory screen. So we only update and draw the inventory when it is
active.

`game.py`:
```python
class Game:
    def run(self):
        self.inventory_active = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_i:
                        self.inventory_active = not self.inventory_active
                    if self.inventory_active:
                        self.player.inventory.update(event)

            keys = pygame.key.get_pressed()

            self.player.draw(self.screen)

            if self.inventory_active:
                self.player.inventory.draw(self.screen)

            pygame.display.flip()
```

The `player` sprite has an inventory, and we update and draw that one. 

All the code I used can be found on [my GitHub](https://github.com/yashaslokesh/pyadventure). 
If you have any questions, you can easily contact me on Twitter. 

Thanks for reading!