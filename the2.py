# -*- coding: utf-8 -*-

def physics(inputs): #theta1, theta2, d, fs, fk, s, m1, m2, t1, t2

    theta1 = inputs[0]

    theta2 = inputs[1]

    d = inputs[2]

    fs = inputs[3]

    fk = inputs[4]

    s = inputs[5]

    m1 = inputs[6]

    m2 = inputs[7]

    t1 = inputs[8]

    t2 = inputs[9]

    import math

    theta3 = math.radians(180) - math.radians(theta1) - math.radians(theta2) #

    surface_m1 = math.sin(math.radians(theta2)) * d / math.sin(theta3) #inclined surface which m1 on

    surface_m2 = math.sin(math.radians(theta1)) * d / math.sin(theta3) #inclined surface which m2 on 

    g = 9.8  #gravitation constant

    if t1 == 0:

        newa_m1 = (m1 * g * math.sin(math.radians(theta1)) - fk * m1 * g * math.cos(math.radians(theta1))) / m1 #ip kesildikten sonraki m1 ivmesi            

        newa_m2 = (m2 * g * math.sin(math.radians(theta2)) - fk * m2 * g * math.cos(math.radians(theta2))) / m2 #ip kesildikten sonraki m2 ivmesi downward

        path_m1 = 0.5 * newa_m1 * t2 * t2 # ip kesildikten sonraki m1 in aldigi yol

        path_m2 = 0.5 * newa_m2 * t2 * t2 # ip kesildikten sonraki m2 nin aldigi yol

        x1_location = surface_m1 - (s/2) - (0.1)

        x2_location = surface_m2 - (s/2) - (0.1)

        if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenerse

            if x1_location - path_m1 >= 0 and x2_location - path_m2 >= 0:

                x1 = x1_location - path_m1

                x2 = x2_location - path_m2

            elif x1_location - path_m1 >= 0 and x2_location - path_m2 < 0:

                x1 = x1_location - path_m1

                x2 = 0

            elif x1_location - path_m1 < 0 and x2_location - path_m2 >= 0:

                x1 = 0

                x2 = x2_location - path_m2

            elif x1_location - path_m1 < 0 and x2_location - path_m2 < 0:

                x1 = 0

                x2 = 0

        elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) <= (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # m1 statik surtunmeyi yener , m2 yenemezse            
            
            if x1_location - path_m1 >= 0:

                x1 = x1_location - path_m1

                x2 = x2_location

            elif x1_location - path_m1 < 0:

                x1 = 0

                x2 = x2_location

        elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) <= (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): #m1 statik surtunmeyi yenemez , m2 yenerse

            if x2_location - path_m2 >= 0:

                x2 = x2_location - path_m2

                x1 = x1_location

            elif x2_location - path_m2 < 0:

                x2 = 0

                x1 = x1_location

        elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) <= (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) <= (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenemezse

            x1 = x1_location

            x2 = x2_location
            


    elif t1 > 0:


        if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360) + fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360):

            # m1 slides downward and m2 slides upward, with the same magnitude of acceleration.
            # a = g(m1.sintheta1-m2.sintheta2-fk.m1costheta1-fk.m2.costheta2)/(m1+m2)

            a = ((m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) - (fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) - (fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360))) / (m1 + m2)                                                 

            path1 = 0.5 * a * (t1**2) # t1 suresince alinan yol

            Vs = a * t1 # t1 sonundaki ortak hiz
            

            if path1 >= s / 2: #m2 stuck at pulley

                newa_t2_m1 = (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) # m1 ivmesi t2 suresinde

                newa_t2_m2 = (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) - (fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) # m1 ivmesi t2 suresinde

                path_t2_m2 = 0.5 * newa_t2_m2 * t2 * t2

                path_t2_m1 = 0.5 * newa_t2_m1 * t2 * t2

                x1 = surface_m1 - s - 0.1 - path_t2_m1 

                x2 = surface_m2 - 0.1 - path_t2_m2

                if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenerse

                        
                    if x1 > 0 and x2 > 0:

                        x1 = x1

                        x2 = x2

                    elif x1 > 0 and x2 <0:

                        x1 = x1

                        x2 = 0

                    elif x1< 0 and x2 >0:

                        x1 = 0

                        x2 = x2

                    else:

                        x1 = 0

                        x2 = 0

                elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # m1 statik surtunmeyi yener , m2 yenemezse
                        
                    if x1 > 0:

                        x1 = x1

                        x2 = surface_m2 - 0.1

                    else:

                        x1 = 0

                        x2 = surface_m2 - 0.1

                elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): #m1 statik surtunmeyi yenemez , m2 yenerse

                    if x2 > 0:

                        x2 = x2

                        x1 = surface_m1 - 0.1 - s

                    else:

                        x2 = 0

                        x1 = surface_m1 - 0.1 - s

                elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenemezse

                    x1 = surface_m1 - 0.1 - s

                    x2 = surface_m2 - 0.1

                     

            elif path1 < s / 2:

                newa_1 = ((m1 * g * math.sin(theta1 * 2 * math.pi / 360) - fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) / m1) #ip kesildikten sonraki m1 ivmesi

                newa_2_u = ((m2 * g * math.sin(theta2 * 2 * math.pi / 360) + fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) / m2) #ip kesildikten sonraki m2 ivmesi upward

                newa_2_d = ((m2 * g * math.sin(theta2 * 2 * math.pi / 360) - fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) / m2) #ip kesildikten sonraki m2 ivmesi downward
                        
                t_stop1 = (a * t1) / newa_1 #kayip durma suresi m1 icin

                t_stop2 = (a * t1) / newa_2_u #kayip durma suresi m2 icin

                path_m1_t2 = (Vs * t2) + (0.5 * newa_1 * (t2**2))
     
                path_m1_tstop1 = (Vs * t_stop1) + (0.5 * newa_1 * (t_stop1**2)) #t_stop1(durma suresi) m1 in aldigi yol

                path_m2_tstop2 = (Vs * t_stop1) - (0.5 * newa_2_u * (t_stop2**2)) #t_stop2(durma suresi m2 nin aldigi yol

                path_m2_t2_stop2 = (0.5 * newa_2_d * (t2-t_stop2)**2)
     
                m1_total = path1 + path_m1_t2

                x1 = surface_m1 - m1_total - s/2 - 0.1

                
                    

                if t2 >= t_stop2:

                    if path1 + path_m2_tstop2 >= s / 2:

                        if (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) <= (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): #m2 statik surtunmeyi yenemezse

                            x2 = surface_m2 - 0.1

                            if x1 >= 0:

                                x1 = x1

                            else:

                                x1 = 0

                        elif (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): #m2 statik surtunmeyi yenerse

                            x2 = surface_m2 - path_m2_t2_stop2 - 0.1

                            if x1 >= 0 and x2 >= 0:

                                x1 = x1

                                x2 = x2

                            elif x1 < 0 and x2 >= 0:

                                x1 = 0

                                x2 = x2
                                    
                            elif x1 >= 0 and x2 < 0:

                                x1 = x1

                                x2 = 0

                            elif x1 < 0 and x2 < 0:

                                x1 = 0

                                x2 = 0

                    elif path1 + path_m2_tstop2 < s / 2:

                        if (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) <= (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)):

                            if x1 >= 0:

                                x1 = x1

                                x2 = surface_m2 - (s/2 - path1 - path_m2_tstop2) - 0.1

                            elif x1 < 0:

                                x1 = 0

                                x2 = x2 = surface_m2 - (s/2 - path1 - path_m2_tstop2) - 0.1                            

                        elif (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)):

                            if x1 >= 0:

                                x1 = x1

                                x2 = surface_m2 - (s/2 - path1 - path_m2_tstop2) - 0.1 - path_m2_t2_stop2

                            elif x1 < 0:

                                x1 = 0

                                x2 = surface_m2 - (s/2 - path1 - path_m2_tstop2) - 0.1 - path_m2_t2_stop2

                elif t2 < t_stop2:

                    path_m2_t2 = (Vs * t2) - (0.5 * newa_2_u * (t2**2))

                    if x1 >= 0:

                        x1 = x1

                        x2 = surface_m2 - (s/2 - path1 - path_m2_t2) - 0.1

                    elif x1 < 0:

                        x1 = 0

                        x2 = surface_m2 - (s/2 - path1 - path_m2_t2) - 0.1                        

                            
        elif (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) - (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360) + fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360):

            # m2 slides downward and m1 slides upward, with the same magnitude of acceleration.
            # a = g(m2.sintheta2-m1.sintheta1-fk.m1costheta1-fk.m2.costheta2)/(m1+m2)

            a = ((m2 * g * math.sin(theta2 * 2 * math.pi / 360)) - (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) - (fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360))) / (m1 + m2)

            path1 = 0.5 * a * (t1**2)

            Vs = a * t1 # t1 sonundaki ortak hiz
            

            if path1 >= s / 2: #m1 stuck at pulley

                newa_t2_m1 = (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) # m1 ivmesi t2 suresinde

                newa_t2_m2 = (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) - (fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) # m2 ivmesi t2 suresinde

                path_t2_m2 = 0.5 * newa_t2_m2 * (t2**2)

                path_t2_m1 = 0.5 * newa_t2_m1 * (t2**2)

                x2 = surface_m1 - s - 0.1 - path_t2_m1 

                x1 = surface_m2 - 0.1 - path_t2_m2

                if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenerse

                        
                    if x1 > 0 and x2 > 0:

                        x1 = x1

                        x2 = x2

                    elif x1 > 0 and x2 <0:

                        x1 = x1

                        x2 = 0

                    elif x1 < 0 and x2 >0:

                        x1 = 0

                        x2 = x2

                    else:

                        x1 = 0

                        x2 = 0

                elif (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) and (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)): # m2 statik surtunmeyi yener , m1 yenemezse
                        
                    if x2 > 0:

                        x2 = x2

                        x1 = surface_m1 - 0.1

                    else:

                        x2 = 0

                        x1 = surface_m1 - 0.1

                elif (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) and (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)): #m2 statik surtunmeyi yenemez , m1 yenerse

                    if x1 > 0:

                        x1 = x1

                        x2 = surface_m2 - 0.1 - s

                    else:

                        x1 = 0

                        x2 = surface_m2 - 0.1 - s

                elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenemezse

                    x2 = surface_m2 - 0.1 - s

                    x1 = surface_m1 - 0.1

                     
