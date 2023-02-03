'''
CLASSY BOATS
-----------------
Use the following Pseudocode to create this program:

1.) Create a class called Boat( )
2.) Use a constructor that sets two attributes: name and isDocked.
3.) The name should be entered as an argument when the object is created.
4.) The isDocked attribute is a Boolean variable. Set it to True.
5.) Add a method called dock( )
6.) In this method, if the boat is already docked print "(boat name) is already docked."
7.) If it is not docked, print "(boat name) is docking" and set the isDocked attribute to True.
8.) Add another method called undock( )
9.) In this method, if the boat is already undocked print "(boat name) is already undocked."
10.) If it is docked print "(boat name) is undocking" and set the isDocked attribute to False.
11.) Add another class called Submarine( ) that will inherit the Boat( ) class.
12.) In the Submarine( ) class create a method called submerge( ) that will print "(boat name) is submerging" 
if the boat is undocked and "(boat name) can't submerge" if the boat is docked.

Let's Float the Boat
--------------------
13.) Instantiate an object of the Submarine( ) class. Don't forget to pass in a name.
14.) Call the dock( ) method once
15.) Call the undock( ) method twice
16.) Call the dock( ) method two more times
17.) Call the submerge( ) method once
18.) Call the undock( ) method once
19.) Call the submerge( ) method a final time.

OUTPUT:
USS Hermon is already docked.
USS Hermon is undocking
USS Hermon is already undocked.
USS Hermon is docking
USS Hermon is already docked.
USS Hermon can't submerge!
USS Hermon is undocking
USS Hermon is submerging!
'''
class Boat():
    def __init__(self, name):
        self.name = name
        self.isdocked = True
    def dock(self):
        if self.isdocked == True:
            print(self.name,"is already docked.")
        else:
            print(self.name,"is docking.")
            self.isdocked = True
    def undock(self):
        if self.isdocked == False:
            print(self.name,"is already undocked.")
        else:
            print(self.name,"is undocking.")
            self.isdocked = False
class Submarine(Boat):
    def submerge(self):
        if self.isdocked == True:
            print(self.name,"can't submerge.")
        else:
            print(self.name,"is submerging.")

def main():
    uss = Submarine("USS Hermon")
    uss.dock()
    uss.undock()
    uss.undock()
    uss.dock()
    uss.dock()
    uss.submerge()
    uss.undock()
    uss.submerge()


if __name__ =="__main__":
    main()
