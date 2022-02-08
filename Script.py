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

image=np.random.randn(256,256)
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

np.savez('StructureFunctions_Incrs_myimage.npz', S2=S2, S3norm=S3norm, ps=ps, scalesx=scalesx, scalesy=scalesy)
