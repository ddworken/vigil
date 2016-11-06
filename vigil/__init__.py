import operator
import inspect

class VigilError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class swear(object):
    # An array of hardcoded operator to function conversions
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '==': operator.eq}

    def __init__(self, func, expectedOut):
        self.func = func
        self.expectedOut = expectedOut

    def __call__(self, f):
        def wrapped_f(*args):
            # Use inspect to grab the name of the file that contained the function
            callerFilename = inspect.stack()[1][1]
            try:
                out = f(*args)
            except:
                out = None
            # Convert a string to a function using the above table
            if str(type(self.func)) == "<type 'str'>" or str(type(self.func)) == "<class 'str'>":
                self.func = self.ops[self.func]
            if self.func(out, self.expectedOut) == False:
                raise VigilError("Swear Failed!")
                if delete:
                    deleteFunction(callerFilename, f.func_name) 
            return out
        return wrapped_f

class implore(object):
    # An array of hardcoded operator to function conversions
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '==': operator.eq}

    def __init__(self, func, argIndex, arg2):
        self.func = func
        self.argIndex = argIndex
        self.arg2 = arg2

    def __call__(self, f):
        def wrapped_f(*args):
            # Use inspect to grab the name of the function that called it
            # and the file it is in
            caller = inspect.stack()[1][3]
            callerFilename = inspect.stack()[1][1]
            # Convert any strings into functions
            if str(type(self.func)) == "<type 'str'>" or str(type(self.func)) == "<class 'str'>":
                self.func = self.ops[self.func]
            if self.func(args[self.argIndex], self.arg2) == False:
                if delete:
                    deleteFunction(callerFilename, caller)
                raise VigilError("Implore broken by " + caller + " in " + callerFilename)
            return f(*args)
        return wrapped_f

def deleteFunction(filename, functionName):
    """ String, String -> None
        Deletes the specified function in the specified file"""
    def getIndentationLevel(line):
        """ Returns the indentation level of the specified line measured
            in number of spaces. """
        indentedLength = len(line.replace("\t", "    "))
        unindentedLength = len(line.replace("\t", "    "))
        return unindentedLength - indentedLength
    
    with open(filename) as f:
        program = f.read().splitlines()
    indexStart = -1
    for index,line in enumerate(program):
        if "def " + functionName in line:
            indexStart = index
            break
    if indexStart == -1:
        print("Function definition not found!")
        return
    initIndentationLevel = getIndentationLevel(program[indexStart])
    # Find the next line that is at the same indentation level
    for index,line in enumerate(program[indexStart]):
        indentationLevel = getIndentationLevel(line)
        if indentationLevel == initIndentationLevel:
            indexEnd = indexStart + index
    # Remove the function
    program = program[:indexStart] + program[indexEnd:]
    # Write to a file
    with open(filename+"modded", "w") as f:
        f.write("\n".join(program))

try:
    with open("vigil.conf") as f:
        delete = f.read().split("=")[1].strip() == True
except:
    # If vigil.conf doesn't exist, then default to not deleting anything
    delete = False
        
def main():
    import sys

    @implore('==', 0, 42)
    @swear('==', 85)
    def restrictedAdd1(a1, a2):
        return a1+a2
    def equal(a1, a2):
        return a1==a2
    @implore(equal, 0, 42)
    @swear(equal, 85)
    def restrictedAdd2(a1, a2):
        return a1+a2

    def exceptionHandler(exception_type, exception, traceback):
        print(str(exception_type.__name__) + ": " + str(exception))
    sys.excepthook = exceptionHandler

    print(restrictedAdd1(42,43))
    print("+++++++++++++++++++")
    print(restrictedAdd1(42, 42))
    print("===================")
    print(restrictedAdd2(42,43))
    print("+++++++++++++++++++")
    print(restrictedAdd2(41, 42))


if __name__ == "__main__":
    main()

