# fault_offset_distribution
Python codes for analyzing the distribution of vertical scarp offset along a fault. Includes interpolating data points, calculating moving average, and plotting results. Example data is from the Sawtooth fault (see Lifton et al., 2023; https://earthquake.usgs.gov/cfusion/external_grants/reports/G21AP10271.pdf). 

We measured vertical separation from topographic profiles at 85 sites on the Sawtooth fault in central Idaho. Topographic profiles were extracted from QL1 lidar digital elevation models in ArcGIS, and analyzed using the Matlab topographic profile tool developed by DuRoss et al. (2019). 

The first python script is `linear_interpolation_main_branch.py`. This script reads a datafile with two columns (distance along fault and vertical separation) and no header. It uses a 1D interpolation with defined interval to create regularly spaced data points between the irregular vertical offset measurements. The output datafile is `linear_interpolation_main_branch.txt`. This script also plots the original data points and an interpolated line between them.

The second python script is `moving_average_padded_branches.py`. This script takes the output from the first script as input and performs a moving average. The window size can be adjusted. This script also does a simple padding to the data so that the average extends all the way to the end. It still needs some adjustments to make the beginning of the moving average more accurate - it currently started at zero because the left side of the data is not padded. The output is a datafile `moving_average_data_main_branch.txt`. It also plots a figure with the original data points with error bars (colored by age) and moving average.

This is still a work in progress and I will update as I make changes.
