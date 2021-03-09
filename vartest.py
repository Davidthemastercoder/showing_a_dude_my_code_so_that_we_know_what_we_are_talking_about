var = "lqqqqqqqqqqqq=2;"
command = " prit;"
ri = 0
i = 0
state2 = 0
state = 0
var_name = ""
var_val = ""
sec = True
while i< len(var):
    if var[i].isalpha() and state == 0:
        
        state =  0
        var_name = var_name + var[i]
        i = i + 1
        #print (var_name)
        
        if var[i] == "=" and state == 0:
             i = i + 1
             state = 2
    if state == 2:
        var_val = var_val + var[i]
        i = i +1 
        if var[i] == ";":
            #print(var_name , var_val)
            break

status = 0
while ri<len(command):
    if command[ri] == " " and sec == True:
        ri = ri +1
        if command[ri] != " ":
            state2 = 0
        
    if command[ri] == "p" and state2 == 0:
       state2 = 1
       ri= ri+1
    if command[ri] == "r" and state2 == 1:
        state2 = 2
        ri = ri + 1
    if command[ri] == "i" and state2 == 2:
        state2 = 3
        ri = ri + 1
    if command[ri] == "t" and state2==3:
        state2 = 4
        ri = ri +1
    if command[ri] == ";" and state2 == 4:
        ri = ri +1
        print(var_val)
        break
    
def iftry(String):
    some = 1
    compare = ""
    i2 = 0
    status = 0
    while i2 < len(String):
        #print(status)
        if String[i2] == " " and status == 0:
           i2 = i2 +1
           print(String[i2])
           print("Status is" , status)
           if String[i2] != " ":
              
              status = 1
              
        if String[i2] == "i" and status == 1:
              print("Status is" , status)
              i2 = i2 +1
              status = 2
              print(String[i2])
              print("Status is" , status)
        if String[i2] == "f" and status == 2:
               i2 = i2 + 1
               #status = 3
               print(String[i2])
               print("Status is" , status)
               status = 4
        #if String[i2] == " " and status == 3:
              #i2 = i2 +1
              #print(String[i2])
              #if String[i2] != " ":
                  #print(String[i2])
               
        if status == 4 and String[i2] == "(":
            i2 = i2 + 1
            print("Status is" , status)
            status = 5
            
            
        if status == 5 and String[i2] == "$":
           print(String[i2])
           i2 = i2 +1
           status = 6
           
        if status == 6 and String[i2] == "<":
            print("Status is" , status)
            print(String[i2])
            i2 = i2 + 1
            status = 7
            
            
        if status == 7 and unicode(String[i2], "utf-8").isnumeric() == True:
            compare = compare + String[i2]
            i2 = i2 +1
            print("Status is" , status)
            status = 7
            if unicode(String[i2] , "utf-8").isnumeric() == False:
               # i2 = i2 +1
                status = 8
            
      
                 
                #print(String[i2])
     
        if status == 8 and String[i2] == ")":
            print String[i2]
            #print(String[i2])
            #print(compare)
            comparer(compare)
            break

def comparer(val):
    if int(var_val) < int(val):
        print("varval is lower then compare val")
    if  int (var_val) > int(val):
        print("varval is higher then compare val")
        

iftry(" if($<5)")   
