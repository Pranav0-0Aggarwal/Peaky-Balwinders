import csv
import shutil
import pickle
fresult=dict()
listenum=list()
import json
object= open("/Users/pranavaggarwal/Downloads/json-transformation-main/data/sample_2/source.json")
object2="/Users/pranavaggarwal/Downloads/json-transformation-main/data/app/transformers/pranav.pickle"
obj=json.load(object)
with open(object2,"rb") as f:
    obj2 = pickle.load(f)


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
 

if __name__ == "__main__":
    result= Dict2Class(obj)
    listenum=obj2["Enumerations"]
    ENUM=dict()
    counter=0
    for i in obj2.keys():
    
        if i =="Enumerations":
            break
        temp=listenum[counter].replace("{","")
        temp=temp.replace("}","")
        if listenum[counter]=="{":
            message="Hi"
            print(temp)
            print(listenum[counter])
            if listenum[counter]=="{}":
                continue
            ENUM=json.loads(listenum[counter])
        #fresult[i]=eval(obj2[i].strip())
        #ENUM=json.loads(listenum[counter])
        print(counter)
        counter=counter+1

    print(fresult)
        

