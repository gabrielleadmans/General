#writing code to clean up output file from FlexStation.
#input a csv and output a better one





# setting working directory

import os
os.chdir('/Users/gabrielleadmans/Documents/_06 data/Fluo-8 FlexStation')
os.getcwd() #checks the directory in use


#opening file in read only mode
print('file name?')
filename = str(input())

with open('my_data.csv', 'r') as infile, open('data_out.csv', 'w') as outfile:
    for line in infile:
        outfile.write(line)

with 
    
    print ('yay')


    test = os.path.isfile(filename)
    print(test)
    if test:
        print('file open is' + 'filename')
        

2023-03-22-1747.csv

with open('2023-03-22-1747.csv'⁩, 'r', encoding= 'utf8') as f:






import csv

    csvreader = csv.reader(infile)






with open('testfile.csv', 'r', encoding= 'utf8') as infile, open('data_out.csv','w') as outfile:
    rows = []
    rows.append('temperature,Time,1A,1B,1C,1D, 1F,1D,1E,1F,1G, 1H')
    n=0
    letter=0
    finalrow = 0
    outfile_list=[]
    infile_noblanks=[]
    for row in infile:
        row_aslist= row.split(',')
        if row_aslist !=['', '', '', '', '', '', '', '', '', '', '', '', '\n']:
            #print(row)
            infile_noblanks.append(row)
               

    for row in infile_noblanks:
        n=n+1
        if n== 2 or ((n-2)/16).is_integer():
            letter='A'
            finalrow = finalrow +1
            row_aslist= row.split(',')
            new_row_aslist = ['','','','','','','','','','','','','']
            temp= row_aslist[1]
            row_aslist = row_aslist[1:]
            new_row_aslist[0]=temp
            for item in row_aslist :
                if item != '':
                    time=item #unnecssary line
                    new_row_aslist[1]=item
                    print(new_row_aslist)

        
        elif not (n/2).is_integer():
            row_aslist= row.split(',')           
            if letter=='A':
                new_row_aslist[2:]=row_aslist[2:]
                letter == 'B'
                outfile_list.append(','.join(new_row_aslist))
                print(outfile_list)
                break
            if letter == 'B':
                new_row_aslist[2:]=row_aslist[2:]
                letter == 'C'
                outfile_list.append(','.join(new_row_aslist))
                print(outfile_list)
                break
            
        
                
        row_aslist= row.split(',')

         
        rows.append(row)
    rows





row = (',21.6,,,,,,,0.7346')
n=2

if n== 2:
    row_aslist= row.split(',')
    new_row_aslist = ['','','','','','','','','','','','','']
    temp= row_aslist[1]
    row_aslist = row_aslist[1:]
    new_row_aslist[0]=temp
    for item in row_aslist :
        if item != '':
            time=item #unnecssary line
            new_row_aslist[1]=item
if n
#if n is 3



rows = []
rows.append('temperature,Time,1A,1B,1C,1D,1F,1D,1E,1F,1G,1H')

    

    
    test = os.path.isfile(infile)
    print (test)



    test = os.path.isfile(filename)






















=========
    

with open('testfile.csv', 'r', encoding= 'utf8') as infile, open('data_out.csv','w') as outfile:
    n=0
    letter=0
    finalrow = 0
    outfile_list=['temperature,Time,1A,1B,1C,1D, 1F,1D,1E,1F,1G, 1H']
    infile_noblanks=[]
    for row in infile:
        row_aslist= row.split(',')
        #print(row_aslist)
        if row_aslist !=['', '', '', '', '', '', '', '', '', '', '', '\n']:
            #print(row)
            infile_noblanks.append(row)
               

    for row in infile_noblanks:
        n=n+1
        if n== 2 or ((n-2)/16).is_integer():
            letter='A'
            finalrow = finalrow +1
            row_aslist= row.split(',')
            new_row_aslist = ['','','','','','','','','','','','','']
            temp= row_aslist[1]
            row_aslist = row_aslist[1:]
            new_row_aslist[0]=temp
            for item in row_aslist :
                if item != '':
                    #time=item 
                    new_row_aslist[1]=item
                    #print(new_row_aslist)

        
        elif not (n/2).is_integer():
            row_aslist= row.split(',')           
            if letter=='A':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[2]=item

                letter = 'B'
                continue
            
            if letter=='B':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[3]=item

                letter = 'C'
                continue

            if letter=='C':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[4]=item

                letter = 'D'
                continue


            if letter=='D':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[5]=item
                letter = 'E'
                continue

            if letter=='E':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[6]=item
                letter = 'F'
                continue

            if letter=='F':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[7]=item
                letter = 'G'
                continue

            if letter=='G':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[8]=item
                letter = 'H'
                continue            


            if letter=='H':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[9]=item
                letter = 'A'

                stripped_new_row_aslist =[]
                for item in new_row_aslist:
                    stripped_new_row_aslist.append(item.strip('\n'))
                outfile_list.append(','.join(stripped_new_row_aslist))
                print('new row is ' + str(outfile_list))
                continue
            
        #if n== 3418:
        #    break



    print('outfile is', outfile_list)
    outfile.write(outfile_list)
    #return outfile_list

==========

