class Skittle(object):
    """A Skittle object has a color to describe it."""
    def __init__(self, color):
        self.color = color

class Bag(object):
    """A Bag is a collection of Skittles. All bags share the
    number of Bags ever made (sold) and each bag keeps track of
    its Skittles in a list.
    """

    number_sold = 0

    def __init__(self):
        self.skittles = []
        Bag.number_sold += 1

    def tag_line(self):
        """Print the Skittles tag line."""
        print("Taste the rainbow!")

    def print_bag(self):
        print([s.color for s in self.skittles])

    def take_skittle(self):
        """Take the first skittle in the bag (from the front of
        the skittles list).
        """
        return self.skittles.pop(0)

    def add_skittle(self, s):
        """Add a skittle to the bag."""
        self.skittles.append(s)
    
    def take_color(self, color):
        for i in range (len(self.skittles)-1):
            if self.skittles[i].color == color:
                return self.skittles.pop(i)
            else:
                return None

    def take_all(self):
        for i in range (len(self.skittles)-1):
            print(self.skittles.pop(i-1).color)

                
            
        

      

johns_bag = Bag()
johns_bag.print_bag()

for color in ['blue', 'red', 'green', 'red']:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()

#johns_bag.take_color('red')
johns_bag.print_bag()

johns_bag.take_all()
