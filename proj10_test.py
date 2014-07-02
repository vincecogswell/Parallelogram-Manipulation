#################
#
# Proj 10 Test
#
#################

import proj10_quad

quad = proj10_quad.Quad

# A and B represent valid inputs that work normally
A = quad(5,10,50)
B = quad(10.2,15.8)
# C represents a variable that doesn't assign a 'DA' value
C = quad(AB = 30, A = 90)
# D represents an invalid input
D = quad(-5, 22, 194)
E = quad("this","is","invalid")

# Calculations for A
print("Evaluating A:" ,"\n", "\tprint A: " ,A)
print("\tis_valid: ", A.is_valid() )
print("\tis_rectangle: ", A.is_rectangle() )
print("\tis_rhombus: ", A.is_rhombus())
print("\tis_square: ", A.is_square())
print("\tsides: ", A.sides())
print("\tangles: ", A.angles())
print("\tperimeter: ", A.perimeter())
print("\tarea: ", A.area())
print("\tscale (by 3): ", A.scale(3), "\n")

# Calculations for B     
print("Evaluating B:" ,"\n", "\tprint B: " , B)
print("\tis_valid: ", B.is_valid() )
print("\tis_rectangle: ", B.is_rectangle() )
print("\tis_rhombus: ", B.is_rhombus())
print("\tis_square: ", B.is_square())
print("\tsides: ", B.sides())
print("\tangles: ", B.angles())
print("\tperimeter: ", B.perimeter())
print("\tarea: ", B.area())
print("\tscale (by 8): ", B.scale(8),"\n")

# Calculations for C
print("Evaluating C:" ,"\n", "\tprint C: " , C)
print("\tis_valid: ", C.is_valid() )
print("\tis_rectangle: ", C.is_rectangle() )
print("\tis_rhombus: ", C.is_rhombus())
print("\tis_square: ", C.is_square())
print("\tsides: ", C.sides())
print("\tangles: ", C.angles())
print("\tperimeter: ", C.perimeter())
print("\tarea: ", C.area())
print("\tscale (by 1.8): ", C.scale(1.8),"\n")

# Calculations for D
print("Evaluating D:" ,"\n", "\tprint D: " , D)
print("\tis_valid: ", D.is_valid() )
print("\tis_rectangle: ", D.is_rectangle() )
print("\tis_rhombus: ", D.is_rhombus())
print("\tis_square: ", D.is_square())
print("\tsides: ", D.sides())
print("\tangles: ", D.angles())
print("\tperimeter: ", D.perimeter())
print("\tarea: ", D.area())
print("\tscale (by 2.5): ", D.scale(2.5),"\n")

# Calculations for E
print("Evaluating E:" ,"\n", "\tprint E: " , E)
print("\tis_valid: ", E.is_valid() )
print("\tis_rectangle: ", E.is_rectangle() )
print("\tis_rhombus: ", E.is_rhombus())
print("\tis_square: ", E.is_square())
print("\tsides: ", E.sides())
print("\tangles: ", E.angles())
print("\tperimeter: ", E.perimeter())
print("\tarea: ", E.area())
print("\tscale (by 2.5): ", E.scale(2.5),"\n")

