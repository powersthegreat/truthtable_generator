'''
Author: William Powers
KUID: 3023462
Due Date: 9/1/2022
Assignment: 01
Last modified: 8/26/2022
File Purpose: 
A object based truth table generator that takes in a set of 
variables and their corresponding logical equations then outputs
a cleanly formatted truth table. 

Input syntax for created objects as follows:
- variables should be 'p', 'q', or 'r'
- only up to three variables (don't know how to scale this part)
- for OR operator use '+'
- for AND operator use '*'
- for NOT operator use '(not var)'
- for 'p->q' input as '(not p) + q
- for 'p<->q' input as '(p * q) + ((not p) * (not q))
'''

class TruthTable:
    def __init__(self):
        '''
        Setting up initial class variables including a table(two dimensinoal array),
        variables(p, q, and r in that order), equations(break down of main equation),
        and titles(concatenation of variables and equations used for printing).
        '''
        self.table = None
        self.variables = None
        self.equations = None
        self.titles = None
    
    def create_table(self):
        '''
        Creates table(two dimensional array) or size dependig on number of variables
        and number of broken down equations.
        '''
        #rows is proportional to 2 to the power of the number of variables being used
        rows = 2**len(self.variables)
        #concatenating titles to be used in printing
        titles = self.variables + self.equations
        #setting titles as class variable titles
        self.titles = titles
        #columns set as length of titles
        columns = len(self.titles)
        #looping through number of columns and number of rows to create table of size rowXcolumns
        table = []
        for i in range(0, rows):
            mini = []
            for j in range(0, columns):
                mini.append(0)
            table.append(mini)
            mini = []
        #setting table as class variable table
        self.table = table

    def print_table(self):
        '''
        Prints out titles class variable then prints each row of the table class variable
        row by row. 'Print_table_clean' is a more effiecent way of veiwing the table, yet
        this method is useful for testing purposes.
        '''
        print(self.titles)
        for row in self.table:
            print(row)

    def print_table_clean(self):
        '''
        Creates and concatenates to a single string to be printed out representing the full table.
        '''
        row_str = ""
        #adds each title as a string to the row_str representing the string verison of the full table
        for title in self.titles:
            row_str += str(title)
            #adds a three spaces for cleaner printout
            row_str += "   "
        #moves to new row to begin concatenating rows of table
        row_str += "\n"
        #adds each value of each row to row_str
        for row in self.table:
            for col in row:
                row_str += str(col)
                #tab added for cleaner printout
                row_str += "\t"
            #moves to new line once each row is fully concatenated
            row_str += "\n"
        #prints out string formatted table
        print(row_str)
        #returns string formatted table for further use
        return row_str
    
    def fill_table_variables(self):
        '''
        Fills each variable column of the table with its corresponding initial truth value. This method
        is not scalable as it is the reason three variables is the max this class can take.
        '''
        #if one variable was inputed adds true and false in corresponding position in that variables column
        #does this statically
        if len(self.variables) == 1:
            self.table[0][0] = True
            self.table[1][0] = False

        #if two variables were inputted adds true and false in corresponding position for each variables column
        #does this statically
        elif len(self.variables) == 2:
            for i in range(0,2):
                self.table[i][0] = True
                self.table[i][1] = True
            for i in range(2,4):
                self.table[i][0] = False
                self.table[i][1] = True
            self.table[1][1] = False
            self.table[3][1] = False

        #if three variables were inputted adds true and false in corresponding position for each variables column
        #does this statically
        elif len(self.variables) == 3:
            for i in range(0, 4):
                self.table[i][0] = True
                self.table[i][1] = True
                self.table[i][2] = True
            for i in range(4, 8):
                self.table[i][0] = False
                self.table[i][1] = True
                self.table[i][2] = True
            for i in range(2,4):
                self.table[i][1] = False
            for i in range(6,8):
                self.table[i][1] = False
            self.table[1][2] = False
            self.table[3][2] = False
            self.table[5][2] = False
            self.table[7][2] = False
            
    def solve_table(self):
        '''
        For each equation column, goes through and fills in the equivalent boolean value referencing
        the variables in that row. This is done by first establishing which variables are which in
        the given row, and then using python's built in eval() method to convert the columns title
        equation, into an object that can be used. The table class variable is returned at the end.
        '''
        #looping through each row
        for i in range(len(self.table)):
            #determining where the variable columns end and the equation columns begin
            eq_start = len(self.table[0]) - len(self.equations)
            eq_end = len(self.table[0])
            #looping through the above columns for each row
            for j in range(eq_start, eq_end):
                #setting up which values in the row being looked at to use as what variable
                #does this statically
                #if three variables, p, q, and r are defined at position...
                if len(self.variables) == 3:
                    p = self.table[i][0]
                    q = self.table[i][1]
                    r = self.table[i][2]
                #if two variables, p and q are defined at position...
                elif len(self.variables) == 2:
                    p = self.table[i][0]
                    q = self.table[i][1]
                #if one variable, p is defined at position...
                elif len(self.variables) == 1:
                    p = self.table[i][0]

                #the title of the column being looked at is converted from a string to an
                #object by use of the built in eval() function, this then uses the previously
                #defined variables to provide a numerical boolean answer
                answer_logic = eval(self.titles[j])

                #true is evaluated as 1 in python therefore the answer_logic could become greater
                #than one at time (ex. True + True + True = 3) therefore if the answer_logic is 
                #any number of one or greater the current table position is set as 'True'
                if answer_logic >= 1 or answer_logic == True:
                    self.table[i][j] = True
                #false is evaluated as 0 in python therefore if answer_logic is any number less than
                #1 the current table position is set to 'False'
                else:
                    self.table[i][j] = False
        #table is returned for further use
        return self.table
            

