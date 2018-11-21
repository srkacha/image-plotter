import matplotlib.pyplot as plt
import numpy as np

#prvo krovic
roofX = np.array([1, 11, 6, 1])
roofY = np.array([5, 5, 9, 5])

#sad moze temelj
houseFrameX = np.array([2, 2, 10, 10])
houseFrameY = np.array([5, 1, 1, 5])

#vrata jer ono mora se nekad i uci
doorX = np.array([6, 6, 8, 8])
doorY = np.array([1, 4, 4, 1])

#prozor jer valja se nekad i provjetriti
windowFrameX = np.array([3, 3, 5, 5, 3])
windowFrameY = np.array([4, 2, 2, 4, 4])

plt.figure()
plt.plot(roofX, roofY)
plt.plot(houseFrameX, houseFrameY)
plt.plot(doorX, doorY)
plt.plot(windowFrameX, windowFrameY)
plt.show()