#################################
                    
            elif path1 < s / 2:

                newa_2 = ((m2 * g * math.sin(theta2 * 2 * math.pi / 360) - fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) / m2) #ip kesildikten sonraki m2 ivmesi

                newa_1_u = ((m1 * g * math.sin(theta1 * 2 * math.pi / 360) + fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) / m1) #ip kesildikten sonraki m1 ivmesi upward

                newa_1_d = ((m1 * g * math.sin(theta1 * 2 * math.pi / 360) - fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) / m1) #ip kesildikten sonraki m1 ivmesi downward
                        
                t_stop2 = (a * t1) / newa_2 #kayip durma suresi m2 icin

                t_stop1 = (a * t1) / newa_1_u #kayip durma suresi m1 icin

                path_m2_t2 = (Vs * t2) + (0.5 * newa_2 * (t2**2))
     
                path_m2_tstop2 = (Vs * t_stop2) + (0.5 * newa_2 * (t_stop2**2)) #t_stop2(durma suresi) m2 in aldigi yol

                path_m1_tstop1 = (Vs * t_stop1) - (0.5 * newa_1_u * (t_stop2**2)) #t_stop1(durma suresi m1 nin aldigi yol

                path_m1_t2_stop2 = (0.5 * newa_1_d * (t2-t_stop2)**2)
     
                m2_total = path1 + path_m2_t2

                x2 = surface_m2 - m2_total - s/2 - 0.1

                
                    

                if t2 >= t_stop1:

                    if path1 + path_m1_tstop1 >= s / 2:

                        if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) <= (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)): #m1 statik surtunmeyi yenemezse

                            x1 = surface_m1 - 0.1

                            if x2 >= 0:

                                x2 = x2

                            else:

                                x2 = 0

                        elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)): #m1 statik surtunmeyi yenerse

                            x1 = surface_m1 - path_m1_t2_stop2 - 0.1

                            if x2 >= 0 and x1 >= 0:

                                x2 = x2

                                x1 = x1

                            elif x2 < 0 and x1 >= 0:

                                x2 = 0

                                x1 = x1
                                    
                            elif x2 >= 0 and x1 < 0:

                                x2 = x2

                                x1 = 0

                            elif x2 < 0 and x1 < 0:

                                x1 = 0

                                x2 = 0

                    elif path1 + path_m1_tstop1 < s / 2:

                        if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) <= (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)):

                            if x2 >= 0:

                                x2 = x2

                                x1 = surface_m1 - (s/2 - path1 - path_m1_tstop1) - 0.1

                            elif x2 < 0:

                                x1 = 0

                                x1 = surface_m1 - (s/2 - path1 - path_m1_tstop1) - 0.1                            

                        elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)):

                            if x2 >= 0:

                                x2 = x2

                                x1 = surface_m1 - (s/2 - path1 - path_m1_tstop1) - 0.1 - path_m1_t2_stop2

                            elif x2 < 0:

                                x2 = 0

                                x1 = surface_m1 - (s/2 - path1 - path_m1_tstop1) - 0.1 - path_m1_t2_stop2

                elif t2 < t_stop1:

                    path_m1_t2 = (Vs * t2) - (0.5 * newa_2_u * (t2**2))

                    if x2 >= 0:

                        x2 = x2

                        x1 = surface_m1 - (s/2 - path1 - path_m1_t2) - 0.1

                    elif x2 < 0:

                        x2 = 0

                        x1 = surface_m1 - (s/2 - path1 - path_m1_t2) - 0.1


