import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()

ax.plot(np.arange(0,25,5),[1,7,3,5,11],color='red',marker='o',label='line1')
ax.plot(np.arange(0,25,5),[4,3,1,8,12],color='green',marker='o',linestyle='dashdot',label='line2')
# in the task picture label is line1 for both, but it's pretty obvious it should be line1 and line2
ax.legend()
plt.show()

fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,2,3)
ax3=fig.add_subplot(2,2,4)
ax1.plot([1,7,6,3,4])
ax2.plot([9,4,2,4,9])
ax3.plot([-7,-4,2,-4,-7])
plt.show()

fig,ax=plt.subplots()
x=np.linspace(-5,5,11)
ax.plot(x,[x1*x1 for x1 in x])
ax.annotate('min',xy=(0,0),xytext=(0,10),arrowprops = dict(facecolor = 'green'))
plt.show()

fig=plt.figure()
grid = plt.GridSpec(2, 8)
picture=fig.add_subplot(grid[:,:-1])
cb=fig.add_subplot(grid[1,-1])

rng = np.random.default_rng(10)
data = rng.normal(5,5,size=(7,7)) # no idea what sort of data is used for this picture,so I'll just use random one
im=picture.imshow(data,extent=(0,7,0,7))
plt.colorbar(im,cax=cb)
plt.show()

fig,ax=plt.subplots()
x = np.arange(0.0, 5, 0.01)
y = np.cos(x*np.pi)
plt.plot(x, y, color = "red")
plt.fill_between(x, y)
plt.show()

fig,ax=plt.subplots()
x = np.arange(0.0, 5, 0.01)
y=[np.cos(xx*np.pi) if np.cos(xx*np.pi)>=-0.5 else None for xx in x]
plt.ylim(-1, 1)
plt.plot(x, y, linewidth=3)
plt.show()


fig, axs = plt.subplots(1, 3, figsize=(15, 4))
x = np.arange(0, 7)
y = x
where_set = ['pre', 'post', 'mid']
for i, ax in enumerate(axs):
  ax.step(x, y, "g-o", where=where_set[i])
  ax.grid()
plt.show()

fig, ax = plt.subplots()
x = np.arange(0, 11, 1)
y1 = np.array([(-0.2)*i**2+2*i for i in x])
y2 = np.array([(-0.4)*i**2+4*i for i in x])
y3 = np.array([2*i for i in x])
labels = ["y1", "y2", "y3"]
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')
plt.show()

fig, ax = plt.subplots()
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
ax.pie(vals, labels=labels)
ax.axis("equal")
plt.show()

fig, ax = plt.subplots()
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))
plt.show()