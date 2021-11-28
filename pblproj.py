#import modules
import os
import shutil

#the current working directory
print('before:\n',os.getcwd())

#------------------------------------------------------------
#change the location here (for new test-cases)
fdpath=r"C:\Users\Priyanshi Jogi\Desktop\PBL PROJECT\TEST-2"
#------------------------------------------------------------

#changing the directory
os.chdir(fdpath)
print('after:\n',os.getcwd())

#printing file names...
print(os.listdir())

#to get extension
lst_extension=[]
#for unknown(ie.if there is no dot('.')),if extension is not specified
unknown=[]

for i in os.listdir():
    #print(i)
    if '.' in i:#(if true)
        #get the words after the dot
        extension= i.split(".")[-1]
        lst_extension.append(extension)
    else:#if false
        unknown.append(i)
#printing the file names after the dot
print(lst_extension)
#the unknown files
print('unknown files are:',unknown)
#making it set to remove duplicates
lst_extension=set(lst_extension)
print(lst_extension)
#print(os.environ)
#specifying at which path i want to create a folder and store the files
path=os.environ['UserProfile']+'\\'+ 'Desktop' + '\\' +'FILE MANAGER'

#os.mkdir(path)
#exception handling
try:
    shutil.rmtree(path)
    os.mkdir(path)
    os.mkdir(path+'\\'+'unknown')
    print('folder created')
except:
    os.mkdir(path)
    os.mkdir(path+'\\'+'unknown')
    print('folder created')
    
for ex in lst_extension:
    print(ex,end=',')
    os.mkdir(path+ '\\' + ex)
          
    for j in os.listdir():
        if ex in j:
            shutil.copy(j,path+ '\\'+ex +'\\')
            for i1 in os.listdir():
                if '.' in i1:
                    pass
                else:
                    shutil.copy(i1,path+ '\\'+ 'unknown' + '\\')


