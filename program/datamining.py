class mining:
    
    def __init__(self):

        self.college = ''
        self.course = ''
        self.currentRound = 1
        self.state = list()       # [ [Data1, Data2] , ... ] where each element is respective result of its round
                                      # DataN --> [OpeningRank, ClosingRank] of Nth Year

    def entry(self):

        self.college = raw_input('College : ')
        self.course = raw_input('Course : ')
        self.currentRound = int(raw_input('\nHow many round result do you have for this year : '))

        for i in range(7):
            data1 = [-1,-1]
            data2 = [-1,-1]
            print'College : ',self.college
            print'Course : ',self.course
            data1[0] = int(raw_input('\nOpening Rank of round '+str(i+1)+' in 2017 : '))
            data1[1] = int(raw_input('Closing Rank of round '+str(i+1)+' in 2017 : '))

            if i<self.currentRound:
                data2[0] = int(raw_input('\nOpening Rank of round '+str(i+1)+' in 2018 : '))
                data2[1] = int(raw_input('Closing Rank of round '+str(i+1)+' in 2018 : '))      

            os.system('cls')
            self.state.append([data1,data2])
        else:
            print'\nData uploaded successfully!\n'
            
    def new_record(self,new=0):
        if self.state[self.currentRound-1][1]==[-1,-1]:
            return
        if new:
            self.currentRound = new
        else:
            new = self.currentRound = int(raw_input(' Round Number : '))

        print 'College : ',self.college
        print 'Course : ',self.course
        self.state[new-1][1][0] = int(raw_input('\nOpening Rank of 2018  : '))
        self.state[new-1][1][1] = int(raw_input('Closing Rank of 2018  : '))
        os.system('cls')


    def tabular(self):
        
        table = PT(['Round','Year','OpeningRank','ClosingRank'])
        empty = [' ']*4
        
        for i in range(7):
            table.add_row([i+1,2017] + self.state[i][0])

            if i<self.currentRound:
                table.add_row([i+1,2018] + self.state[i][1])
                table.add_row(empty)
        print table 

def analysis():
    try:
        file3 = open('pattern.txt','rb')
    except:
        print '\nNo Data found!\n'
        return
    table = PT(['S.no','College','Course'])
    i=1
    try:
        while True:
            obj3 = pickle.load(file3)
            table.add_row([i,obj3.college,obj3.course])
            i+=1
    except EOFError:
        print table
        file3.seek(0)
        ch = int(raw_input("Select your choice (0 for none) : "))   #GO for Loop
        os.system('cls')
        if ch:
            for i in range(ch):
                obj5 = pickle.load(file3)
            else:
                print '\n\t',obj5.college,' -- ',obj5.course,'\n'
                obj5.tabular()
        else:
            return 1

def new():
    with open('pattern.txt','ab') as file0:
        while True:
            obj0 = mining()
            obj0.entry()
            pickle.dump(obj0,file0)
            ch = raw_input("press 'y' to enter more : ")
            if ch!='y':
                break

def update():           # See if remove/rename is needed
    num = int(raw_input(' Round Number : '))
    temp = open('temp.txt','ab')
    file1 = open('pattern.txt','ab+')
    try:
        while True:
            obj1 = pickle.load(file1)
            obj1.new_record(num)
            pickle.dump(obj1,temp)
    except EOFError:
        file1.close()
        temp.close()
        os.remove('pattern.txt')
        os.rename('temp.txt','pattern.txt')

def start():
    loop=1
    while loop!='0':
        
        print '\n1. Analysis\n2. New Record\n3. Update\n'
        ch = raw_input('Enter your choice : ')
        os.system('cls')
        if ch=='1':
            if analysis():
                return
        elif ch=='2':
            new()
        elif ch=='3':
            update()
        else:
            return

        loop = raw_input("\nPress enter to start over (0 to go back).... ")
        
#Driver Code

import pickle,os
try:                                                
    from prettytable import PrettyTable as PT               
except:                
    print"\nPrettytable module NOT installed on your pc !! Please install it first...\nTerminating.\n"
    quit()
     
