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

# Image should be the two-dimensional field we want to analyze
image=np.random.randn(512,512)
# We normalize the image by centering and standarizing it
tmp=(image-np.nanmean(image))/np.nanstd(image)

# Definition of scales
scalesx=np.arange(-40,41,1)
scalesy=np.arange(-40,41,1)

ps=np.array((2,3))
# Initialization of matrix
S=np.zeros((len(ps),len(scalesy),len(scalesx)))
Snorm=np.zeros((len(ps),len(scalesy),len(scalesx)))

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
            Snorm[:,isy,isx]=compute_moments_2D(incrs, moms=3)
            
np.savez('StructureFunctions_Incrs_myimage.npz', S=S, Snorm=Snorm, ps=ps, scalesx=scalesx, scalesy=scalesy)
