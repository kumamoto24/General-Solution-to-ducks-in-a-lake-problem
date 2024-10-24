import random
try:
    duck_number = int(input("How many ducks are in the lake?\n池塘有几只鸭子？\n池には何羽のアヒルがいますか?"))
    test_time = int(input("How many times do you want to test? \n你想要实验多少次？\n何回テストしますか? "))
except ValueError:
    print("You must enter an integer!\n你必须输入一个整数\n整数を入力する必要があります")
hit = 0

def compare(sample):
    for i in range(1,len(sample)):
        if sample[i] - sample[i-1] > 0.5:
            return True

for i in range(test_time):
    sample = []
    
    for n in range(duck_number):
        sample.append(random.random())
        
    sample.sort()
    if (sample[-1] - sample[0] < 0.5) or compare(sample) == True:
        hit += 1


print(f"The probability of {duck_number} ducks staying in a same semicircle is {hit/test_time*100}%")
        
    
    
