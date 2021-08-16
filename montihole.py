import random

def make_the_doors():
    
    doors = []
    zeropoint = 0
    
    for i in range(3):
        doors.append(random.randint(0,1))

        if doors[i] == 1:
            for x in range(2-i):
                doors.append(0)
            break

        else:
            zeropoint = zeropoint+1
        
        if zeropoint == 2:
            doors.append(1)
            break

    return doors

running = True

while running:
    
    algo = 0
    success = 0
    keep_or_quit = ""
    algo = int(input("what algo do you use? 0 or 1"))

    if algo == 0:
        
        for i in range(100000):

            want = 0
            doors = []
            want = random.randint(0,2)
            doors = make_the_doors()

            if doors[want] == 0:
                pass
            elif doors[want] == 1:
                success = success+1

        print("100000번 도전, {}번 성공".format(success))
        
    elif algo == 1:
        
        for i in range(100000):

            want = 0
            doors = []
            want = random.randint(0,2)
            doors = make_the_doors()
        
            if doors[want] == 1:
                pass
            elif doors[want] == 0:
                success = success+1
        
        print("100000번 도전, {}번 성공".format(success))
    
    keep_or_quit = input("keep or quit? k or q")
    if keep_or_quit == 'k':
        pass
    elif keep_or_quit == 'q':
        running = False
    

    







