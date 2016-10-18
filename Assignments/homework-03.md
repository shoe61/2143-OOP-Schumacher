###Scott Schumacher
###homework-03.md

**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
[]
['blue', 'red', 'green', 'red']
blue
1
1
[]
None
2
2
```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.



### Answer 2

```python

	def take_color(self, color):
			for i in range (len(self.skittles)-1):
				if self.skittles[i].color == color:
					return self.skittles.pop(i)
				else:
					return None

```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.



### Answer 3

```python

    def take_all(self):
        for i in range (len(self.skittles)-1):
            print(self.skittles.pop(i-1).color)

```
