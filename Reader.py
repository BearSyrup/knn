class Reader:

    def read_csv(self, path):
        try:
            with open(path,"r") as file:       
                buffer = [x.rstrip().split(",") for x in file.readlines()]
                return buffer
        except:
            print("Hilston we have a problem")
        



csv = Reader()
buff = csv.read_csv("document.csv")
print(buff)