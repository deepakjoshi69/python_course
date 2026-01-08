# map function takes two argument a function and where the function implement

l = [1,2,3,4,5,7]

def square(n):
    return n*n

square_list = map(square, l)

print(list(square_list))