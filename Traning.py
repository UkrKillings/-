import random
import time

print("Тренируйся и развлекайся UkrKillent")

def main():
    start = str(input("Введите [1] для капчи с цифрами:"
                      "Введите [2] для капчи с буквами:  "))
    while True:
        if start == "1":
            capha = (''.join([random.choice(list('1234567890')) for x in range(5)]))
            print("\n" + str('Капча: ' + capha))
            start_time = time.time()
            vvod = input("Ваша купча: ")
        if start == "2":
            capha = (''.join([random.choice(list('1234567890qwertyuiop')) for x in range(5)]))
            print("\n" + str('Купча: ' + capha))
            start_time = time.time()
            vvod = input("Ваша купча: ")
        if vvod == capha:
            times = (time.time() - start_time)
            print("--- " + str('%.1f' % times) + " seconds ---")
            print("Маладец, капча введена правельно! \n")

        else:
            print("Купча введена не верно \n")
                    

main()