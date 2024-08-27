# add module
import sys
import os.path
import csv
import os

def freplacement (List_pair,string_replacement,count_replasment):
    this_count_replasment = count_replasment
    return_string = string_replacement

    for pair in List_pair:
        while return_string.find(pair[0]) != -1:
            return_string = return_string.replace(pair[0], pair[1], 1)
            # total number of symbols replaced old or new?
            this_count_replasment += 1 * len(pair[0])
    # recursion?
    # if count_replasment!=this_count_replasment:
    #    return_string,this_count_replasment=freplacement(List_pair,return_string,this_count_replasment)


    return [return_string,this_count_replasment]


debag = False

# error sting
err_message_param = 'Not enough actual parameters.'
err_message_file = 'The specified file was not found.'


# check list params
if len(sys.argv) != 3:
    if len(sys.argv) < 2:
        raise ValueError(f'{err_message_param}\nParameter(1) "Configuration file" is not specified')

    if len(sys.argv) < 3:
        raise ValueError(f'{err_message_param}\nParameter(2) "Target File" is not specified')

# get params
this_script_name  = sys.argv[0]
this_script_path = os.path.abspath(os.curdir)
configuration_file = sys.argv[1]
target_file = sys.argv[2]

# check params
if not os.path.isfile(os.path.join(this_script_path,configuration_file)):
     raise ValueError(f'{err_message_file}\n{os.path.join(this_script_path,configuration_file)} not exists configuration nfile')

if not os.path.isfile(os.path.join(this_script_path,target_file)):
    raise ValueError(f'{err_message_file}\n{os.path.join(this_script_path,target_file)} not exists target nfile')


# get and show params
if debag:
    print (f'######################################################################')
    print (f'Current script: {os.path.join(this_script_path,this_script_name)}')
    print (f'######################################################################')       
    print (f'Configuration file: {os.path.join(this_script_path,configuration_file)}') 

list_of_pairs = [] 

with open(configuration_file, 'r') as fr:
    reader = csv.reader(fr)
    for rows in reader:
       for row in rows:
        list_of_pairs.append(row.split('='))   

if debag:
    print(list_of_pairs)


 
# get target file
if debag:
    print (f'######################################################################')
    print (f'Target file: {os.path.join(this_script_path,target_file)}') 

row_num = 0
count_replacement = 0
count_replacement_list = []
replacement_list = []

with open(target_file,"r") as fr:
    reader = csv.reader(fr)   
    for rows in reader:
      for row in rows:
        count_replacement =0
        
        if debag:
            print (f'\tTarget file line({row_num}): before edit') 
            print (f'\t\t{row}') 
        # replace
        row,count_replacement=freplacement(list_of_pairs,row,count_replacement) 
        if debag:
            print (f'\tTarget file line({row_num}): after edit ({count_replacement} replacement count)') 
            print (f'\t\t{row}') 
        count_replacement_list.append(count_replacement)
        replacement_list.append(row);
        row_num +=1  

if debag:
    print (f'######################################################################')
    print(count_replacement_list)
    print(replacement_list)


# sorded 
arg_sort = sorted(range(len(count_replacement_list)), key=lambda i: count_replacement_list[i], reverse=True)

if debag:
    print (f'######################################################################')
    print([count_replacement_list[i] for i in arg_sort])
    print([replacement_list[i] for i in arg_sort])

with open(target_file, 'w') as fw:
    for i in arg_sort:
        fw.write(f"{replacement_list[i]}\n")

if debag:
    print (f'######################################################################')

# show
with open(target_file, 'r') as fr:
    reader = csv.reader(fr)   
    for rows in reader:
      for row in rows:
       print(row)   

input("Press Enter to continue.")