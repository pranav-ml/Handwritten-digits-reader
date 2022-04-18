import network
from draw_pad import draw_num
import numpy as np
import pickle
x=1
to_learn=int(input("To teach,press 1.To load existing lesson,press 0\n"))
training_data=[None]*150
print(to_learn)
if to_learn==1:
    print("Learning mode:Draw number ONE (5 times)")
    for x in range(x,x+10):
        a=draw_num()
        td1=np.array((a),dtype=np.float32)
        td2=np.array(([1],[0],[0],[0],[0]))
        training_data[(x*3)-1-2]=tuple((td1,td2))
        training_data[(x*3)-1-1]=tuple((td1,td2))
        training_data[(x*3)-1]=tuple((td1,td2))
        
    print("Learning mode:Draw number TWO (5 times)")
    for x in range(x+1,x+11):
        a=draw_num()
        td1=np.array((a),dtype=np.float32)
        td2=np.array(([0],[1],[0],[0],[0]))
        training_data[(x*3)-1-2]=tuple((td1,td2))
        training_data[(x*3)-1-1]=tuple((td1,td2))
        training_data[(x*3)-1]=tuple((td1,td2))
        print(x)
    print("Learning mode:Draw number THREE (5 times)")
    for x in range(x+1,x+11):
        a=draw_num()
        td1=np.array((a),dtype=np.float32)
        td2=np.array(([0],[0],[1],[0],[0]))
        training_data[(x*3)-1-2]=tuple((td1,td2))
        training_data[(x*3)-1-1]=tuple((td1,td2))
        training_data[(x*3)-1]=tuple((td1,td2))
        
    print("Learning mode:Draw number FOUR (5 times)")
    for x in range(x+1,x+11):
        a=draw_num()
        td1=np.array((a),dtype=np.float32)
        td2=np.array(([0],[0],[0],[1],[0]))
        training_data[(x*3)-1-2]=tuple((td1,td2))
        training_data[(x*3)-1-1]=tuple((td1,td2))
        training_data[(x*3)-1]=tuple((td1,td2))
        
    print("Learning mode:Draw number FIVE (5 times)")
    for x in range(x+1,x+11):
        a=draw_num()
        td1=np.array((a),dtype=np.float32)
        td2=np.array(([0],[0],[0],[0],[1]))
        training_data[(x*3)-1-2]=tuple((td1,td2))
        training_data[(x*3)-1-1]=tuple((td1,td2))
        training_data[(x*3)-1]=tuple((td1,td2))
        
    file = open('digits.data', 'wb')
    pickle.dump(training_data, file)
    file.close()
        
        
        
file = open('digits.data', 'rb')
lesson_data = pickle.load(file)
net = network.Network([361, 20,  5])
net.SGD(lesson_data, 1000, 5, 1)
file.close()
keeptrying=0
print(len(training_data))
while keeptrying==0:
    
    print("Draw a number:")
    test=draw_num()
    test_data=np.array((test),dtype=np.float32)
    
    output = np.argmax(net.feedforward(test_data))+1

    print("You Drew Number:",output)
    print("To try again type 0, else type 1")
    keeptrying=int(input())