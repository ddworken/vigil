import vigil
import math

@vigil.swear(">=", 1)
def sqr(x):
    return x*x

def main():
    print("When swears are not violated, everything works fine. ")
    print("sqr(2): ")
    print(sqr(2))
    print("But when they are violated...")
    print("sqr(0.1): ")
    print(sqr(0.1))

if __name__ == "__main__":
    main()
