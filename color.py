import operator

def color (G):
    colors = {}
    magnitudes = {}
    count = 0
    vertices = []
    for set in G:
        for element in set:
            if element not in vertices:
                vertices.append(element)
    for set in G:
        for element in set:
            count = 0

            for a in G:
                for b in a:
                    if element == b:
                        count += 1
            magnitudes[element] = count
            
    sortedReverse = sorted(magnitudes.items(), key=operator.itemgetter(1))
    sortedMag = []
    for i in range (len(sortedReverse)):
        sortedMag.append(sortedReverse[len(sortedReverse)-i-1])
    color = 1
    colors[sortedMag[0][0]]= color
    color = 2
    for i in sortedMag:
        isIn=False
        if i[1] in colors:
            print()
        elif i[1] not in colors:
            for j in G:
                for k in j:
                    if k in j and i[1] in j:
                        print()
                    elif k not in colors and i[1] != k:
                            
                        for a in G:
                            for b in a:
                                if b in colors and k in colors:
                                    color+=1
                        colors[k]=color
            
                    elif k not in colors:
                        colors[k] = color
    return colors
                          
                        
        
        
    
    
                
    
    
    
