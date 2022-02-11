w, h = 1000, 1000

colors_list = [[(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)],
          [(230, 57, 70), (241, 250, 238), (29, 53, 87)],
          [(183, 183, 164), (221, 190, 169), (107, 112, 92), (203, 153, 126)],
          [(212, 224, 155), (246, 244, 210), (203, 223, 189), (241, 156, 121), (164, 74, 63)]] 

colors = []

cube_size = random(4,15)
fill_deform = random(2,12)
outline_deform = random(2,12)

border_size = 40


def get_random_element(l):
    return l[int(random(len(l)))]

def draw_border():
    noStroke()
    fill(252, 245, 229)
    
    rect(0, 0, w, border_size)
    rect(0, 0, border_size, h)
    rect(w - border_size, 0, border_size, h)
    rect(0, h - border_size, w, border_size) 
    stroke(0)
    strokeWeight(2)
    noFill()
    rect(border_size, border_size, w - border_size * 2, h - border_size * 2)
    

# Center of the quad, size, deform strength,outline, fill color
def draw_rect(x, y, x_s, y_s, d, o, f):

    stroke(*o)
    fill(*f)
    strokeJoin(ROUND)
    beginShape()
    
    vertex(x - x_s - random(-d, d), y - y_s - random(-d, d))
    vertex(x + x_s - random(-d, d), y - y_s - random(-d, d))
    vertex(x + x_s - random(-d, d), y + y_s - random(-d, d))
    vertex(x - x_s - random(-d, d), y + y_s - random(-d, d))
    
    endShape(CLOSE)
    
    
def setup():
    size(w, h)
    randomSeed(int(random(10010)))
    pixelDensity(2)
    colors = get_random_element(colors_list)
    # colors = colors_list[4]
    background(252, 245, 229)
    # background(*get_random_element(colors))
    
    
    strokeWeight(2)
    for r in range(30):
        draw_cube_layer(5, get_random_element(colors))
    draw_border()
    
    # Go Outside the border
    if (random(1) < .9):
        for r in range(7):
            draw_cube_layer(5, get_random_element(colors))
    # save('Examples/Great/' + str(int(random(10000))) + '.png')
    
def draw_cube_layer(o, layer_color):
    first_cube = [random(0, h), random(0, 1000)]
    
    cubes = []
    choose_cubes = []
    drawing_cubes = []
    
    cubes.append(first_cube)
    drawing_cubes.append(first_cube)
    choose_cubes.append(first_cube)
    
    for j in range(2000):
        c = cubes[int(random(len(cubes)))]
        
        next_cube = c[:]
        if (random(1) < .5):
            if (random(1) < .5):
                next_cube[0] += cube_size
                next_cube[1] -= cube_size*2
            else:
                next_cube[0] -= cube_size
                next_cube[1] -= cube_size*2
        else:
            if (random(1) < .5):
                next_cube[0] += cube_size
                next_cube[1] += cube_size*2
            else:
                next_cube[0] -= cube_size
                next_cube[1] += cube_size*2
            
        if ((next_cube in drawing_cubes) == False):
            cubes.append(next_cube)
            choose_cubes.append(next_cube)
            drawing_cubes.append(next_cube)
            
            # Symmetry mode?
            if (random(1) < 0):
                sym_cube = next_cube[:]
                sym_cube[0] += (w/2 - next_cube[0])*2
                
                cubes.append(sym_cube)
                choose_cubes.append(sym_cube)
            
                drawing_cubes.append(sym_cube)
                
        if j%2 == 0 and len(cubes) > 3:
            cubes.pop(0)
    
    drawing = True
    for c in drawing_cubes:
        if (drawing == True):
            draw_rect(c[0], c[1], cube_size, cube_size, fill_deform, (0, 0, 0, 0), layer_color)
            draw_rect(c[0], c[1], cube_size, cube_size, outline_deform, (0, 0, 0, 255), (0, 0, 0, 0))
        if (random(1) < .06):
            drawing = False
        
        if (drawing == False and random(1) < .1):
            drawing = True
        
