"""

authors: C. Granero-Belinchon (IMT- Atlantique).

date: 09/2021
"""
import numpy as np
import cv2

def polar_axis(data, n_theta=-1):
    '''    
    This function returns 2 numpy arrays characterizing the polar coordinates 
    of the output field of the function field_2D_polar:
 
    axis_t, axis_r, size = polar_axis(data, n_theta=-1)

    Input arguments :
        
        data  : image to analyze
        n_theta : nb points desired in the theta direction if =-1: auto-detect (as R_max*pi) 
        
    Output arguments :
        
        axis_t : vector of angles
        axis_r : vector of radius
        size : shape of field in polar coordinates
        
    Usage example :
        
        image=np.random.randn((1000,1000))
        axis_t, axis_r, size = polar_axis(image, n_theta=-1)

   
    ##
    N.B Garnier (ENS Lyon) and C. Granero-Belinchon (IMT- Atlantique), September 2021
 
    '''  

    Nx,Ny = data.shape
    R_max = min(Nx//2,Ny//2)
    N_theta = n_theta if n_theta>0 else (int)(R_max*np.pi)
    size  = (R_max+1, N_theta)      # N_theta pts in [0,2*pi[ and R (tau) in [O, R_max]
    axis_t= np.arange(N_theta)/N_theta*2*np.pi - np.pi/2
    axis_r= np.arange(R_max+1)
    return axis_t, axis_r, size

   
def field_2D_polar(H, n_theta=-1):    
    '''    
    This function returns the cartesian field H in polar coordinates. The center of the field is used as origin.
    First dimension is the angle in [0, 2*pi[, second dimension is the radius in [0, R_max]
 
    H_polar = field_2D_polar(H, n_theta=-1)

    Input arguments :
        
        H  : field to analyze
        n_theta : nb points desired in the theta direction if =-1: auto-detect (as R_max*pi) 
        
    Output arguments :
        
        H_polar : H field in polar coordinates
        
    Usage example :
        
        image=np.random.randn((1000,1000))
        image_polar = field_2D_polar(image, n_theta=-1)

   
    ##
    N.B Garnier (ENS Lyon) and C. Granero-Belinchon (IMT- Atlantique), September 2021
 
    '''  

    Nx,Ny = H.shape
    H_t= np.transpose(H) # cv2 works on images, which are transposed of matrices
    origin= (Nx//2, Ny//2) 
    axis_t, axis_r, size = polar_axis(H, n_theta) # overkill here...
    R_max = size[0]-1
    return cv2.warpPolar(H_t, size, origin, R_max, cv2.WARP_POLAR_LINEAR+cv2.INTER_CUBIC) # possible option: cv2.WARP_FILL_OUTLIERS