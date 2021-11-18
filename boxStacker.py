# Box Stacking Algorithm

# This python function takes the boxes entered into it and attempts to assemble it into a neat pallet.


# build a box class, represents a box
class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

# Box Array goes here
# build with the following sample
arr = [Box(1,1,1), Box(1,1,1), Box(1,1,1), Box(1,1,1), Box(1,1,1)]

# palletize function takes in an array of boxes, then returns an array of arrays, layer by layer
# in the form [[[layer1 row 1], [layer1 row 2],...], [[layer2 row1], [layer2 row2],...],...]
def palletize (arr):
    # starting with a resolution of 8x1x1 for simplicity's sake
    maxHeight = 8
    maxWidth = 1
    maxLength = 1

    