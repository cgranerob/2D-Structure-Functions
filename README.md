# 2D-Structure-Functions
Two-dimensional structure functions for direction-dependent multiscale analysis of textures.

The nth order structure function of a two-dimensional field <img src="https://render.githubusercontent.com/render/math?math=F(x,y)"> can be defined as:

<img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{n}(F) = \mathbb{E} \left\{ \left( F(r_{x} %2B l_{x}, r_{y} %2B l_{y}) - F(r_{x}, r_{y}) \right)^{n} \right\} ">

where <img src="https://render.githubusercontent.com/render/math?math=(r_x,r_y)"> denotes a spatial position, <img src="https://render.githubusercontent.com/render/math?math=l_x"> and <img src="https://render.githubusercontent.com/render/math?math=l_y"> are the separation distances along each dimension of the field and <img src="https://render.githubusercontent.com/render/math?math=\mathbb{E}"> is the expected value operator. So, the second order structure function <img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{2}(F)"> is the variance of the increment <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F = F(r_x %2B l_x,r_y %2B l_y) - F(r_x,r_y)">, the skewness of the increment is the ratio <img src="https://render.githubusercontent.com/render/math?math=\frac{S^{l_x,l_y}_{3}(F)}{S^{l_x,l_y}_{2}(F)^{3/2}}">, the kurtosis of the increment is <img src="https://render.githubusercontent.com/render/math?math=\frac{S^{l_x,l_y}_{4}(F)}{S^{l_x,l_y}_{2}(F)^{2}}"> and so on.

A change of coordinates from cartesian to polar allows for analysis with respect to direction: <img src="https://render.githubusercontent.com/render/math?math=S_{n}^{l_x,l_y} \rightarrow S_{n}^{r,\theta}">.

# Contents
This repository contains four main functions contained in the Structure_functions.py file: 

1) **Incrs_anisotropic_generator2d**: takes as input a two-dimensional field <img src="https://render.githubusercontent.com/render/math?math=F(x,y)"> and two scales <img src="https://render.githubusercontent.com/render/math?math=l_x"> and <img src="https://render.githubusercontent.com/render/math?math=l_y"> and generates the process <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F"> which is the spatial increment of the two-dimensional field.
2) **compute_moments_2D**: computes the <img src="https://render.githubusercontent.com/render/math?math=p"> order moment of a given n-dimensional field introduced as input.
3) **field_2D_polar**: returns the cartesian field used as input in polar coordinates.
4) **polar_axis**: returns 2 numpy arrays characterizing the polar coordinates of the output field of the function field_2D_polar

These functions can be combined to perform a multiscale direction-dependent analysis of images based on structure functions, see Script.ipynb.

# References
Carlos Granero-Belinchon, Stephane G. Roux, Nicolas B. Garnier, Pierre Tandeo, Bertrand Chapron and Alexis Mouche, **Two-dimensional structure functions to characterize convective rolls in the marine atmospheric boundary layer from Sentinel-1 SAR images**, preprint Arxiv ...

# Contact

Carlos Granero-Belinchon <br />
Mathematical and Electrical Engineering Department <br />
IMT Atlantique <br />
Brest, France <br />
e: carlos.granero-belinchon [at] imt-atlantique.fr <br />
w: https://cgranerob.github.io/ <br />
w: https://www.imt-atlantique.fr/en/person/carlos-granero-belinchon <br />
