import numpy as np

depths = np.array([1.5, 3, 4.5, 6.0, 7.5, 9.0])
blows = np.array([4, 7, 12, 9, 22, 31])

depths_ft = depths * 3.28
print("Depths in feet:", depths_ft)

print("Average blows:", round(blows.mean(), 2))
print("Max blows:", blows.max())
print("Min blows:", blows.min())
print("Total blows:", blows.sum())

print("Blows above 10:", blows[blows > 10])

max_index = blows.argmax()
print("Max at depth:", depths[max_index], "m")