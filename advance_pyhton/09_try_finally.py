def show(a, b):
    try:
        return a/b
    except TypeError:
        print("Please enter a number!")
    except ZeroDivisionError:
        return f"divison by zero is not allowed in python"
    except Exception as e:
        return e
    # finally is always executes if there is an exception or not 
    # but mainly requred in functions to exceutes after returning any value 
    finally:
        print("Now this exception is completed!")

print(show(5, "d"))