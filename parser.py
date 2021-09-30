import csv, collections, sys

class data_dump:

    file_name = ""
    max_lines = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.max_lines = self.get_max_lines(file_name)

    @staticmethod
    def get_max_lines(file_name):
        count = 0
        for row in open(file_name):
            count += 1
        return count


    def get_averages(self, LanguageGroup, WordType):
        with open(self.file_name, newline='') as csvfile:

            reader = csv.DictReader(csvfile)

            # plz somebody tell me there is a better way to do this in Python
            npFullTime = 0
            npRedTime = 0
            npFullCount = 0
            npRedCount = 0
            SRedTime = 0
            SRedCount = 0
            SFullTime = 0
            SFullCount = 0

            for x in range(self.max_lines-1):
                read_line = reader.__next__()

                if read_line["LanguageGroup"] == LanguageGroup and read_line["WordType"] == WordType:
                    #verb type: NP-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Full":
                        npFullTime += int(read_line["ReadingTime"])
                        npFullCount += 1
    
                    #verb type: NP-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Reduced":
                        npRedTime += int(read_line["ReadingTime"])
                        npRedCount += 1

                    #verb type: S-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Full":
                        SFullTime += int(read_line["ReadingTime"])
                        SFullCount += 1

                    #verb type: S-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Reduced":
                        SRedTime += int(read_line["ReadingTime"])
                        SRedCount += 1
                
        npFullAvg = npFullTime / npFullCount
        npRedAvg = npRedTime / npRedCount
        SRedAvg = SRedTime / SRedCount
        SFullAvg = SFullTime / SFullCount
        
        return npFullAvg, npRedAvg, SRedAvg, SFullAvg

    # param: LangaugeGroup should be str "L1" or "L2"
    def get_mins(self, LanguageGroup, WordType):
        with open(self.file_name, newline='') as csvfile:

            reader = csv.DictReader(csvfile)

            npFull = sys.maxsize
            npRed = sys.maxsize
            sFull = sys.maxsize
            sRed = sys.maxsize
            
            for x in range(self.max_lines-1):
                read_line = reader.__next__()

                if read_line["LanguageGroup"] == LanguageGroup and read_line["WordType"] == WordType:
                    #verb type: NP-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Full":
                        if int(read_line["ReadingTime"]) < int(npFull):
                            npFull = read_line["ReadingTime"]
                
                    #verb type: NP-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Reduced":
                        if int(read_line["ReadingTime"]) < int(npRed):
                            npRed = read_line["ReadingTime"]

                    #verb type: S-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Full":
                        if int(read_line["ReadingTime"]) < int(sFull):
                            sFull = read_line["ReadingTime"]

                    #verb type: S-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Reduced":
                        if int(read_line["ReadingTime"]) < int(sRed):
                            sRed = read_line["ReadingTime"]
        return npFull, npRed, sFull, sRed

    def get_maxs(self, LanguageGroup, WordType):
        with open(self.file_name, newline='') as csvfile:

            reader = csv.DictReader(csvfile)

            npFull = -sys.maxsize - 1
            npRed = -sys.maxsize - 1
            sFull = -sys.maxsize - 1
            sRed = -sys.maxsize - 1
            
            for x in range(self.max_lines-1):
                read_line = reader.__next__()

                if read_line["LanguageGroup"] == LanguageGroup and read_line["WordType"] == WordType:
                    #verb type: NP-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Full":
                        if int(read_line["ReadingTime"]) > int(npFull):
                            npFull = read_line["ReadingTime"]
                
                    #verb type: NP-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "NounPhrase" and read_line["RCType"] == "Reduced":
                        if int(read_line["ReadingTime"]) > int(npRed):
                            npRed = read_line["ReadingTime"]
        
                    #verb type: S-bias, Embedded Clause Type: Full
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Full":
                        if int(read_line["ReadingTime"]) > int(sFull):
                            sFull = read_line["ReadingTime"]

                    #verb type: S-bias, Embedded Clause Type: Reduced
                    if read_line["VerbBias"] == "Sentence" and read_line["RCType"] == "Reduced":
                        if int(read_line["ReadingTime"]) > int(sRed):
                            sRed = read_line["ReadingTime"]
        return npFull, npRed, sFull, sRed

