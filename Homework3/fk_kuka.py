def DH_transform(q, d, alpha, a): 
            '''The modified DH convention transform matrix
            alpha: twist angle, a: link length, 
            d: link offset, q: joint angle'''
            T = Matrix([[             cos(q),             -sin(q),           0,               a],
                        [sin(q) * cos(alpha), cos(q) * cos(alpha), -sin(alpha), -sin(alpha) * d],
                        [sin(q) * sin(alpha), cos(q) * sin(alpha),  cos(alpha),  cos(alpha) * d],
                        [                  0,                   0,           0,               1]])
            return T 

        
        
            ''' Rotation matrix along x axis'''
            R_x = Matrix([[      1,      0,      0],
                          [      0, cos(q), -sin(q)],
                          [      0, sin(q),  cos(q)]])
            
            return R_x
    

            ''' Rotation matrix along y axis'''
            R_y = Matrix([[ cos(q),     0, sin(q)],
                          [      0,     1,      0],
                          [-sin(q),     0, cos(q)]])
            
            return R_y

    
            ''' Rotation matrix along z axis'''
            R_z = Matrix([[ cos(q),-sin(q), 0],
                          [ sin(q), cos(q), 0],
                          [      0,      0, 1]])
            
            return R_z
