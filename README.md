# Vigil

https://github.com/munificent/vigil but as a python package

To quote the above, "Vigil is truly vigilant about not allowing code that fails to pass programmatic specifications."

### Implore

Functions can state the oaths they promise to uphold via ```vigil.implore```: 

``` python
import math
import vigil

# The 0th argument to sqrt must always be greater than or equal to zero. 
@vigil.implore(">=", 0, 0)
def sqrt(x):
    return math.sqrt(x)
```

If a caller fails to meet the requirement, a ```VigilError``` will be thrown and the caller will be punished as defined in the ```vigil.conf```. 

### Swear

Functions can state the oaths they promise to uphold via ```vigil.swear```: 

``` python
import math
import vigil

@vigil.swear(">=", 0)
def sqr(x):
    return x*x
```

If a function fails to meet its oath, a ```VigilError``` will be thrown and the function will be punished as defined in the ```vigil.conf```. 

### Punishment

The punishment for misbehaving functions is defined in a ```vigil.conf```. vigil.conf can either say ```deleteFunctions = False``` or ```deleteFunctions = True```. 

### [FAQ](https://github.com/munificent/vigil)

#### Is this serious?

Eternal moral vigilance is no laughing matter.

#### But isn't a language that deletes code crazy?

No, wanting to keep code that demonstrably has bugs according to its own specifications is crazy. What good could it possibly serve? It is corrupted and must be cleansed from your codebase.

Vigil will do this for you automatically.

#### Vigil deleted a function. Won't that cause the functions that call it to fail?

It would seem that those functions appear to be corrupted as well. Run Vigil again and it will take care of that for you. Several invocations may be required to fully excise all bugs from your code.
