import time  # import the time module

def countdown(t): # define a function named countdown with a parameter t
    while t: # while t is not 0
        mins, secs =divmod(t, 60) # divmod() returns quotient and remainder
        timer = ' {:02d}:{:02d}'.format(mins,secs) # format the output
        print(timer,end='\r') # end='\r' is used to print the output in the same line
        time.sleep(1) # sleep for 1 second
        t -= 1 # decrement the value of t by 1
    print('Fire in the hole!') # print the message when the countdown is over

t = input("Enter the time in seconds: ") # input the time in seconds from the user

countdown(int(t)) # call the function with the input time in seconds




