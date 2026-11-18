import numpy as np

dem = np.array([
[120, 125, 130, 128, 122],
[118, 135, 150, 140, 125],
[115, 140, 165, 145, 128],
[110, 128, 138, 132, 120],
])

print(dem)
print("Shape:", dem.shape)
print("Row 2, column 2:", dem[2, 2])
print("Highest point:", dem.max(), "m")
print("Lowest point:", dem.min(), "m")
print("Average elevation:", round(dem.mean(), 1), "m")
print("Cells above 135 m:", (dem > 135).sum())
print(dem > 135)
print("row 0, coloumn 4",dem[0, 4])
print("max last roud" ,dem[3].max())
print(dem[:, 0].mean())
print(dem < 120)
print(dem.max()-dem.min())
