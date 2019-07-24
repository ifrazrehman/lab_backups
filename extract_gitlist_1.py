import sys, os
import io
from subprocess import check_output

#create git hash lists that contain README
def githashlist_withreadme(repo_dir,commitlist_path):
    os.chdir(repo_dir)
    # str = os.popen("git log --pretty=format:%H -- README.md > " + output_path).read()
    str = os.popen("git log --pretty=format:%H -- CONTRIBUTE.md").read()
    gitlist_file = open(commitlist_path, 'w')
    gitlist_file.write(str)
    gitlist_file.close()

def githashlist_all(repo_dir,commitlist_path):
    os.chdir(repo_dir)
    # str = os.popen("git log --pretty=format:%H -- README.md > " + output_path).read()
    str = os.popen("git log --pretty=format:%H").read()
    gitlist_file = open(commitlist_path, 'w')
    gitlist_file.write(str)
    gitlist_file.close()

###SETTING PATH here
repo_dir = "/Users/pongbhop/Documents/gitRepository/npm/"
gitlist_all = "/Users/pongbhop/Documents/python_workstation/npmrepo/npm_gitlist_all.txt"
gitlist_withreadme = "/Users/pongbhop/Documents/python_workstation/Prelim/output/npm_gitlist_withreadme.txt"
database1_path = "/Users/pongbhop/Documents/python_workstation/nd
githashlist_withreadme(repo_dir,gitlist_withreadme)
githashlist_all(repo_dir,gitlist_all)
