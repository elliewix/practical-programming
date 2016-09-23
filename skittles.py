import random

def make_candy_bowl(colors, num_candies):
	bowl = []
	for i in range(num_candies):
		candy = random.choice(colors)
		bowl.append(candy)
	return bowl

col_str = "red, blue, grey, yellow"

colors = col_str.split(", ")

print(colors)

howmany = 10000

bowl = []

for i in range(howmany):
    skittle = random.choice(colors)
    bowl.append(skittle)


for color in colors:
    print("there are", bowl.count(color), color)

# how can we collect these more formally?

color_count = {}

for color in colors:
    count = bowl.count(color)
    color_count[color] = count

print(color_count)

