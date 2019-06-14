# Program to help select college/branch wrt rank
# NOTE : Program is designed for judicious use! Playing around can lead to crash ;)

import os,pickle
try:                                                
    from prettytable import from_csv,PrettyTable as PT               
except:                
    print"\nPrettytable module NOT installed on your pc !! Please install it first...\nTerminating.\n"
    quit()


class build:

    def __init__(self):
        self.name = ''
        self.cutoff = []

    def Input(self):
        self.name = raw_input('Enter Filename : ')
        temp = open(self.name+'.csv').readlines()
        for i in temp:
            self.cutoff.append(i.strip().split(','))

def sort(mytable):
    select = raw_input("\nSort Option         1. Institute Name(a/d)\n\
                    2. Course Name(a/d)\n\
                    3. OpeningRank(a/d)\n\
                    4. ClosingRank(a/d)\n\
                    5. Serial Number(a/d)\n\n\
    Choose your Option : ")             # ERROR for wishlist --> Option 5.
    dict1 = {'1':'Institute','2':'Course','3':'O-Rank','4':'C-Rank','5':'S.no','d':True,'a':False}
    mytable.sortby = dict1[select[0]]
    mytable.reversesort = dict1[select[1]]
    mytable.align = 'l'
    return True   


    
def new():
    year = int(raw_input("\nWhich Year Dataset to Use (2016/2017) : "))
    if year in [2016,2017]:
        code = str(year%2010)
    else:
        return
        
    brand = raw_input("\nWhich College tag to Search     --> a. IIT\n\
                                --> b. NIT\n\
                                --> c. III-T\n\n\
        Select Your Option(a/b/c) : ")

    ###
    if brand in ['a','b','c']:
        file0 = open('cutoff.txt','rb')
        try:
            
            while 1:
                obj0 = pickle.load(file0)
                if obj0.name==brand+code:
                    cutoff = obj0.cutoff                 # [college,branch,quota,open,close]
                    file0.close()
                    break
        except:
            print'Data not found :(\n'
            file0.close()
            return
    else:
        print 'Invalid Choice!\n'
        return
                

    duration = raw_input("\nCourse Duration (4 or 5 Years) : ")
    
    rank = int(raw_input("\nWhat is your Rank : "))

    l_var = int(raw_input("\nLower Variance : "))
    u_var = int(raw_input("\nUpper Variance (in no upper bound type '-1') : "))

    

    # work                              format : S.No,College,Branch,Opening,Closing

    table = PT(['S.no','Institute','Course','O-Rank','C-Rank'])

    lower = rank - l_var

    if u_var==-1:
        upper = 10**7
    else:
        upper = rank + u_var

    sno = 0

    ################################
    for i in range(len(cutoff)):
                      
        if len(cutoff[i])<3:
            break
        if len(cutoff[i])!=5:
            print 'Correct this data : ',cutoff[i]
                
        elif cutoff[i][2] in ['AI','OS'] and duration in cutoff[i][1]:
            cutoff[i][-1]=int(cutoff[i][-1])
            if cutoff[i][-1]>=lower and cutoff[i][-1]<=upper:                
                sno+=1
                row = [sno]+cutoff[i][0:2]+map(int,cutoff[i][3:])
                table.add_row(row)

                cutoff[i].append(sno)
        
    ################################

    sort(table)             # Manage S.No
    os.system('cls')
    print '\n*** Based on Last stage Cut-offs AND no HS considered ***\n'
    print table

    wish = map(int,raw_input("\nType S.No of Shortlisted (CSV) (0 if none) : ").split(','))

    if 0 not in wish:
        memo = raw_input("Enter memo name  : ")
        with open(memo+'.txt','a+') as file2:
            if not file2.read(1):
                file2.write('Institute,'+'Course,'+'O-Rank,'+'C-Rank\n')
            else:
                file2.seek(0,2)
            for i in cutoff:
                if len(i)==6 and i[-1] in wish:
                    temp = str(i[0])+','+str(i[1])+','+str(i[3])+','+str(i[4])
                    file2.write(temp+'\n') # correct it           

    # Work

    print '\nThank you! Your response has been saved!\n'

def old():
    memo = raw_input("\nWhich record data to show : ")
    with open(memo+".txt", "a+") as fp:
        mytable = from_csv(fp)
    os.system('cls')
    sort(mytable)
    print mytable

def guide():

    '''
        Currently a manual procedure but would later be added in an update
                                                                                                                '''
    os.system('cls')
    print '\nALGORITHM TO HELP DECIDE THE BEST OPTION!'

    choice = raw_input("\nWhat Suits your better :-    1. YOU are sure to pursue higher studies after ug\n\
                             2. YOU want to settle early with a job\n\
                             3. YOU are not sure\n\n\
                Select : ")
    os.system('cls')
    if choice == '1':
        print '\nYour first preference should be the course then Select the best college offering you the course\n\
                Prefer Tier 1 & Tier 2 colleges only!'
    elif choice =='2':
        print "\nChoose the best college you could get irrespective of the branch."
    else:
        os.system('cls')
        print open('guide.txt').read()

def newyear():      # Admin function to feed new year data
    file0 = open('cutoff.txt','ab+')
    while True:        
        obj0 = build()
        obj0.Input()
        pickle.dump(obj0,file0)
        ch = raw_input("press 'y' to feed more data ")
        if ch!='y':
            break
    file0.close()


#Driver Code
    
loop=1
try:
        
    while loop!='0':
        os.system('cls')
        choice = raw_input("\nWhich Category to Search     --> a. New Search\n\
                             --> b. Wishlist\n\
                             --> c. Analysis\n\
                             --> d. Guide\n\n\
        Select Your Option(a/b/c/d) : ")
        if choice=='0':
            newyear()
        elif choice=='a':
            new()
        elif choice=='b':
            try:
                old()
            except:
                print '\nNO Wishlist found!'
        elif choice=='c':
            import datamining
            datamining.start()
        else:
            guide()

        loop = raw_input("\nPress any key to start over (0 to exit).... ")
except:
    print 'Wrong Input! TERMINATING...'
    raw_input()
