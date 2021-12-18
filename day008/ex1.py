test_h = int(input("Height of wall: \n"))
test_w = int(input("Width of wall: \n"))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    cans = round(area / cover)
    print(f'You will need {cans} cans of paint')

paint_calc(height = test_h, width = test_w, cover = coverage)