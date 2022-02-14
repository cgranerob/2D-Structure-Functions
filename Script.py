#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
authors: C. Granero-Belinchon (IMT- Atlantique).
date: 02/2022
"""

#%% Import Libraries

import numpy as np
from Increments import Incrs_anisotropic_generator2d
from Moments import compute_moments_2D

#%% Script 2D Analysis

image=np.random.randn(256,256) # Interesting images of ocean surface roughness can be found at https://www.seanoe.org/data/00456/56796/

# We normalize the image by centering and standarizing it
tmp=(image-np.nanmean(image))/np.nanstd(image)

# Definition of scales
scalesx=np.arange(-40,41,1)
scalesy=np.arange(-40,41,1)

ps=np.array((2,3))
# Initialization of matrix
S=np.zeros((len(ps),len(scalesy),len(scalesx)))
S3norm=np.zeros((len(scalesy),len(scalesx)))

# Estimation of structure functions for each combination of scales (scalex,scaley)
for isx in range(len(scalesx)):
    for isy in range(len(scalesy)):  
        
        scalex=scalesx[isx]
        scaley=scalesy[isy]
        
        if scalex!=0 or scaley !=0:
            incrs = Incrs_anisotropic_generator2d(tmp, scalex, scaley)
            S[:,isy,isx]=compute_moments_2D(incrs, moms=ps)
            # Normalizing the increments avoid the effects of variance on higher order moments
            incrs=(incrs-np.mean(incrs))/np.std(incrs)
            S3norm[isy,isx]=compute_moments_2D(incrs, moms=3)
            
# We avoid the zero in the middle (we can not generate increment of size lx=ly=0)
S2=np.squeeze(S[0,:,:])
S2[40,40]=np.nan
S3norm[40,40]=np.nan
S2[40,40]=np.nanmean(S2[40-1:40+2,40-1:40+2])
S3norm[40,40]=np.nanmean(S3norm[40-1:40+2,40-1:40+2])

from Polar_coord import field_2D_polar
from Polar_coord import polar_axis

axis_t, axis_r, size = polar_axis(S2, n_theta=-1)
S2_polar = field_2D_polar(S2, n_theta=-1)
S3_polar = field_2D_polar(S3norm, n_theta=-1)

#%% Plot of images

# Cartesian
plt.figure()
plt.contourf(scalesy,scalesx,S2new, cmap=BrBG)
plt.xlabel(r'$\delta x$')
plt.ylabel(r'$\delta y$')
plt.colorbar()
plt.title(r'$S_2(\delta_x \delta_y X)$')
#plt.savefig('/home/administrateur/Desktop/Research/ANR_SCALES/Multiscale_Entropy_Images/Scripts_images-SAR/S2_2D_20170315.pdf',format='pdf',bbox_inches='tight')
plt.show()

plt.figure()
plt.contourf(scalesy,scalesx,S3new, cmap='seismic')
plt.xlabel(r'$\delta x$')
plt.ylabel(r'$\delta y$')
plt.colorbar()
plt.title(r'$S_3(\delta_x \delta_y X)$')
#plt.savefig('/home/administrateur/Desktop/Research/ANR_SCALES/Multiscale_Entropy_Images/Scripts_images-SAR/S3_2D_20170315.pdf',format='pdf',bbox_inches='tight')
plt.show()

# Polar
plt.figure()
plt.contourf(axis_r,axis_t,S2new_p, cmap=BrBG)
plt.xlabel(r'$r$')
plt.ylabel(r'$\theta$')
plt.colorbar()
plt.title(r'$S_2(\delta_r X)$')
plt.show()

plt.figure()
plt.contourf(axis_r,axis_t,S3new_p, cmap='seismic')
plt.xlabel(r'$r$')
plt.ylabel(r'$\theta$')
plt.colorbar()
plt.title(r'$S_3 $')
plt.show()

np.savez('StructureFunctions_Incrs_myimage.npz', S2=S2, S3norm=S3norm, ps=ps, scalesx=scalesx, scalesy=scalesy)
