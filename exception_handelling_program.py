#Write One Exception Handling program


def exceptionHandellingProgram():
    
    try:
        a = 10
        b = 0
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("Divide by zero error")
    except Exception as e:
        print("Some other error", e)
    finally:
        print("Finally block is always executed")

exceptionHandellingProgram()