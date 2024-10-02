import numpy as np

def calculate(list):
    try:
        if list.size <9 :
            raise ValueError
        elif list.size >9:
            print ("only 9 fisrt numbers will be considered")
            list2 = list[0:9]
        else :
            list2 = list
        list3 = list2.reshape(3,3)
        mean = np.mean
        variance = np.var
        std = np.std
        max = np.max
        min = np.min
        sum = np.sum
        npFunc =[mean, variance, std, max, min, sum]
        calculations = {}
        for func in npFunc :
            res0 = func(list3,axis=0)
            res1 = func(list3,axis=1)
            res2 = func(list3,axis=None)
            calculations[func.__name__] = [res0.tolist() , res1.tolist(), res2.tolist()]
        calculations["standard deviation"] = results.pop("std")
        calculations["variance"] = results.pop("var")
        print(calculations)
        
    except ValueError:
        print("List must contain nine numbers.")
    return calculations
