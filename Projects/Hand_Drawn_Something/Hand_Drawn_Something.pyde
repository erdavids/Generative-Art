w, h = 1000, 1000

line_points = []

colors_list=[['#b7b7a4','#ddbea9','#6b705c','#cb997e'],['#d4e09b','#f6f4d2','#cbdfbd','#f19c79','#a44a3f'],['#2b2d42','#8d99ae','#edf2f4','#ef233c','#d90429'],['#f4f1de','#e07a5f','#3d405b','#81b29a','#f2cc8f'],['#50514f','#f25f5c','#ffe066','#247ba0','#70c1b3'],['#8cb369','#f4e285','#f4a259','#5b8e7d','#bc4b51'],['#fe938c','#e6b89c','#ead2ac','#9cafb7','#4281a4'],['#177e89','#084c61','#db3a34','#ffc857','#323031'],['#e93e49','#fcf5e5'],['#000000','#ffffff'],["#f14d42","#f4fdec","#4fbe5d","#265487","#f6e916","#f9a087","#2e99d6"],["#f04924","#fcce09","#408ac9"],["#e95145","#f8b917","#b8bdc1","#ffb2a2"],['#a63d40','#e9b872','#90a959','#6494aa'],["#b8b8d1","#5b5f97","#ffc145","#fffffb","#ff6b6c"],["#edae49","#d1495b","#00798c","#30638e","#003d5b"],["#efbc9b","#725d68","#a8b4a5"],["#cad2c5","#84a98c","#52796f"],["#0d3b66","#faf0ca","#f4d35e"],["#885053","#fe5f55"],["#ac8887","#9f4a54","#6f8695"],["#f79256","#fbd1a2","#7dcfb6"],["#fc7a57","#ffd65c","#5e5b52","#98d9c2"],["#083d77","#ebebd3","#da4167","#f4d35e","#f78764","#a09ebb"],["#bee9e8","#62b6cb","#1b4965","#cae9ff","#5fa8d3"],["#41afc8","#84c0c6","#9fb7b9","#bcc1ba","#f2e2d2"],["#5bc0eb","#fde74c"],["#ab9787","#92b9bd","#a8d4ad","#f2f79e"],["#adc698","#c05746","#d0e3c4"],["#094074","#164b7d","#235586","#305f8f","#3c6997"],["#e01a4f","#f15946","#f9c22e","#53b3cb"],["#383d3b","#4f5251","#666767","#7d7c7d","#939192","#aaa6a8","#c1bbbe","#d8d0d4","#eee5e9"],["#f9e5c8","#f96273","#89b2bd"],["#ffc759","#ff7b9c","#607196"],["#628395","#96897b","#dbad6a"],["#e8d6cb","#d0ada7","#ad6a6c"],["#95b8d1","#f09d51","#394053"],["#ee6c4d","#58a4b0","#58a4b0","#f38d68"],["#ad343e","#474747","#f2af29"],["#be7c4d","#5d737e"],["#c05746","#1778b5","#adc698"]]
cols = colors_list[int(random(len(colors_list)))]
def get_random_color():
    return cols[int(random(len(cols)))]

step = 60

# lincount, offset, hue?
# Subdivide line into more points for curve?
# bo - Base offset for creating base
# bi - Base iterations for defomring base
# points defined as [[x, y], [x, y], ...]
def draw_cool_line(pts, bo, bi, fo, fi, dc):
    # Deform some to form a base
    for i in range(bi):
        for p in pts:
            # Add slight drift
            p[0] += random(-bo, bo)
            p[1] += random(-bo, bo)
    
    # Keep deforming on subsequent line draws to form variations
    bts = pts
    for i in range(fi):
        for b in bts:
            # Add slight drift
            b[0] += random(-fo, fo)
            b[1] += random(-fo, fo)
        beginShape()
        for b in bts:
            curveVertex(*b)
        endShape()
        
        strokeWeight(1)
        # Draw dots if you want?
        for j in range(1, len(bts) - 2):
            for d in range(dc):
                spot = random(1)
                dot_x = (1 - spot)* bts[j][0] + spot * bts[j + 1][0]
                dot_y = (1 - spot)* bts[j][1] + spot * bts[j + 1][1]
                
                circle(dot_x, dot_y, 1)
            
    
    # Debugging, draw base line
    # beginShape()
    # for p in pts:
    #     curveVertex(*p)
    # endShape()
# The path to drawing a good line

# Bounds (left, right, top, bottom), line count, point count
def draw_block(lc, pc):
    for i in range(lc):
        stroke(get_random_color())
        pts = []
        
        current = [random(0, w), random(0, h)]
        for i in range(pc):
            pts.append([current[0], current[1]])
            
            if (random(1) < .5):
                if (random(1) < .5):
                    current[0] += step
                else:
                    current[0] -= step
            else:
                if (random(1) < .5):
                    current[1] += step
                else:
                    current[1] -= step
            
        draw_cool_line(pts, 2, 2, 10, 2, 10)
        
        # Debugging, thin lines
        # draw_cool_line(pts, 0, 0, 0, 1, 0)
        
    
def setup():
    size(w, h)
    background("#f1faee")
    pixelDensity(2)
    strokeWeight(2)
    stroke(0, 0, 0, 120)
    noFill()

    for k in range(200):
        draw_block(5, 100)
    

    # Try some art
    save("Examples/HandDrawn/" + str(int(random(100000))) + ".png")
