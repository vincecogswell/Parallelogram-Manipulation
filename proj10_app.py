#######################
#
# Proj 10 Application
#
#######################

import proj10_quad

quad = proj10_quad.Quad
try:
    in_file = open( "quad_input.txt" , "r")
    
    count = 0
    valid = 0
    avg_p = 0
    avg_a = 0
    max_p = 0
    max_a = 0
    
    for line in in_file:
        count += 1
        split = line.split(',')
        x = float(split[0])
        y = float(split[1])
        z = float(split[2])
        
        print("Line", count, ":", line)

        if quad(x,y,z).is_valid() == True:
            valid += 1
            print("Sides:" ,quad(x,y,z).sides())
            print("Angles:",quad(x,y,z).angles())
            print("Perimeter:",quad(x,y,z).perimeter())
            print("Area:",quad(x,y,z).area(),"\n")
            avg_p += quad(x,y,z).perimeter()
            avg_a += quad(x,y,z).area()

            if quad(x,y,z).perimeter() > max_p:
                max_p = quad(x,y,z).perimeter()
                max_parallel = line
                max_parallel_area = quad(x,y,z).area()

            if quad(x,y,z).area() > max_a:
                max_a = quad(x,y,z).area()
                max_parallel_2 = line
                max_perimeter = quad(x,y,z).perimeter()
        else:
            print("Not a valid parallelogram\n")

    print("-"*15)
    print("Final Summary")
    print("-"*15)
    print("Lines processed:", count)
    print("Valid parallelograms:", valid)
    print("Average area:", (avg_a / valid))
    print("Average perimeter:", (avg_p / valid),"\n")
    print("Parallelogram with largest perimeter:", max_parallel)
    print("\tPerimeter:",max_p)
    print("\tArea:",max_parallel_area,"\n")
    print("Parallelogram with largest area:", max_parallel_2)
    print("\tPerimeter:", max_perimeter)
    print("\tArea:", max_a)
            
        
    
except IOError:
    print("\n\t***quad_input.txt file not found***")
    
