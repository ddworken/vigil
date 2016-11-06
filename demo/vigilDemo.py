import vigil
import math

@vigil.implore(">=", 0, 0)
@vigil.swear(">=", 0)
def sqrt(x):
    return math.sqrt(x)

def main():
    print("sqrt(2): ")
    print(sqrt(2))
    print("++++++++++++++++++++++++")
    print("sqrt(-2): ")
    print(sqrt(-2))
    
if __name__ == "__main__":
    main()
