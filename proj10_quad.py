
import math

################################################################################
## Class Quad
################################################################################

class Quad( object ):
    
    def __init__( self, AB=None, DA=None, A=None ):
        """
        Initialize an object of type Quad.
        """
        
        self.__sideAB = AB
        if DA == None: #if the DA value wasn't entered, then use side AB
            self.__sideDA = AB
        else:
            self.__sideDA = DA

        if A == None:
            A = 90
       
        self.__angleA = A
        self.__valid = self.__validate()

        
    def __validate( self ):
        """
         Determine if a Quad is valid.
        """

        valid = False

        try:
            AB = self.__sideAB
            DA = self.__sideDA
            A = self.__angleA

            if AB > 0 and DA > 0 and A > 0 and A < 180:
                valid = True

        except TypeError:
            pass

        return valid
        
        
    
    def __repr__( self ):
        """
        Return a string (the representation of a Quad).
        """
        try:
            out_str = "[{:3.1f},{:3.1f},{:3.1f},{:3.1f}]" \
                .format( self.__sideAB, self.__sideDA, self.__sideAB, self.__sideDA )
            
        except ValueError:
            out_str = "[{:3.1s},{:3.1s},{:3.1s},{:3.1s}]" \
                .format( self.__sideAB, self.__sideDA, self.__sideAB, self.__sideDA )          

        return out_str


        
    def __str__( self ):
        """
        Return a string (the representation of a Quad).
        """
        try:
            out_str = "[{:4.1f},{:4.1f},{:4.1f},{:4.1f}]" \
                .format( self.__sideAB, self.__sideDA, self.__sideAB, self.__sideDA )
            
        except ValueError:
            out_str = "[{:4.1s},{:4.1s},{:4.1s},{:4.1s}]" \
                .format( self.__sideAB, self.__sideDA, self.__sideAB, self.__sideDA )
        
        return out_str

    def is_valid( self ):
        """
        Return a Boolean (is the Quad valid?).
        """

        return self.__valid

    def is_rectangle( self ):
        """
        Return a Boolean (is the Quad a rectangle?)
        """
        
        rect = False

        if self.__angleA == 90:
            rect = True
            
        return rect

    def is_rhombus( self ):
        """
        Return a Boolean (is the Quad a rhombus?)
        """
    
        rhom = False

        if self.__sideAB == self.__sideDA:
            rhom = True

        return rhom

    def is_square( self ):
        """
        Return a Boolean (is the Quad a square)?
        """
        
        sq = False

        if self.__angleA == 90 and self.__sideAB == self.__sideDA:
            sq = True

        return sq

    def sides( self ):
        """
        Return a tuple containing the Quad's four sides.
        """
    
        sides = []

        sides.append(self.__sideAB)
        sides.append(self.__sideDA)
        sides.append(self.__sideAB)
        sides.append(self.__sideDA)

        return tuple(sides)
    
    def angles( self ):
        """
        Return a tuple containing the Quad's four angles (in degrees) 
        """

        angles = []
        
        if self.is_valid() == True:
            ang_1 = self.__angleA
            ang_2 = 180 - self.__angleA
            ang_3 = self.__angleA
            ang_4 = 180 - self.__angleA

            angles.append(float(round(ang_1,1)))
            angles.append(float(round(ang_2,1)))
            angles.append(float(round(ang_3,1)))
            angles.append(float(round(ang_4,1)))

            return tuple(angles)
        
        elif angles == []:
            angles.append(None)
            angles.append(None)
            angles.append(None)
            angles.append(None)

            return tuple(angles)
        
    def perimeter( self ):
        """
        Return a float representing the Quad's perimeter.
        """

        perimeter = 0

        if self.is_valid() == True:
            perimeter = (2*self.__sideAB)+(2*self.__sideDA)

        return perimeter
    
    def area( self ):
        """
        Return a float representing the Quad's area.
        """

        area = 0
        
        if self.is_valid() == True:
            b = self.__sideAB
            h = (math.sin(math.radians(self.__angleA)))*(self.__sideDA)
            area = b*h
            
        return area

    def scale( self, factor=1.0 ):
        """
        Scale all four of a Quad's sides by the same factor.
        """

        sides = []
        
        if factor > 0 and self.is_valid() == True:
            AB = (self.__sideAB*factor)
            DA = (self.__sideDA*factor)
            sides.append(AB)
            sides.append(DA)
            sides.append(AB)
            sides.append(DA)
            
            return sides

        if sides == []:
            sides.append(self.__sideAB)
            sides.append(self.__sideDA)
            sides.append(self.__sideAB)
            sides.append(self.__sideDA)

            return sides
        

