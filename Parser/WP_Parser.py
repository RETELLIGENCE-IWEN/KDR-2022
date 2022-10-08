


# Final Struct Data
class WP_Struct:

    def __init__(self, isWP, _values):
        
        self.X = _values[0]
        self.Z = _values[1]
        self.Y = _values[2]
        self.Xoff = _values[3]
        self.Yoff = _values[4]
        self.Zoff = _values[5]

        if not isWP:
            self.XR = _values[6]
            self.YR = _values[7]
            self.ZR = _values[8]



# Parser
class WP_Data:

    def __init__(self, NameOfFile, Prefix):

        self.IsFileOpen = False

        try:
            if Prefix: self.File = open(Prefix+NameOfFile, 'r') 
            else:      self.File = open(NameOfFile, 'r') 

            self.Data = self.File.readlines()
            self.IsFileOpen = True
        except: pass


    
    # Read Data and return in the form of WP_Struct
    def ReadData(self, index, types):

        if self.IsFileOpen:

            try:

                CallName = types + "[" + str(index) + "]"

                matching = [_[:-1] for _ in self.Data if CallName in _]

                Values = [_.split("=")[1] for _ in matching]

                struct = WP_Struct(types=="WP", Values)

                return struct

            except: return False
        else: return False



    def Terminate(self): self.File.close()






if __name__ == "__main__":
    # Example Useage ####################################################

    # My = WP_Data("C:/Users/ailish7/Documents/AirSim/WayPoints.txt", None)
    My = WP_Data("WayPoints.txt", None)


    if My.IsFileOpen: Got_WP = My.ReadData(4,"WP")

    if Got_WP:
        print(Got_WP.X)
        print(Got_WP.Y)
        print(Got_WP.Z)
        print(Got_WP.Xoff)
        print(Got_WP.Zoff)
        print(Got_WP.Yoff, "\n")


    if My.IsFileOpen: Got_PS = My.ReadData(0,"PS")

    if Got_PS:
        print(Got_PS.X)
        print(Got_PS.Y)
        print(Got_PS.Z)
        print(Got_PS.Xoff)
        print(Got_PS.Zoff)
        print(Got_PS.Yoff)
        print(Got_PS.XR) # not in use
        print(Got_PS.YR) # not in use
        print(Got_PS.ZR, "\n")