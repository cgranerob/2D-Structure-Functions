import numpy as np
import cv2

def Incrs_anisotropic_generator2d(image, scalex, scaley):
    '''    
    This function generate a vector of increments at a given scale_x, scale_y from a 2d image
 
    
    incrs = Incrs_anisotropic_generator2d(image, scalex, scaley)
    
    Input arguments :
        
        image  : image to analyze
        scalex    : size of scale in x dim
        scaley    : size of scale in y dim
        
    Output arguments :
        
        incr : vector of increments to compute statistics
        
    Usage example :
        
        image=np.random.randn((1000,1000))
        incr = Incrs_anisotropic_generator2d(image,scalex, scaley)

    Comments: In python first dimension is vertical alignment (y direction in this program). Second dimension is horizontal alignment (x direction)

    Comments: If image=array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
    
    scalex=scaley=1 then: image2=array([[9, 7, 8],
                                       [3, 1, 2],
                                       [6, 4, 5]])
    and so to define the increments such as Frisch 1995 (x(r+l) -x(r)) we have to define image -image2.
    

    ##
    C. Granero-Belinchon (IMT- Atlantique), September 2021
 
    '''  
    # check parameters
    if  image.ndim != 2 :
        raise TypeError('Image must be two dimensional.\n')
    
    image2=np.roll(image , scaley, axis=0)
    image2=np.roll(image2, scalex, axis=1)
    
    if scaley>=0 and scalex>=0:
        incr=-(image2[scaley::,scalex::]-image[scaley::,scalex::])
    elif scaley<0 and scalex<0:
        incr=-(image2[:scaley,:scalex]-image[:scaley,:scalex])
    elif scaley>=0 and scalex<0:
        incr=-(image2[scaley::,:scalex]-image[scaley::,:scalex])
    elif scaley<0 and scalex>=0:
        incr=-(image2[:scaley,scalex::]-image[:scaley,scalex::])
    
    return incr

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
    axis_t, axis_r, size = polar_axis(H, n_theta)
    R_max = size[0]-1
    return cv2.warpPolar(H_t, size, origin, R_max, cv2.WARP_POLAR_LINEAR+cv2.INTER_CUBIC)