import StatCalcFun
import Utils
# initialize startup variable

state = True

while state is True:
    print("STAT_CALC_APP_ ver1.0.0\n")
    print("FUNCTION LIST")
    print("\t1. Independent T test")
    print("\t2. Independent T test (raw)")
    print("\t3. Find mean")
    print("\t4. Find standard deviation")
    print("\t5. Independent T test (raw)")
    print("\t6. Independent T test (param)")
    print("\t7. Goodness of fit test (chi-square) - equal expectation")
    print("\t8. Independence test ")

    print()
    print("ENTER 0 TO EXIT")
    try:
        n = int(input("Enter your option >> "))
        if n == 0:
            break
        elif n == 1:
            again = True
            while again:
                print("\tIndependent T test\n")
                n1 = int(input("Enter data(n1) size >> "))
                n2 = int(input("Enter data(n2) size >> "))
                x1 = float(input("Enter value(x1) >> "))
                x2 = float(input("Enter value(x2) >> "))
                s1 = float(input("Enter value(s1) >> "))
                s2 = float(input("Enter value(s2) >> "))
                print(StatCalcFun.independent_t_test(x1, x2, s1, s2, n1, n2))
                again = Utils.againprompt()
        elif n ==2:
            print("Developing.....")

        elif n == 3:
            again = True
            while again:
                print("\tCalculate mean by entering sample data (numbers) >> ")
                print(StatCalcFun.my_mean(StatCalcFun.set_list()))
                again = Utils.againprompt()

        elif n == 4:
            again = True
            while again:
                print("\tCalculate standard deviation by entering sample data (numbers) >> ")
                print(StatCalcFun.standard_deviation(StatCalcFun.set_list()))
                again = Utils.againprompt()

        elif n == 5:
            again = True
            while again:
                print("\tDependent t test (raw)")
                print(StatCalcFun.dependent_t_test(StatCalcFun.set_list(), StatCalcFun.set_list()))
                again = Utils.againprompt()

        elif n == 6:
            again = True
            while again:
                print("\tDependent t test (param) ")
                _d = float(input("Enter _d >> "))
                sd = float(input("Enter sd >> "))
                nd = int(input("Enter nd >> "))
                print(StatCalcFun.dependent_t_test(_d, sd, nd))
                again = Utils.againprompt()

        elif n ==7:
            again = True
            while again:
                print("\tGoodness of fit test")
                print(StatCalcFun.goodness_of_fit(StatCalcFun.set_list()))
                again = Utils.againprompt()

        elif n == 8:
            again = True
            while again:
                print("\t8. Independence test ")
                print(StatCalcFun.independence_test(Utils.get_2Matrix()))
                again = Utils.againprompt()

    except ValueError:
        print("I told you to enter a number right? ")

    except:
        print("Stop messing here, just enter a number already! ")


