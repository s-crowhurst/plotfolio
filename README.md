This repo contains matplotlib stylesheets that I reqularly use for presenting scientific data.

To use them, you should put the .mpl file(s) you wish to use in your `~/.config/matplotlib/stylelib/` directory and the following at the top of your plotting script:

```Python
import matplotlib.pyplot as plt
plt.style.use('style_name') # Where style_name is the filename before .mplstyle (e.g. Light-01)
```
