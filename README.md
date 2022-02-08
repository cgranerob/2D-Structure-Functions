# 2D-Structure-Functions
Two-dimensional structure functions for direction-dependent multiscale analysis of textures.

This repository contains two main functions: 

1) Incrs_anisotropic_generator2d: contained in the Increments.py file, this function takes as input a two-dimensional field <img src="https://render.githubusercontent.com/render/math?math=F(x,y)"> and two scales <img src="https://render.githubusercontent.com/render/math?math=l_x"> and <img src="https://render.githubusercontent.com/render/math?math=l_y"> and generates the process <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F = F(r_x %2B l_x,r_y %2B l_y) - F(r_x,r_y)"> which is the spatial increment of the two-dimensional field.
2) compute_moments_2D: contained in the Moments.py file, this function computes the <img src="https://render.githubusercontent.com/render/math?math=p"> order moment of a given n-dimensional field introduced as input.

Both functions can be combined to perform a multiscale direction-dependent analysis of images based on structure functions, see Script.py.

The nth order structure function of a two-dimensional field <img src="https://render.githubusercontent.com/render/math?math=F(x,y)"> can be defined as:

<img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{n}(F) = \mathbb{E} \left\{ \left( F(r_{x} %2B l_{x}, r_{y} %2B l_{y}) - F(r_{x}, r_{y}) \right)^{n} \right\} ">

where <img src="https://render.githubusercontent.com/render/math?math=(r_x,r_y)"> denotes a spatial position, <img src="https://render.githubusercontent.com/render/math?math=l_x"> and <img src="https://render.githubusercontent.com/render/math?math=l_y"> are the separation distances along each dimension of the field and <img src="https://render.githubusercontent.com/render/math?math=\mathbb{E}"> is the expected value operator. So, the second order structure function <img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{2}(F)"> is the variance of the increment <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F">, the third order structure function <img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{3}(F)"> is the skewness of the increment <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F">, the fourth order structure function <img src="https://render.githubusercontent.com/render/math?math=S^{l_x,l_y}_{4}(F)"> is the kurtosis of the increment <img src="https://render.githubusercontent.com/render/math?math=\delta_{l_x,l_y}F"> and so on.

A change of coordinates from cartesian to polar allows for analysis with respect to direction: <img src="https://render.githubusercontent.com/render/math?math=S_{n}^{l_x,l_y} \rightarrow S_{n}^{r,\theta}">.
