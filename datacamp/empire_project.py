# import numpy, matplotlib, and set seed
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
# clear the plot
plt.clf()

# initialization
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        # if loop starts
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1, 7)

        # implement clumsiness
        if np.random.rand() < 0.001:
            step = 0 

        random_walk.append(step)
    all_walks.append(random_walk)

# convert all_walks to a NumPy array: np_aw
np_aw = np.array(all_walks)

# transpose np_aw
np_aw_t = np.transpose(np_aw)

# select last row from np_aw_t: ends
ends = np_aw_t[-1]

# plot histogram of ends, display plot
plt.hist(ends, bins=30)
plt.title("Distribution of Random Walk Ends")
plt.xlabel("Final Position")
plt.ylabel("Frequency")
plt.show()