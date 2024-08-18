import math

class IO():
    def getStr(self):
        return input().strip()
    
    def getInt(self):
        return int(input().strip())
    
    def getStrList(self):
        return self.getStr().split(' ')
    
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    
    def strTuple(self, tuple):
        return "%s %s" % tuple
    
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()

"""
Input
Input consists of up to 25 Snaggle expressions, one per line, followed by a line
containing (), which should not be processed.
Integers are sequences of at most 10 digits, optionally preceded by ‘-’.
Real numbers are in standard floating point format (i.e. not E format) without a
sign.
Snaggle expressions of the form (p e1 e2
) have a single space separating the
three elements and no spaces elsewhere.
Snaggle expressions are at most 300 characters in length.
Expected value
The expected value of a random variable is the weighted average over all possible
outcomes. For example, if a variable has the value n1 with some probability p and
the value n2
 otherwise, the expected value is p × n1 + (1 – p) × n2
.
Output
Output is a single line for each Snaggle expression in the input giving the expected
value of the expression to two decimal places.

"""

def problem():

    def parse(expression):
        temp = ""
        output = []
        for ch in expression:
            if ch == '(':
                continue
            elif ch == ')':
                output.append(temp)
                temp = ")"
            elif ch == ' ':
                output.append(temp)
                temp = ""
            else:
                temp += ch

        output.append(temp)
        def toFloat(a):
            try: 
                res = float(a)
                return res
            except ValueError: return a

        return [toFloat(a) for a in output]

    def expected(p, e1, e2):
        return p * e1 + (1 - p) * e2
    while True:
        line = io.getStr()
        if line == "()": break

        tokens = parse(line)
        stack = []
        # 
        for token in tokens:

            if token == ")":
                # pop
                e2 = stack.pop()
                e1 = stack.pop()
                p = stack.pop()

                stack.append(expected(p, e1 + e2, e1 - e2))
            else:
                stack.append(token)

        print("%.2f" % stack[0])

problem()
#