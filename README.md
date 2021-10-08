# pyplot-my-figure
Custom figure subclass to pyplot figure

## Install

1) clone the repo
```
git clone git@github.com:eborrell/mds.git
```

2) set python version
```
pyenv local 3.9.7
```

3) create virtual environment and install required packages
```
make venv
```

4) activate venv
```
source venv/bin/activate
```

## Developement

in step 3) also install developement packages
```
make develop
```

## Examples

1) import + define functions
```
from figures.myfigure import MyFigure

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)
f = x**2
g = x**3
```

2) show one line plot with linear scale
```
fig = plt.figure(FigureClass=MyFigure)
fig.plot(x, f)
plt.show()
```

3) save plot multiple lines plots with log scale for y axis
```
fig = plt.figure(FigureClass=MyFigure, dir_path='foo', file_name='bar')
y = np.vstack((f, g))
fig.set_plot_type('semilogx')
fig.plot(x, y)
```
