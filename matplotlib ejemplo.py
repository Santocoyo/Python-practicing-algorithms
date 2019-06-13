import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,4,9,16,25], "g--", label="Cuadrados")
plt.plot([1,2,3,4,5],[1,8,27,64,125], "r*-", label="Cubicos")
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.ylim(0,140)
plt.xlim(0,5.5)
plt.legend(loc="upper left")
plt.show()
