"""

authors: C. Granero-Belinchon (IMT- Atlantique).

date: 09/2021
"""
import numpy as np

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
