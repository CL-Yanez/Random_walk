import random
import matplotlib.pyplot as plt

def random_walk(n):
    """Returns a random moves defines by the number of steps"""
    random_list = list()

    #Coordinates
    start_position = random.randrange(10)
    random_list.append(start_position)
    
    for i in range(n):
                
        movement = -1 if random.random() > 0.5 else 1
        value = random_list[i] + movement
        random_list.append(value)
                

    return random_list

def plot_walk(n):
    walks = random_walk(n)


    random.seed(1)
    plt.plot(walks)
    plt.show()

# track_1 = plot_walk(500)

for i in range(3):
    plot_walk(200)
    