with open('testfile.csv', 'r', encoding= 'utf8') as infile, open('data_out.csv','w') as outfile:
    n=0
    letter=0
    finalrow = 0
    outfile_list=['temperature,Time,1A,1B,1C,1D, 1F,1D,1E,1F,1G, 1H']
    infile_noblanks=[]
    for row in infile:
        row_aslist= row.split(',')
        print(row_aslist)
        print(row)
        if row_aslist !=['', '', '', '', '', '', '', '', '', '', '', '\n']:
            #print(row)
            row_aslist_stripped=[]
            for item in row_aslist:
    
                row_aslist_stripped.append(item.strip('\n'))
            infile_noblanks.append(row_aslist_stripped)
            print(infile_noblanks)

q=['', '', '', '', '', '', '', '', '', '', '', '1234\n']
q_stripped =[]            
for item in q:
    q_stripped.append(item.strip('\n'))
    print (item)



                
with open('testwrite.csv', 'w') as file:
        for item in outfile_list:
            file.write(str(item)+', ')
        file.write('n')



        for x in row:
            file.write(str(x)+', ')
        file.write('n')


=== 2023_03_24


        
with open('testfile.csv', 'r', encoding= 'utf8') as infile, open('data_out.csv','w') as outfile:
    n=0
    letter=0
    finalrow = 0
    outfile_list=['temperature,Time,1A,1B,1C,1D, 1F,1D,1E,1F,1G, 1H']
    infile_noblanks=[]
    for row in infile:
        row_aslist= row.split(',')
        print(row_aslist)
        print(row)
        if row_aslist !=['', '', '', '', '', '', '', '', '', '', '', '\n']:
            #print(row)
            row_aslist_stripped=[]
            for item in row_aslist:
    
                row_aslist_stripped.append(item.strip('\n'))
            infile_noblanks.append(row_aslist_stripped)



    for row_aslist in infile_noblanks:
        n=n+1
        if n== 2 or ((n-2)/16).is_integer():
            letter='A'
            new_row_aslist = ['','','','','','','','','','','','','']
            temp= row_aslist[1]
            row_aslist = row_aslist[1:]
            new_row_aslist[0]=temp
            for item in row_aslist :
                if item != '':
                    #time=item 
                    new_row_aslist[1]=item
                    #print(new_row_aslist)

        
        elif not (n/2).is_integer():
            row_aslist= row.split(',')           
            if letter=='A':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[2]=item

                letter = 'B'
                continue
            
            if letter=='B':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[3]=item

                letter = 'C'
                continue

            if letter=='C':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[4]=item

                letter = 'D'
                continue


            if letter=='D':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[5]=item
                letter = 'E'
                continue

            if letter=='E':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[6]=item
                letter = 'F'
                continue

            if letter=='F':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[7]=item
                letter = 'G'
                continue

            if letter=='G':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[8]=item
                letter = 'H'
                continue            


            if letter=='H':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[9]=item
                letter = 'A'
                outfile_list.append(','.join(new_row_aslist))
                #print('new row is ' + ','.join(new_row_aslist))
                continue
            
        #if n== 3418:
        #    break



    print('outfile is', outfile_list)
    
    #outfile.write(outfile_list)
    #return outfile_list





   # ===== 2023_03_24- 12:28


        

with open('testfile.csv', 'r', encoding= 'utf8') as infile, open('data_out.csv','w') as outfile:
    n=0
    letter=0
    finalrow = 0
    outfile_list=['temperature,Time,1A,1B,1C,1D,1E,1F,1G,1H']
    infile_noblanks=[]
    for row in infile:
        row_aslist= row.split(',')
        #print(row_aslist)
        if row_aslist !=['', '', '', '', '', '', '', '', '', '', '', '\n']:
            #print(row)
            infile_noblanks.append(row)
               

    for row in infile_noblanks:
        n=n+1
        if n== 2 or ((n-2)/16).is_integer():
            letter='A'
            finalrow = finalrow +1
            row_aslist= row.split(',')
            new_row_aslist = ['','','','','','','','','','','','','']
            temp= row_aslist[1]
            row_aslist = row_aslist[1:]
            new_row_aslist[0]=temp
            for item in row_aslist :
                if item != '':
                    #time=item 
                    new_row_aslist[1]=item
                    #print(new_row_aslist)

        
        elif not (n/2).is_integer():
            row_aslist= row.split(',')           
            if letter=='A':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[2]=item

                letter = 'B'
                continue
            
            if letter=='B':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[3]=item

                letter = 'C'
                continue

            if letter=='C':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[4]=item

                letter = 'D'
                continue


            if letter=='D':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[5]=item
                letter = 'E'
                continue

            if letter=='E':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[6]=item
                letter = 'F'
                continue

            if letter=='F':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[7]=item
                letter = 'G'
                continue

            if letter=='G':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[8]=item
                letter = 'H'
                continue            


            if letter=='H':
                for item in row_aslist:
                    if item != '':
                        new_row_aslist[9]=item
                letter = 'A'

                stripped_new_row_aslist =[]
                for item in new_row_aslist:
                    stripped_new_row_aslist.append(item.strip('\n'))
                outfile_list.append(','.join(stripped_new_row_aslist))
                print('new row is ' + str(outfile_list))
                continue
            
        #if n== 3418:
        #    break



    print('outfile is', outfile_list)

                    
with open('testwrite.csv', 'w') as file:
        for item in outfile_list:
            file.write(str(item)+'\n ')
        file.write('n')
