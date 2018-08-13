# we create the issue
# and test it with the error handling


'''try:
    m = input("enter marks: ")
    marks = m + 50
    print(marks)

except:
    print("Please enter an integer value")

else:
    # if try is success, this statement are executed
    print("success")

finally:
    # this statement executes in both success and error
    print("this is finally")'''

class MyError(Exception):
    '''
        parent class for the exception
    '''
    pass

class ZeroError(MyError):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    # repr = return the canonical string representation of the object.

try:
    num = int(input("enter the number"))
    if (num < 1):
        raise ZeroError("Number cannot be zero")
except ZeroError as e:
    print("Error raised: ", e.data)
    