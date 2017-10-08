
from geneticAlgorithm import *
classdict={###Foundation classes
                'ETCS 105' : ['Career Discovery', 2,'Engineering Tech & Comp Sci', [], [],10],
                'ETCS 108' : ['Computer Internet and Society', 3, 'Engineering Tech & Comp Sci', [], [],1],
                'Dept Cnst':['x', 3, 'v', [], [],27],
                'FCWR 101' : ['Writing I: Foundations of College Composition', 3, 'Foundations',[], [],17 ],
                'FCWR 151' : ['Writing II: Foundations of Research Writing', 3, 'Foundations',['FCWR 101'], [],20 ],
                'FCSP 105' : ['Foundations of Speech Communication', 3, 'Foundations',[], [],3 ],
                'FCSC 101' : ['Foundations of Scientific Process', 3, 'Foundations',[], [],11 ],
                'FCIQ 101' : ['Foundations of Inquiry', 3, 'Foundations', [], [],39 ],
                'FCWR 304' : ['Communication for Technical Professions', 3, 'Foundations', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [],25 ],
                 ### Seminars:
                'ICLT 3XX' : ['Literature choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [],36 ],
                'ICPH 3XX' : ['Philosophy choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [],30 ],
                'ICBS 3XX' : ['Behavioral Science choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [],26 ],
                'ICSS 309' : ['Technology and Global Issues', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [],24 ],
                ###MATH
                'MATH 170' : ['Calculus I', 4, 'Math', [], [],7 ],
                ###SCIENCE
                'PHYS 170' : ['General Physics I', 4, 'Science', [], ['MATH 170'],31 ],
                #'CHEM 110' : ['General Chemistry I', 4, 'Science', [], ['TMAT 135'] ],
                'BIOL 110' : ['General Biology I', 4, 'Science', [], [],28 ],
                #requires 4 CSCI/ITEC totaling 12
                # 'CSCI/ITEC':['4 CSCI/ITEC', 3, 'General Option', [], [] ],
                'MATH 180': ['Calculus II', 4, 'Mathematics', ['MATH 170'], [],2 ],
                'MATH 310': ['Linear Algebra', 3, 'Mathematics', ['MATH 180'], [],12 ],
                'PHYS 180': ['General Physics II', 4,'Sciences', ['PHYS 170'], ['MATH 180'],15 ],
                #'Life Science/Biology': ['Elective', 3,'Sciences', [], [] ],
                #'CHEM 150': ['General Chemistry II', 4, 'Sciences', ['CHEM 110'], [] ],
                #'BIOL 150': ['General Biology II', 4, 'Sciences', ['BIOL 110'], [] ],
                #'Physics': ['Elective', 3, 'Sciences', [], [] ],
                #requires 2 math/science elective totaling 6
                'Mathematics/Science Electives': ['Math/Science Electives', 3, 'Mathematics/Science Electives', [], [],35 ],
                'Mathematics/Science Electives2': ['Math/Science Electives', 3, 'Mathematics/Science Electives', [], [],13 ],
                'CSCI 300': ['DataBase Management', 3, 'Big Data Management and Analytics Concentration', ['CSCI 260'], [],38],
                'CSCI 355':['Artificial Intelligence I', 3, 'Artificial Intelligence I', ['CSCI 260'], [],8],
                'General Elective': ['Elective', 3, 'General Elective', [], [],22 ],
                #Network Security Concentration
                #'CSCI 352': ['Introduction to Network and Internet Security', 3, 'Network Security Concentration', ['CSCI 345', 'CSCI 370'], []],
                'CSCI 357': ['CISCO Academy Level 1', 3, 'Network Security Concentration', ['Dept Cnst'], [],6],
                #'CSCI 440': ['Network Security and Perimeter Protection', 3, 'Network Security Concentration', ['CSCI 345','CSCI 370'], ['CSCI 385']],
                'CSCI 445': ['Operating System Security', 3, 'Network Security Concentration', ['CSCI 345'], [],23],
                #'CSCI 460': ['Special Topics I', 3, 'Network Security Concentration', ['Dept Cnst'], []],
                #  'CSCI 470': ['Special Topics II', 3, 'Network Security Concentration', ['Dept Cnst'], []],
                #Big Data Management and Analytics Concentration
                #  'CSCI 365': ['Information Retrieval', 3, 'Big Data Management and Analytics Concentration', ['CSCI 270', 'CSCI 300'], []],
                #  'CSCI 372': ['Big Data Analytics', 3, 'Big Data Management and Analytics Concentration', [], []],
                # 'CSCI 401': ['Database Interfaces and Programming', 3, 'Big Data Management and Analytics Concentration', ['CSCI 300'], []],
                'CSCI 405': ['Distributed Database Systems', 3, 'Big Data Management and Analytics Concentration', ['CSCI 300'], [],33],
                #  'CSCI 415': ['Introduction to Data Mining', 3, 'Big Data Management and Analytics Concentration', [' CSCI 270', 'CSCI 300', 'CSCI 335'], []],
                'CSCI 125': ['Computer Programming I', 3, 'Computer Science', [], [],19],
                'CSCI 155': ['Computer Organization and Architecture', 3,'Comptuer Science',['CSCI 125', 'MATH 170'], [],32],
                'CSCI 185': ['Computer Programming II', 3, 'Computer Science', ['CSCI 125'], [],1],
                'CSCI 235': ['Elements of Discrete Structures', 3, 'Computer Science', ['MATH 170', 'CSCI 185'], [],34],
                'CSCI 260': ['Data Structures', 3, 'Computer Science', ['MATH 170', 'CSCI 185'], [],9],
                'CSCI 270': ['Probability and Statistics for CS', 3, 'Computer Science', ['CSCI 235', 'MATH 180'],[],0],
                'CSCI 312': ['Theory of Computation', 3, 'Computer Science', ['CSCI 235'], [],21],
                'CSCI 318': ['Programming Language Concepts', 3, 'Computer Science',['CSCI 260'], [],29],
                'CSCI 330': ['Operating Systems', 3, 'Computer Science', ['CSCI 260', 'CSCI 185'], [],14],
                'CSCI 335': ['Design and Analysis of Algorithm', 3, 'Computer Science', ['CSCI 260'], [],5],
                'CSCI 345': ['Computer Networks', 3, 'Computer Science', ['CSCI 330'],[],4],
                'CSCI 380': ['Introduction to Software Engineering', 3, 'Computer Science',['CSCI 260'],[],18],
                'CSCI 455': ['Senior Project', 3, 'Computer Science', ['Dept Cnst'],[],37],
                # 'CSCI XXX': ['Electives', 6, 'Computer Science', [],[]]
}
####################this dictionary below not used. Use the one above###############################################
"""classdict={
    ### FOUNDATION
    'FCWR 101' : ['Writing I: Foundations of College Composition', 3, 'Foundations',[], [] ],
    'FCWR 155' : ['Writing II: Foundations of Research Writing', 3, 'Foundations',['FCWR 101'], [] ],
    'FCSP 105' : ['Foundations of Speech Communication', 3, 'Foundations',[], [] ],
    'FCSC 101' : ['Foundations of Scientific Process', 3, 'Foundations',[], [] ],
    'FCIQ 101' : ['Foundations of Inquiry', 3, 'Foundations', [], [] ],
    'FCWR 304' : ['Communication for Technical Professions', 3, 'Foundations', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [] ],
   ### Seminars:
    'ICLT 3XX' : ['Literature choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [] ],
    'ICPH 3XX' : ['Philosophy choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [] ],
    'ICBS 3XX' : ['Behavioral Science choice', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [] ],
    'ICSS 309' : ['Technology and Global Issues', 3, 'Seminars', ['FCIQ 101', 'FCSP 105', 'FCSC 101', 'FCWR 151'], [] ],

   ###MATH
    'MATH 170' : ['Calculus I', 4, 'Math', [], [] ],
   ###SCIENCE
    'PHYS 170' : ['General Physics I', 4, 'Science', [], ['MATH 170'] ],
    'CHEM 110' : ['General Chemistry I', 4, 'Science', [], [] ],
    'BIOL 110' : ['General Biology I', 4, 'Science', [], [] ],

#requires 4 CSCI/ITEC totaling 12
    #'CSCI/ITEC':['4 CSCI/ITEC', 3, 'General Option', [], [] ],
    'MATH 180': ['Calculus II', 4, 'Mathematics', ['MATH 170'], [] ],
    'MATH 310': ['Linear Algebra', 3, 'Mathematics', ['MATH 180'], [] ],
    'PHYS 180': ['General Physics II', 4,'Sciences', ['PHYS 170'], ['MATH 180'] ],
    #'Life Science/Biology': ['Elective', 3,'Sciences', [], [] ],
    'CHEM 150': ['General Chemistry II', 4, 'Sciences', ['CHEM 110'], [] ],
    'BIOL 150': ['General Biology II', 4, 'Sciences', ['BIOL 110'], [] ],
    #'Physics': ['Elective', 3, 'Sciences', [], [] ],
    #requires 2 math/science elective totaling 6
    #'Mathematics/Science Electives': ['Math/Science Electives', 3, 'Mathematics/Science Electives', [], [] ],
    #'General Elective': ['Elective', 3, 'General Elective', [], [] ],


#Network Security Concentration
    'CSCI 352': ['Introduction to Network and Internet Security', 3, 'Network Security Concentration', ['CSCI 345'], []],
    'CSCI 357': ['CISCO Academy Level 1', 3, 'Network Security Concentration', ['Dept Cnst'], []],
    'CSCI 440': ['Network Security and Perimeter Protection', 3, 'Network Security Concentration', ['CSCI 345'], ['CSCI 385']],
    'CSCI 445': ['Operating System Security', 3, 'Network Security Concentration', ['CSCI 385', 'CSCI 345'], []],
    'CSCI 460': ['Special Topics I', 3, 'Network Security Concentration', ['Dept Cnst'], []],
    'CSCI 470': ['Special Topics II', 3, 'Network Security Concentration', ['Dept Cnst'], []],
    'CSCI 385': ['Network and Internet Security', 3, 'Network Security Concentration', ['CSCI 345'], ['CSCI 440']],
    #Big Data Management and Analytics Concentration
    'CSCI 365': ['Information Retrieval', 3, 'Big Data Management and Analytics Concentration', ['CSCI 270', 'CSCI 300'], []],
    'CSCI 372': ['Big Data Analytics', 3, 'Big Data Management and Analytics Concentration', [], []],
    'CSCI 401': ['Database Interfaces and Programming', 3, 'Big Data Management and Analytics Concentration', ['CSCI 300'], []],
    'CSCI 405': ['Distributed Database Systems', 3, 'Big Data Management and Analytics Concentration', ['CSCI 300'], []],
    'CSCI 415': ['Introduction to Data Mining', 3, 'Big Data Management and Analytics Concentration', [' CSCI 270', 'CSCI 300', 'CSCI 335'], []],
    'CSCI 300': ['DataBase Management', 3, 'Big Data Management and Analytics Concentration', ['CSCI 260'], []],

    'CSCI 125': ['Computer Programming I', 3, 'Computer Science', [], []],
    'CSCI 155': ['Computer Organization and Architecture', 3,'Comptuer Science',['CSCI 125', 'MATH 170'], []],
    'CSCI 185': ['Computer Programming II', 3, 'Computer Science', ['CSCI 125'], []],
    'CSCI 235': ['Elements of Discrete Structures', 3, 'Computer Science', ['MATH 170', 'CSCI 185'], []],
    'CSCI 260': ['Data Structures', 3, 'Computer Science', ['MATH 170', 'CSCI 185'], []],
    'CSCI 270': ['Probability and Statistics for CS', 3, 'Computer Science', ['CSCI 235', 'MATH 180'],[]],
    'CSCI 312': ['Theory of Computation', 3, 'Computer Science', ['CSCI 235'], []],
    'CSCI 318': ['Programming Language Concepts', 3, 'Computer Science',['CSCI 260'], []],
    'CSCI 330': ['Operating Systems', 3, 'Computer Science', ['CSCI 260', 'CSCI 185'], []],
    'CSCI 335': ['Design and Analysis of Algorithm', 3, 'Computer Science', ['CSCI 260'], []],
    'CSCI 345': ['Computer Networks', 3, 'Computer Science', ['CSCI 330'],[]],
    'CSCI 380': ['Introduction to Software Engineering', 3, 'Computer Science',['CSCI 260'],[]],
    'CSCI 455': ['Senior Project', 3, 'Computer Science', ['Dept Cnst'],[]]

    #'CSCI XXX': ['Electives', 6, 'Computer Science', [],[]]
}"""


class SequenceGene(Gene):
    def __init__(self, name):
        Gene.__init__(self)
        self.randomInit()#<---random start value
        self.name = name#<--- keep track of semester the gene repersents

    def printGene(self):
        print "name = " + self.name +"    " + "\tsemester = " + str(self.value) #<---Print name of semester and possible classes to take in that semester

    def randomInit(self):
        self.value =random.choice([1,2,3,4,5,6,7,8])#['s1','s2','s3','s4','s5','s6','s7','s8'])


class SequenceChromosome(Chromosome):                       #/
    def __init__(self, length):                             #|
        Chromosome.__init__(self, length)                   #|
        self.randomInit()                                   #|
        self.fitness = self.fitnessFunction()               #|
                                                            #|
    def randomInit(self):                                   #| creating a chromosome that hold all classes as genes
        states = classdict.keys()                           #| (all keys in classdict are genes)
        for state in range(0,self.length):                  #|
            newGene = SequenceGene(states [state])          #|
            self.genes.append(newGene)                      #\



    def fitnessFunction(self):
        totalcredit = 18
        creditcount1 = 0
        creditcount2 = 0
        creditcount3 = 0
        creditcount4 = 0
        creditcount5 = 0
        creditcount6 = 0
        creditcount7 = 0
        creditcount8 = 0
        fitness = 0
        equalCount = 0

        for CLASS in range(0, len(self.genes)-1):                                       #CLass is an index that reference the gene in self.gene
            if(classdict[self.genes[CLASS].name][3]!=[]):                               # if statements checks the class in the dictionary has any pre-req
                p=classdict[self.genes[CLASS].name][3]                                  # storing per-req info into p
                for i in p:                                                             # storing each pre req in i
                    if (self.genes[CLASS].value < self.genes[classdict[i][5]].value ):  #if statement checks the current index value and sees if it is less then the value of the per-req class
                        fitness +=1                                                     #this tell us that the class hasn't met its pre-req requierments so fitness += 1 (VALUE REPRESENT SEMESTER)
                    """if (self.genes[CLASS].value == self.genes[classdict[i][5]].value ):#
                        equalCount +=1"""                                               #

            if(classdict[self.genes[CLASS].name][4]!=[]):
                p=classdict[self.genes[CLASS].name][4]                                  #Same as per-req but accessing list of co-req in dictionary
                for i in p:
                    if (self.genes[CLASS].value < self.genes[classdict[i][5]].value ):
                        fitness +=1

            if(self.genes[CLASS].value == 1):                                           #add all credits of each class in a single semester to a count
                creditcount1+=classdict[self.genes[CLASS].name][1]                      #each count is for its own semester
            if(self.genes[CLASS].value == 2):                                           #when you add to count you will not interfer with other count variable
                creditcount2+=classdict[self.genes[CLASS].name][1]                      #
            if(self.genes[CLASS].value == 3):
                creditcount3+=classdict[self.genes[CLASS].name][1]
            if(self.genes[CLASS].value == 4):
                creditcount4+=classdict[self.genes[CLASS].name][1]
            if(self.genes[CLASS].value == 5):
                creditcount5+=classdict[self.genes[CLASS].name][1]
            if(self.genes[CLASS].value == 6):
                creditcount6+=classdict[self.genes[CLASS].name][1]
            if(self.genes[CLASS].value == 7):
                creditcount7+=classdict[self.genes[CLASS].name][1]
            if(self.genes[CLASS].value == 8):
                creditcount8+=classdict[self.genes[CLASS].name][1]
        if(12>creditcount1 or creditcount1> 18):                                # checks to see if count of each semester is below 12 or higher then 18
            fitness +=1                                                         # if the count is less then 12 or higher then 18 fitness +=
        if(12>creditcount2 or creditcount2> 18):
            fitness +=1
        if(12>creditcount3 or creditcount3> 18):
            fitness +=1
        if(12>creditcount4 or creditcount4> 18):
            fitness +=1
        if(12>creditcount5 or creditcount5> 18):
            fitness +=1
        if(12>creditcount6 or creditcount6> 18):
            fitness +=1
        if(12>creditcount7 or creditcount7> 18):
            fitness +=1
        if(12>creditcount8 or creditcount8> 18):
            fitness +=1

        # if equalCount == 0:
        #     print "zero!"

        return fitness



class SequencePopulation(Population):                       #this class determines the size of your chromosome
    def __init__(self, populationSize, chromosomeSize):     #with a population that determines how many output you receive
        Population.__init__(self, populationSize)
        self.randomPopulation(chromosomeSize)

    def randomPopulation(self, chromosomeSize):
        for a in range(0, self.populationSize):
            self.generation.put(SequenceChromosome(chromosomeSize))



geneticAlgorithm(SequencePopulation(36,40))

                                            #Random print methood i used when starting project
print len(classdict)                        #
print classdict.keys()                      #
name=classdict.keys()
name.sort()
print name
