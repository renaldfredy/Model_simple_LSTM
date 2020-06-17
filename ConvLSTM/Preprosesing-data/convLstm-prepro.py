import os
from skimage import io
import math
from scipy.stats.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
from numpy import unravel_index
import pandas as pd

import matplotlib.colors as colors
import numpy as np

# This dictionary defines the colormap
cdict = {'red':  ((0.0, 0.0, 0.0),   # no red at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.8, 0.8)),  # set to 0.8 so its not too bright at 1

        'green': ((0.0, 0.8, 0.8),   # set to 0.8 so its not too bright at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0)),  # no green at 1

        'blue':  ((0.0, 0.0, 0.0),   # no blue at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0))   # no blue at 1
       }

# Create the colormap using the dictionary
GnRd = colors.LinearSegmentedColormap('GnRd', cdict)

# precipitation_path = os.path.join('.', 'data', 'CHIRTSmax.1983.01.tif')
# ================= mengumpulkan semua data ===================
path_files = os.listdir('../../../../Dataset/Data_JATIM/')
# print(path_files)
data_full = []
for i in range(len(path_files)-61):
	data_ = io.imread('../../../../Dataset/Data_JATIM/'+path_files[i])
	data_[data_<0]=0
	data_full.append(data_)
	print(i)

# print(path_files[347])
print(data_full[0])

# =============================================================


# ======== Menampilkan data 1 bulan ===============================================================
precip_full = io.imread('../../../../Dataset/Data_JATIM/'+path_files[0])

print(precip_full.shape)
precip_full[precip_full<0]=0

data = pd.DataFrame(precip_full)
print(data)
data.to_csv('file1.csv', header=True)


# let's print out the first month/band of this data
plt.figure(figsize=(15,6))
plt.imshow(precip_full[:,:], extent=[110.7, 116.4, -9.000001, -4.850001],cmap='Greys',vmin=1,vmax=36)
plt.show()
# =====================================================================================================

