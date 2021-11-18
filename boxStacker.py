# Box Stacking Algorithm

# This python function takes the boxes entered into it and attempts to assemble it into a neat pallet.


# build a box class, represents a box
class Box:
    def __init__(self, h, w, l, id):
        self.h = h
        self.w = w
        self.l = l
        self.id = id
    def __str__(self):
        return f'Box Id:{self.id}: w={self.w}, l={self.l}, h={self.h}'

# Box Array goes here
# build with the following sample
arr = [Box(1,1,1,'a'), Box(1,1,1,'b'), Box(1,1,1,'c'), Box(1,1,1,'d')]

# palletize function takes in an array of boxes, then returns an array of arrays, layer by layer
# in the form [[[layer1 row 1], [layer1 row 2],...], [[layer2 row1], [layer2 row2],...],...]
def palletize (array):
    # starting with a resolution of 2x2x2 for simplicity's sake
    maxHeight = 2
    maxWidth = 2
    maxLength = 2

    # define our output array
    # outputArray = [ [ [ [0] * maxLength] * maxWidth] * maxHeight]
    outputArray = [ [[0, 0], [0, 0]] , [[0, 0], [0, 0]] ]
    print(outputArray)
    #method 1: if it fits, it sits, 1x1x1 edition
    for box in array:
        print(box)
        homeFound = False
        while homeFound == False:
            for palletNumber,pallet in enumerate(outputArray):
                print('pallet')
                print(pallet)
                if homeFound == True:
                    break
                for levelNumber, level in enumerate(pallet):
                    print('nested level')
                    print(level)
                    # if we have open level
                    if homeFound == True:
                        break
                    for rowNumber, row in enumerate(level):
                        print('row')
                        print(row)
                        
                        # outputArray[0][0][0][0] = 1
                        print(f'level:{levelNumber}, row:{rowNumber}, val:{outputArray[palletNumber][levelNumber][rowNumber]}')
                        print(outputArray)
                        # if outputArray[palletNumber][levelNumber][rowNumber][singleUnitNumber] == 0:
                        if row == 0:
                            print('home found')
                            print(outputArray)
                            print('boxid')
                            print(box)
                            outputArray[palletNumber][levelNumber][rowNumber] = box.id
                            homeFound = True
                            break
                        # for singleUnitNumber,singleUnit in enumerate(row):
                        #     print('singleUnitNum')
                        #     print(singleUnitNumber)
                        #     # outputArray[0][0][0][0] = 1
                        #     print(f'level:{levelNumber}, row:{rowNumber}, sun:{singleUnitNumber}, val:{outputArray[palletNumber][levelNumber][rowNumber][singleUnitNumber]}')
                        #     print(outputArray)
                        #     # if outputArray[palletNumber][levelNumber][rowNumber][singleUnitNumber] == 0:
                        #     if singleUnit == 0:
                        #         print('home found')
                        #         print(outputArray)
                        #         print('boxid')
                        #         print(box.id)
                        #         outputArray[palletNumber][levelNumber][rowNumber][singleUnitNumber] = box.id
                        #         homeFound = True
                    else:
                        print('checking again')
                        continue
    
    return outputArray


palletize(arr)