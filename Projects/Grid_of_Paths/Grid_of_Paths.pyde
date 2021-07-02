w, h = 1000, 1000

grid_x = 10
grid_y = 10

offset = 10

# The quads will draw inside this rectangle
grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

# Distance between the birds
sep_x = float(grid_x_pixels) / (grid_x - 1)
sep_y = float(grid_y_pixels) / (grid_y - 1)

points = []
trail_count = 75
trail_distance = 2
# trail_chance = .5
                

                
def draw_curvy():
    start_x = int(-sep_x/2 + offset)
    end_x = int(sep_x/2)
    
    start_y = random(-sep_y/2 + offset, sep_y/2)
    other_line = start_y - 20
    change_y = random(-1, 1)
    
    points = []
    
    stroke(15, 15, 15)
    beginShape()
    for i in range(start_x, end_x, 1):
        if (start_y > -sep_y/2 + offset and start_y < sep_y/2):
            vertex(i, start_y)
        points.append((i, start_y))
        start_y -= change_y
    endShape()
    
    beginShape()
    for i in range(start_x, end_x, 1):
        if (other_line > -sep_y/2 + offset and other_line < sep_y/2):
            vertex(i, other_line)
        other_line -= change_y
    endShape()
    
    
    strokeWeight(1)
    for p in points:
        trail_chance = .5
        for i in range(0, int(trail_count + random(-trail_count, trail_count))):
            stroke(15, 15, 15, 255 - i*(255/trail_count))
            if (random(1) < trail_chance):
                if (p[1] + i*trail_distance < sep_y/2 and p[1] + i*trail_distance > -sep_y/2 + offset):
                    circle(p[0], p[1] + i*trail_distance, 1)
                    trail_chance *= .95

def setup():
    size(w, h)
    pixelDensity(2)
    
    background('#F2E5CD')
    stroke(15)
    noFill()

    current_x = w/2.0 - grid_x_pixels/2.0 + sep_x
    current_y = h/2.0 - grid_y_pixels/2.0 + sep_y
    for i in range(grid_x - 2):
        for j in range(grid_y - 2):
            pushMatrix()
            translate(current_x, current_y)
            
            stroke(15)
            rect(-sep_x/2 + offset, -sep_y/2 + offset, sep_x - offset, sep_y - offset)
            draw_curvy()

            
            popMatrix()
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0 + sep_y
        current_x += sep_x
        
    save("Examples/" + str(int(random(10000))) + ".png")
