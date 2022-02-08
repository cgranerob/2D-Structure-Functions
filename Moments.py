"""
authors: C. Granero-Belinchon (IMT- Atlantique).

date: 10/2021
"""
import numpy as np

def compute_moments_2D(data, moms=np.array((2,3))):
    """
    Function Moms = compute_moments_2D(data, moms) estimates the statistical moments of order moms of the given ''data''

    Input arguments :
        data   : signal of length Nx x Ny
        moms     : (1d array) order of the moments to estimate (default=np.array((2,3)))
    
    Output :
        Moms    : moments of the sampled image, len(moms) moments are returned
        
    Usage example :
        
        data=np.random.randn((1000,1000))
        incr = compute_moments_2D(data, moms=2)
    
    ##
    C. Granero-Belinchon (IMT- Atlantique), October 2021  
    """
    
    if len(np.shape(moms))==1:
        # Check dimension of moms, i.e. number of moments to estimate
        mm=len(moms)
    
        # Initialization of moments matrix 
        Moments=np.zeros((mm))
    
        for i in range(mm):      
            # Order of the moment
            p=moms[i]
            # Moments estimation
            Moments[i]=np.nanmean(data.flatten()**p) 
    elif len(np.shape(moms))==0:
        Moments=np.nanmean(data.flatten()**moms)
             
    return Moments
