import numpy as np




if __name__=="__main__":
    array1 = [0]*10
    np_array1 = np.array(array1)
    np_array1[0:2]+=2
    print(np_array1)