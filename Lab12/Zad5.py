def run():
    while True:
        try:
            masa = float(input("Wprowadź swoją wagę w kilogramach: "))
        except ValueError:
            continue
        else:
            if masa < 0:
                print("Wprowadziłeś niewłaściwą wagę ")
                continue
            else:
                break

    while True:
        try:
            wzrost = float(input("Wprowadź swój wzrost w metrach: "))
        except ValueError:
            continue
        else:
            if wzrost < 0:
                print("Wprowadziłeś niewłaściwy wzrost")
                continue
            else:
                break

    bmi = masa / (wzrost * wzrost)

    if bmi < 18.5:
        print(f"Masz niedowagę, Twoje BMI wynosi : {bmi}" )
    elif 18.5 <= bmi < 25:
        print(f"Twoja waga jest prawidłowa, Twoje BMI wynosi {bmi}")
    elif 25 <= bmi < 30:
        print(f"Masz nadwagę, Twoje BMI wynosi : {bmi}")


run()