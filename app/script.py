import csv
import shutil
fresult=dict()
listenum=list()
import json
import pickle
import os

def andconv(vars):
    vars=vars.replace("and", "+")
    return vars

def dotconv(vars):
    sep=["in","-","->"]
    limst = vars.split()
    strin=""
    for i in range(1,len(limst)-1):
        varp=""
        if limst[i]=="in":
            varp='.'+ limst[i] +'.' +limst[i-1]
            strin=vars.replace(f"{limst[i-1]} {limst[i]} {limst[i+1]}", varp)
        '''
        strin=strin+limst[counter]+" "+ varp+" "
        if condition:
            counter=counter+1
        strin=strin+limst[counter]+" "+ varp+" "
        '''
    return strin

def ifelconv(vars):
    sep=["if","then","else"]

    limst=vars.split()
    strin1=""
    strin2=""
    strin3=""
    i1=0
    i2=0
    i3=len(limst)
    for i in range(0,len(limst)):
        if limst[i].lower()=="then":
            i2=i
        elif limst[i].lower()=="else":
            i3=i
    for i in range(i1+1,i2):
        strin1=strin1+limst[i]+" "
    for i in range(i2+1,i3):
        
        strin2=strin2+ limst[i] +" "
    for i in range(i3+1,len(limst)):
        strin3=strin3+limst[i]+" "
    value=eval(strin1)
    if value:
        return strin2
    else:
        return strin3

class Dict2Class():
      
    def __init__(self, obj):
        for key in obj:
            if type(obj[key]) is not dict and type(obj[key]) is not list:
                setattr(self, key, obj[key])
            elif type(obj[key]) is dict:
                setattr(self, key, Dict2Class(obj[key]))
            elif type(obj[key]) is list:
                if len(obj[key])!=1:
                    counter=0
                    for i in obj[key]:
                        setattr(self, f"{key}_{counter}", Dict2Class(i))
                        counter=counter+1
                else:
                    for i in obj[key]:
                        setattr(self, f"{key}", Dict2Class(i))
 

def main(location_a,location_b,nam):
    object= open(location_a)
    obj=json.load(object)

    result = Dict2Class(obj)
    shutil.copy(location_b,'/Users/pranavaggarwal/Downloads/json-transformation-main/data/app/uploads/mapping_copy.csv')
    file= open('/Users/pranavaggarwal/Downloads/json-transformation-main/data/app/uploads/mapping_copy.csv', newline='')
    with open(location_b, newline='') as csvfile:

        readr = csv.DictReader(csvfile)
        rdr= csv.reader(file)
        for r in rdr:

            strin=""
            for i in range(3,len(r)):
                if strin=="":
                    strin=r[i]
                else:
                    strin=strin+','+r[i]

            listenum.append(strin.strip())
        
        for row in readr:
            ENUM=dict()
            for i in listenum:
                if i[0]=='{':
                    i=i.replace("},", "}")
                    #ENUM=json.loads(i)
                    

            l=andconv(row[" Source"])
            #l=dotconv(row[" Source"])
            l=l.replace(" ."," result.")
            l=l.replace("(.","[result.")
            l=l.replace(")","]")
            #l=row[" Source"]
    
            stripped = [s.strip() for s in l]
            exp=""
            for i in stripped:
                condition=True
                '''
                if i[0:4]=='ENUM':
                    p=f"{i[5:-1]}"
                    exp=f"ENUM[{p}]"
                    condition=False
                    '''
                '''
                if exp=="":
                    exp="result"+i
                elif condition:
                    exp=exp+ "+" + " result"+i
                    '''
                exp=l

            
            if row[" Source"].strip().lower()[0:2]=="if":
                exp=ifelconv(row[" Source"].strip())
                
            fresult[row["Target"]]=(exp)
    fresult["Enumerations"]=listenum
    print(fresult)


    # Writing to sample.json
    name=nam
    location=os.path.join("/Users/pranavaggarwal/Downloads/json-transformation-main/data/app/transformers",f"{name}.pickle")
    with open(location,'wb') as handle:
        pickle.dump(fresult, handle, protocol=pickle.HIGHEST_PROTOCOL)
        


if __name__=="__main__":
    loca="/Users/pranavaggarwal/Downloads/json-transformation-main-3/data/sample_1/source.json"
    locb="/Users/pranavaggarwal/Downloads/json-transformation-main-3/data/sample_1/mapping.csv"
    main(loca,locb,"pranav")