'''
Example:
data = data_dump("225_Project3_Experiment_Results.csv")
print("L1--------------------L1-------------------------L1")
npFullAvg, npRedAvg, SFullAvg, SRedAvg = data.get_averages("L1", "Critical")
npFullAvgPost, npRedAvgPost, SFullAvgPost, SRedAvgPost = data.get_averages("L1", "PostCritical")
print("----------------------MEAN-------------------------")
print("NP-bias Full (critical): " + str(npFullAvg) +
              ", NP-bias Full (post- critical): " + str(npFullAvgPost) +
              "\nNp-bias Reduced (critical): " + str(npRedAvg) +
              ", Np-bias Reduced (post-critical): " + str(npRedAvgPost) +
              "\nS-bias Full (critical): " + str(SFullAvg) +
              ", S-bias Full (post critical): " + str(SFullAvgPost) +
              "\nS-bias Reduced (critical): " + str(SRedAvg) +
              ", S-biased Reduced (post-critical): " + str(SRedAvgPost))
npFullMin, npRedMin, SFullMin, SRedMin = data.get_mins("L1", "Critical")
npFullMinPost, npRedMinPost, SFullMinPost, SRedMinPost = data.get_mins("L1", "PostCritical")
print("---------------------MIN--------------------------")
print("NP-bias Full (critical): " + str(npFullMin) + ", NP-bias Full (post-critical): " + str(npFullMinPost))
print("NP-bias Reduced (critical): " + str(npRedMin) + ", NP-bias Reduced (post-critical): " + str(npRedMinPost))
print("S-bias Full (critical): " + str(SFullMin) + ", S-bias Full (post-critical): " + str(SFullMinPost))
print("S-bias Reduced (critical): " + str(SRedMin) + ", S-bias Reduced (post-critical): " + str(SRedMinPost))
npFullMax, npRedMax, SFullMax, SRedMax = data.get_maxs("L1", "Critical")
npFullMaxPost, npRedMaxPost, SFullMaxPost, SRedMaxPost = data.get_maxs("L1", "PostCritical")
print("----------------------MAX--------------------------")
print("NP-bias Full (critical): " + str(npFullMax) + ", NP-bias Full (post-critical): " + str(npFullMaxPost))
print("NP-bias Reduced (critical): " + str(npRedMax) + ", NP-bias Reduced (post-critical): " + str(npRedMaxPost))
print("S-bias Full (critical): " + str(SFullMax) + ", S-bias Full (post-critical): " + str(SFullMaxPost))
print("S-bias Reduced (critical): " + str(SRedMax) + ", S-bias Reduced (post-critical): " + str(SRedMaxPost))
print("L2--------------------L2-------------------------L2")
npFullAvg, npRedAvg, SFullAvg, SRedAvg = data.get_averages("L2", "Critical")
npFullAvgPost, npRedAvgPost, SFullAvgPost, SRedAvgPost = data.get_averages("L2", "PostCritical")
print("----------------------MEAN-------------------------")
print("NP-bias Full (critical): " + str(npFullAvg) +
              ", NP-bias Full (post- critical): " + str(npFullAvgPost) +
              "\nNp-bias Reduced (critical): " + str(npRedAvg) +
              ", Np-bias Reduced (post-critical): " + str(npRedAvgPost) +
              "\nS-bias Full (critical): " + str(SFullAvg) +
              ", S-bias Full (post critical): " + str(SFullAvgPost) +
              "\nS-bias Reduced (critical): " + str(SRedAvg) +
              ", S-biased Reduced (post-critical): " + str(SRedAvgPost))
npFullMin, npRedMin, SFullMin, SRedMin = data.get_mins("L2", "Critical")
npFullMinPost, npRedMinPost, SFullMinPost, SRedMinPost = data.get_mins("L2", "PostCritical")
print("----------------------MIN--------------------------")
print("NP-bias Full (critical): " + str(npFullMin) + ", NP-bias Full (post-critical): " + str(npFullMinPost))
print("NP-bias Reduced (critical): " + str(npRedMin) + ", NP-bias Reduced (post-critical): " + str(npRedMinPost))
print("S-bias Full (critical): " + str(SFullMin) + ", S-bias Full (post-critical): " + str(SFullMinPost))
print("S-bias Reduced (critical): " + str(SRedMin) + ", S-bias Reduced (post-critical): " + str(SRedMinPost))
npFullMax, npRedMax, SFullMax, SRedMax = data.get_maxs("L2", "Critical")
npFullMaxPost, npRedMaxPost, SFullMaxPost, SRedMaxPost = data.get_maxs("L2", "PostCritical")
print("----------------------MAX--------------------------")
print("NP-bias Full (critical): " + str(npFullMax) + ", NP-bias Full (post-critical): " + str(npFullMaxPost))
print("NP-bias Reduced (critical): " + str(npRedMax) + ", NP-bias Reduced (post-critical): " + str(npRedMaxPost))
print("S-bias Full (critical): " + str(SFullMax) + ", S-bias Full (post-critical): " + str(SFullMaxPost))
print("S-bias Reduced (critical): " + str(SRedMax) + ", S-bias Reduced (post-critical): " + str(SRedMaxPost))
'''
