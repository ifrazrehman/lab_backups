import sys, os
import io
import csv
from collections import defaultdict
from collections import Counter
from subprocess import check_output

def extract(repo_dir,input_path,output_path):
    os.chdir(repo_dir)
    file = open(input_path, "r")
    output = open(output_path , "w")

    # (0 = readme itself, 1 = with readme, 2 = other files)
    #output.write("commit_id,filename,date,code\n")
    count =0
    for line in file:
        commit_id = line[0:7]
        date = os.popen("git log " + commit_id + " --pretty=format:\"%ct\"" + " -1").read()

        #ADD git command to extract committor and author here
        file_list= list()
        s = os.popen("git log  --name-only --oneline " + line.strip() +  " -1" ).read()
        buf = io.StringIO(s)
        count = 0

        for line in buf:
            #Do something

        output.write(commit_id+","+file_name+","+ date + ","+ str(act_file_code)+"\n")






        #
        # s = os.popen("git log  --name-only --oneline " + commit_id +  " -1" ).read()
        # buff = io.StringIO(s)
        # for line in buff:
        #     print(line)



repo_dir = ""
input = ""
output= ""
extract(repo_dir,input,output)
