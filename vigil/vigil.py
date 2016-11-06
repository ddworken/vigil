import operator
import inspect

class VigilError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class swear(object):
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
            callerFilename = inspect.stack()[1][1]
            if str(type(self.func)) == "str":
                self.func = ops[self.func]
            try:
                out = f(*args)
            except:
                out = None
            if str(type(self.func)) == "<type 'str'>" or str(type(self.func)) == "<class 'str'>":
                self.func = self.ops[self.func]
            if self.func(out, self.expectedOut) == False:
                raise VigilError("Swear Failed!")
                if delete:
                    deleteFunction(callerFilename, f.func_name) 
            return out
        return wrapped_f

class implore(object):
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
            caller = inspect.stack()[1][3]
            callerFilename = inspect.stack()[1][1]
            if str(type(self.func)) == "<type 'str'>" or str(type(self.func)) == "<class 'str'>":
                self.func = self.ops[self.func]
            if self.func(args[self.argIndex], self.arg2) == False:
                if delete:
                    deleteFunction(callerFilename, caller)
                raise VigilError("Implore broken by " + caller + " in " + callerFilename)
            return f(*args)
        return wrapped_f

def deleteFunction(filename, functionName):
    def getIndentationLevel(line):
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
    for index,line in enumerate(program[indexStart]):
        indentationLevel = getIndentationLevel(line)
        if indentationLevel == initIndentationLevel:
            indexEnd = indexStart + index
    program = program[:indexStart] + program[indexEnd:]
    with open(filename+"modded", "w") as f:
        f.write("\n".join(program))
    
with open("vigil.conf") as f:
    delete = f.read().split("=")[1].strip() == True

def equal(a1, a2):
    return a1==a2

@implore('==', 0, 42)
@swear('==', 85)
def restrictedAdd1(a1, a2):
    return a1+a2

@implore(equal, 0, 42)
@swear(equal, 85)
def restrictedAdd2(a1, a2):
    return a1+a2

def main():
    import sys
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

