# match case is like switch case in c language 

def check(status:int):
    match status:
        case 200:
            return "Error!"
        case 404:
            return "page does not exist!"
        case _:
            return "you entered wrong status!"

print(check(500))