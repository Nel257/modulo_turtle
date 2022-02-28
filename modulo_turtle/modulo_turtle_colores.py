def color_hex(num):
    colorh = ''
#    if num == 1:
#        colorh = '#FF0000'
#    elif num == 2:
#        colorh = '#00FF00'
#    elif num == 3:
#        colorh = '#FFFF00'
#    elif num == 4:
#       colorh = '#0000FF'
#    return colorh

    colores = {
                1:'#FF0000',
                2:'#00FF00', 
                3:'#FFFF00', 
                4:'#0000FF'
                }
    
    colorh = colores.get(num)
    return colorh                            # Logré optimizarlo, yupi!!

#print(color_hex(2))