#######################################################################################
            
        elif math.fabs((m1 * g * math.sin(theta1 * 2 * math.pi / 360)) - (m2 * g * math.sin(theta2 * 2 * math.pi / 360))) <= math.fabs(fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360) + fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)):

            # The system remains at rest.
            # a = 0

            newa_m1 = ((m1 * g * math.sin(theta1 * 2 * math.pi / 360) - fk * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) / m1) #ip kesildikten sonraki m1 ivmesi            

            newa_m2 = ((m2 * g * math.sin(theta2 * 2 * math.pi / 360) - fk * m2 * g * math.cos(theta2 * 2 * math.pi / 360)) / m2) #ip kesildikten sonraki m2 ivmesi downward

            path_m1 = (0.5 * newa_m1 * (t2**2)) # ip kesildikten sonraki m1 in aldigi yol

            path_m2 = (0.5 * newa_m2 * (t2**2)) # ip kesildikten sonraki m2 nin aldigi yol

            x1 = surface_m1 - (s/2) - 0.1 - path_m1

            x2 = surface_m2 - (s/2) - 0.1 - path_m2

            if (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenerse

                if x1 >= 0 and x2 >= 0:

                    x1 = x1

                    x2 = x2

                elif x1 >= 0 and x2 < 0:

                    x1 = x1

                    x2 = 0

                elif x1 < 0 and x2 >= 0:

                    x1 = 0

                    x2 = x2

                elif x1 < 0 and x2 < 0:

                    x1 = 0

                    x2 = 0

            elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) > (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # m1 statik surtunmeyi yener , m2 yenemezse

                x2 = surface_m2 - (s/2) - 0.1

                if x1 >= 0:

                    x1 = x1

                elif x1 < 0:

                    x1 = 0

            elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) > (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): #m1 statik surtunmeyi yenemez , m2 yenerse

                x1 = surface_m1 - (s/2) - 0.1

                if x2 >= 0:

                    x2 = x2

                elif x2 < 0:

                    x2 = 0

            elif (m1 * g * math.sin(theta1 * 2 * math.pi / 360)) < (fs * m1 * g * math.cos(theta1 * 2 * math.pi / 360)) and (m2 * g * math.sin(theta2 * 2 * math.pi / 360)) < (fs * m2 * g * math.cos(theta2 * 2 * math.pi / 360)): # ikisi de statik surtunmeyi yenemezse

                x1 = surface_m1 - (s/2) - 0.1

                x2 = surface_m2 - (s/2) - 0.1


    return [x1,x2]
