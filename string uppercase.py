class IOString():
    def __init__(self):
        self.str1 = ""
    
    def get_string(self):
        self.str1 = input("Enter string : ")
    
    def print_String(self):
        print("Result is: ", self.str1.upper())
strObj = IOString()

strObj.get_string()
strObj.print_String()