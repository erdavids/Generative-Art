w, h = 1000, 1000

# Number of blobs
grid_x = 40
grid_y = 40

grid_x_pixels = 1.1 * w
grid_y_pixels = 1.1 * h

sep_x = float(grid_x_pixels) / (grid_x - 1)
sep_y = float(grid_y_pixels) / (grid_y - 1)

#colors = [(92,97,130, 100), (79,164,165, 100), (202,166,122, 100), (212,117,100, 100)]
#colors = [(139,169,135), (244,107,99), (100,161,165)]
colors = []

#olors = [(255, 255, 255)]

def get_midpoint(x1, y1, x2, y2):
    return [(x1 + x2)/2, (y1 + y2)/2]

def get_distance(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    
def brush_points(x1, y1, x2, y2, brush_height, brush_sat, brush_drift, brush_tips, c, lo, ho):
    pushMatrix()
    
    translate(x1, y1)
    a = atan2(x2, y2);
    translate(-x1, -y1)
    
    # Move to the midpoint and calculate distance
    mp = get_midpoint(x1, y1, x2, y2)
    translate(x1, y1)

    d = get_distance(x1, y1, x2, y2)

    
    rotate(noise(mp[0] * .02, mp[1] * .02) * TWO_PI)
    # line(0, 0, 40, 40)
    
    # Actual Brush Mechanics
    
    fi = random(-brush_drift, brush_drift)
    se = random(-brush_drift, brush_drift)
    th = random(-brush_drift, brush_drift)
    
    for i in range(-brush_height, brush_height, brush_sat):
        strokeWeight(1)
        stroke(c[0], c[1], c[2])
        beginShape()
        
        be = random(-brush_tips, brush_tips)
        curveVertex(-d/2 + be, i + fi)
        curveVertex(-d/2 + be, i + fi)
        
        curveVertex(0, i + se)
        
        en = random(-brush_tips, brush_tips)
        curveVertex(d/2 + en, i + th)
        curveVertex(d/2 + en, i + th)
        #line(-d/2, i, d/2, i)
        endShape()
    popMatrix()

def setup():
    size(w, h)
    
    colorMode(HSB, 360, 100, 100)
    
    background(0, 0, 0)
    
    pixelDensity(2)
    
    strokeWeight(4)
    noFill()
    
    stroke(random(360), 80, 100)
    
    start_c = random(360)
    for i in range(8):
        colors.append(
                      (start_c, 30, 100))
        start_c += 15
        start_c = start_c%360
    
    current_x = w/2.0 - grid_x_pixels/2.0
    current_y = h/2.0 - grid_y_pixels/2.0
    for i in range(grid_x):
        for j in range(grid_y):
            diff = random(sep_y/2)
            brush_points(current_x, current_y, current_x + sep_x * random(1, 2), current_y + sep_y * random(1, 2), int(sep_x/3), 1, 7, 8, colors[int(random(len(colors)))], 100, 200)
            
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0
        current_x += sep_x
    
    save("Examples/NotBad/" + str(int(random(1000))) + ".png")
    
    