'''
Declaring objects for each of the truth table problems that were assigned. Then, in the following
order, assigning their variables, equations, creating their table, filling their table with initial
boolean values, solving the rest of the table, and finally printing out the table in a clean
string format.
'''
#setting up object for demorgan's law one (problem 1)
print("demorgan_law_1")
demorgan_law_one = TruthTable()
demorgan_law_one.variables = ["p", "q"]
demorgan_law_one.equations = ["not p", "not q", "p*q", "not (p*q)", "(not p)+(not q)"]
#creating table and filling initial boolean values for demorgan's law one
demorgan_law_one.create_table()
demorgan_law_one.fill_table_variables()
#solving table for demorgan's law one
demorgan_law_one.solve_table()
#printing table for demorgan's law one
demorgan_law_one.print_table_clean()
print("\n\n")

#setting up object for demorgan's law two (problem 2)
print("demorgan_law_2")
demorgan_law_two = TruthTable()
demorgan_law_two.variables = ["p", "q"]
demorgan_law_two.equations = ["not p", "not q", "p+q", "not (p+q)", "(not p)*(not q)"]
#creating table and filling initial boolean values for demorgan's law two
demorgan_law_two.create_table()
demorgan_law_two.fill_table_variables()
#solving table for demorgan's law two
demorgan_law_two.solve_table()
#printing table for demorgan's law two
demorgan_law_two.print_table_clean()
print("\n\n")

#setting up object for associative law 1 (problem 3)
print("associative_law_1")
associative_law_1 = TruthTable()
associative_law_1.variables = ["p", "q", "r"]
associative_law_1.equations = ["p*q", "q*r", "(p*q)*r", "p*(p*r)"]
#creating table and filling initial boolean values for associatitve law 1
associative_law_1.create_table()
associative_law_1.fill_table_variables()
#solving table for associative law 1
associative_law_1.solve_table()
#printing table for associative law 1
associative_law_1.print_table_clean()
print("\n\n")

#setting up object for associative law 2 (problem 4)
print("associative_law_2")
associative_law_2 = TruthTable()
associative_law_2.variables = ["p", "q", "r"]
associative_law_2.equations = ["p+q", "q+r", "(p+q)+r", "p+(p+r)"]
#creating table and filling initial boolean values for associatitve law 2
associative_law_2.create_table()
associative_law_2.fill_table_variables()
#solving table for associative law 2
associative_law_2.solve_table()
#printing table for associative law 2
associative_law_2.print_table_clean()
print("\n\n")

#setting up object for problem number 5 (problem 5)
print("num_five_equation")
num_five_equation = TruthTable()
num_five_equation.variables = ["p", "q", "r"]
num_five_equation.equations = ["p+q", "(not p)+r", "(not q)+r", "(p+q) *((not p)+r)", "((not p)+r) * ((not q)+r)", "(p+q)*((not p)+r) * ((not q)+r)", "(not (p+q)*((not p)+r) * ((not q)+r)) + r", "True"]
#creating table and filling initial boolean values for problem number 5
num_five_equation.create_table()
num_five_equation.fill_table_variables()
#solving table for problem number 5
num_five_equation.solve_table()
#printing table for problem number 5
num_five_equation.print_table_clean()
print("\n\n")

#setting up object for problem number 6 (problem 6)
print("num_six_equation")
num_six_equation = TruthTable()
num_six_equation.variables = ["p", "q"]
num_six_equation.equations = ["not p", " not q", "p*q", "(not p)+q", "(not q)+p","(not p) * (not q)", "(p*q) + ((not p) * (not q))", "((not p)+q) * ((not q)+p)"]
#creating table and filling initial boolean values for problem number 6
num_six_equation.create_table()
num_six_equation.fill_table_variables()
#solving for problem number 6
num_six_equation.solve_table()
#printing for problem number 6
num_six_equation.print_table_clean()
print("\n\n")


