import matplotlib.pyplot as plt
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)
plt.plot([1,2,3,4,5],[1,4,9,16,25],"g--",label="F. cuadrática")
plt.plot([1,2,3,4,5],[1,8,27,64,125],"r*-",label="F. cúbica")
plt.ylabel("Altura [m]", fontsize=16)
plt.xlabel("Distancia [m]",fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0,140)
plt.xlim(0,5.5)
version=1.11
plt.text(1.1,64,"Graficas %.1f"%version, fontsize=12)
plt.legend(loc="upper left")
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.show()
