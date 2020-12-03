
def is_italic(angle,catop,start_x,start_y):
    angle_deegres = 5
    angle_rad = radians(angle_deegres)
    cat_adj = tan(angle_rad) * catop
    
    stroke(0)
    line((start_x, start_y), (start_x + cat_adj, start_y + catop ))

for i in range(20):
    is_italic(angle, paper_size, repetitions+space, 0)