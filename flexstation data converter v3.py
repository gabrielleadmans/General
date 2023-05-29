# TODO:
# - accept user input

# (very fragile) code to clean up output file from FlexStation.
#input a csv and output a better one
# this only works for a single column of data!! and it needs to be in column 11
# Improvement over v2: now doesn't remove the blank rows from lack of measurements and
# can tehrefore deal with files where not alll wells were analysed 2023/04/17.



#improvements needed:
# - add temperature
# - change name of input file?
# - deal with text in column M of spreadsheet??
# - deal with several columns of data
# for x,y might be better
# look up pandas


# setting working directory

import os
os.chdir('/Users/gabrielleadmans/Documents/_06 data/Fluo-8 FlexStation')
os.getcwd() #checks the directory in use


# opening csv and creating a list of better formatted values
with open('2023-04-07-1403.csv', 'r', encoding= 'utf8') as infile:
    n=0
    letter=0
    finalrow = 0
    outfile_list=['temperature,Time,A,B,C,D,E,F,G,H']
    infile_noblanks=[]
    row_nb = 0
    for row in infile:
        row_nb = row_nb +1
        if not(((row_nb-18)/17).is_integer()):
            row_aslist= row.split(',')
            #print(row)
            infile_noblanks.append(row)
               

    for row in infile_noblanks:
        n=n+1
        if n== 1 or ((n-1)/16).is_integer():
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

        
        elif (n/2).is_integer():
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




    print('outfile is', outfile_list)

# writing the new cvs file                    
with open('testwrite.csv', 'w') as file:
        for item in outfile_list:
            file.write(str(item)+'\n ')
        file.write('n')

