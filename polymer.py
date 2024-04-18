import csv 
class FileReader:
    def __init__(self):
        self.accumulator = []
        self.places = []
        self.Headlines  = []
        self.Description = []
        self.colourCategory = []
        self.lattitude   = []
        self.longitude = []
        self.feed = {"places":self.places , "Headlines":self.Headlines,"Description":self.Description,"colourCategory":self.colourCategory,"lattitude":self.lattitude,"longitude":self.longitude}
    
    def csvRead(self):
         
            with open('news.csv', mode ='r')as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    self.accumulator.append(lines)
            for items in self.accumulator:
                 self.feed["places"].append(items[0])
                 self.feed["Headlines"].append(items[1])
                 self.feed["Description"].append(items[2])
                 self.feed["colourCategory"].append(items[3])
                 self.feed["lattitude"].append(items[4])
                 self.feed["longitude"].append(items[5])

                
                      
         
    def newsReadfromSystem(self):
         FileReader().csvRead()
         print(self.feed)
    def newswriteinsystem(self):
         pass

Filereading = FileReader()
Filereading.csvRead()
Filereading.newsReadfromSystem()















































































