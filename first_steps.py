import random
import matplotlib.pyplot as plt

def random_walk(n):
    """Returns a random moves defines by the number of steps"""
    random_list = list()

    #Coordinates
    x = 0
    y = 0
    for i in range(n):
                
        step = random.choice(['N', 'S', 'E', 'W'])

        if step == 'N':
            y += 1
            random_list.append((x,y))
        elif step == 'S':
            y -= 1
            random_list.append((x,y))
        elif step == 'E':
            x -= 1
            random_list.append((x,y))
        else:
            x += 1
            random_list.append((x,y))

        

    return random_list

def plot_walk(n):
    walks = random_walk(n)
    print(walks)
    x = [x for x, y in walks]
    y = [y for x, y in walks]

    plt.plot(x,y)
    plt.show()

track_1 = plot_walk(10)

# one = random_walk(10)
# print(one)
# for x, y in one:
#     print('printing x',x)
#     print('printing y', y)
    


