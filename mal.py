def generate_ascii_art():
    height=23
    width=55
    
    for row in range(height):
        for col in range(width):
            char=" "
            if row==0:
                if col== 31:
                    char="#"
                elif 32 <= col <= 38:
                    char="@"
                elif col==39:
                    char="#"
            elif row==1:
                if 28 <= col <= 42:
                    char="@"
            elif row==2:
                if 26 <= col <= 31 or 40 <= col <= 43:
                    char="@"
                elif 32 <= col <= 33:  
                    char="*"
                elif 34 <= col <= 35:
                    char="#"
                elif col== 36 or col==39:
                    char="+" 
                elif 37 <= col <= 38:
                    char=" "
            elif row==3:
                if  25 <= col <= 28:
                    char="@"  
                elif col == 29 or col==43:
                    char="="  
                elif 30 <= col <= 42:
                    char=" "
                elif col==44:
                    char="."                  
            elif row==4:               
                if 24 <= col <= 27:
                    char="@"
                elif col==27 or 30 <= col <= 31:
                    char="*"
                elif col==28 or  col==40:
                    char="-"
                elif col==29 or col==33 or col==41 or col==43:
                    char="="
                elif col==32 or col==39:
                    char=":"
                elif col==34 or col==42:
                    char="+"
                elif 35 <= col <= 38:
                    char=" "
                elif 44 <= col <= 45:
                    char="%"
            elif row==5: 
                if      24 <= col <= 25 or 44 <= col <= 45:
                    char="@"
                elif col==26:
                    char="#"
                elif col==27 :
                    char="%"
                elif 28 <= col <= 31 or col==43:
                    char="*"
                elif col==32 or col==39:
                    char=":"
                elif col==33:
                    char="="
                elif col==34 or col==41:
                    char="-"    
                elif 35 <= col <= 38:
                    char=" "
                elif col==40:
                    char="."  
                elif col==41:
                    char="+"  
                    
            elif row==6: 
                if 24 <= col <= 25 or col==45:
                    char="@"
                elif col==26 or col==44:
                    char="%"
                elif col==27 :
                    char="#"
                elif col== 28:
                    char="*"
                elif col==29 or col==40:
                    char="+"
                elif 30 <= col <= 38:
                    char=" "
                elif col==41:
                    char="-"
                elif col==42:
                    char=":"
                              
            elif row==7:
                 if 24 <= col <= 25 or col==45:
                    char="@"
                 elif 26 <= col <= 41 :
                    char=" " 
                 elif col==42:
                    char="="
                 elif col==43:
                    char=":"
                 elif col==44:
                    char="+"         
            elif row==8:
                if col==23:
                    char="#"
                elif 24 <= col <= 27 or 29 <= col <= 37 or 40 <= col <= 47:
                    char="@"
                elif col==28:
                    char="."
                elif col==38 or col==39:
                    char="="
            elif row==9:
                if col==22:
                    char=":"
                elif col==23 or col==25 or 27 <= col <= 29 or col==31  or 33 <= col <= 35 or col== 37 or 39 <= col <= 41 or 43 <= col <= 44:
                    char=" " 
                elif  col==24 : 
                    char="-"
                elif col==26:
                    char="*"
                elif col==30: 
                    char="%"
                elif col==32 or col ==42:   
                    char="="                        
                elif col==36:
                    char="#"
                elif col==38:
                    char="@"
                elif col==45:
                    char="."
                      
            elif row==10:
                if col==23:
                    char=":"
                elif 24 <= col <= 30 or 36 <= col <= 39:
                    char=" "
                elif 31 <= col <= 34 or  40 <= col <= 45:
                    char="@" 
                elif col==35:
                    char="-"      
                                  
            elif row==11:
                if   col==23 or col== 36:
                    char=":"            
                elif col==24 or col==29:
                    char="#"
                elif col==25 or 31 <= col <= 35 or 38 <= col <= 42:
                    char=" "
                elif col==26 or col==27:
                    char="%"
                elif col==28 :
                    char="+"
                elif col==30:
                    char="."
                elif col==37 or col==43:
                    char="="
                elif col==44:
                    char="@"
                    
            elif row==12:
                if  col==25 or col==30 or col==31:
                    char=":"
                elif col==26 or col==28:
                    char="="
                elif col==27 or 36 <= col <= 41 or col == 44: 
                    char="@"
                 
            elif row==13:
                if  col==25:
                    char=":"
                elif 26 <= col <= 27 or col==44: 
                    char="@"
                elif col==31:
                    char="="
                elif col==28 or col==32:
                    char="."
                elif 29 <= col <= 30 or 34 <= col <= 43:
                    char=" "
                elif col==33:
                    char="*"
            elif row==14:
                if  col==25:
                    char="."
                elif col==26 or col==42 :
                    char="="
                elif col==27 or 35 <= col <= 37 or col==39 or col==41 or col==44: 
                    char="@"
                elif col==28:
                    char="-"
                elif 29 <= col <= 30 or 32 <= col <= 33 or col==43:
                    char=" "
                elif col==31:
                    char=":"
                elif col==34:
                    char="#"
                elif col==38 or col==40:
                    char="%"
                         
            elif row==15:
                if col==26 or col==30 or col==36 or col==40:
                    char="-"
                elif col==27 or col==32:
                    char=":"
                elif 28 <= col <= 29 or  col==43:
                    char="@"
                elif col==31 or 34 <= col <= 35 or  col==39 or col==41 or col==42:
                    char=" "
                elif col==33:
                    char="."
                elif col==37 or col==38:
                    char="="
                               
            elif row==16:
                if  25 <= col <= 26 or 29 <= col <= 31 or col==42:
                    char="@" 
                elif 27 <= col <= 28 or 33 <= col <= 41:
                    char=" " 
                elif col==32:
                    char="-"             
            elif row==17:
                if col==26 or 31 <= col <= 33 or  col==41:
                    char="@"
                elif col==24 or 28 <= col <= 30 or 34 <= col <=36 or 38 <= col <=40:
                    char=" "
                elif col==23 or col==27:
                    char="%"
                elif col==25:
                    char=":"
                elif col==37:
                    char="."
                               
            elif row==18:
                if 21 <= col <= 22 or 33 <= col <= 39 :
                    char="@"
                elif 24 <= col <= 26 or 29 <= col <= 32:
                    char=" "
                elif col==23:
                    char=":"
                elif col==27 :
                    char="+"
                elif col==28:
                    char="="
                elif col==40:
                    char="%"    
                               
            elif row==19:
                if 17 <= col <= 22 or 38 <= col <= 41 :
                    char="@"  
                elif 24 <= col <= 28 or 31 <= col <= 36:
                    char=" "
                elif col==23:
                    char="+"
                elif col==29 :
                    char="."
                elif col==30:
                    char=":"
                elif col==37:
                    char="*"
            elif row==20:
                if 13 <= col <= 23 or 41 <= col <= 45 or 36 <= col <= 37:
                    char="@"
                elif 24 <= col <= 31 or 38 <= col <= 40:
                    char=" "
                elif col==32 or col==33:
                    char="="
                elif col==34:
                    char=":"
                elif col==35:
                    char="%"
            elif row==21:
                if 7 <= col <= 24 or 42 <= col <= 50:
                    char="@"
                elif 25 <= col <= 33 or 38 <= col <= 41:
                    char=" "
                elif col==34:
                    char="\\"
                elif 35 <= col <= 36:
                    char=" "
                elif col==37:
                    char="/"                            
            elif row==22:
                if 2 <= col <= 25 or 43 <= col <= 55:
                    char="@"
                elif 26 <= col <= 33 or 38 <= col <= 42:
                    char=" "
                elif col==34:
                    char="/"
                elif 35 <= col <= 36:
                    char=" "
                elif col==37:
                    char="\\"
                    
                            
                               
                           
            print (char, end='')
        print()   

generate_ascii_art()                 
