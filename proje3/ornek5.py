import os
def delete_files():
    dextensions = [".aux" , ".bbl" , ".lof" , ".log" , ".lot" , ".out" , ".toc"]
    files=os.listdir()
    dfiles=[]

    for file in files:
        if file[len(file)-4:]in dextensions:
            dfiles.append(file)

    for file in dfiles:
        os.remove(file)
delete_files()