import random

while True:
    number = random.randint(1, 100)

    for i in range(1, 6):
        print("تلاش", i, "از 5")
        print("فرصت باقی‌مانده:", 6 - i)

        guess = input("عدد را حدس بزن: ")

        if not guess.isdigit():
            print("ورودی نامعتبر است")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد")
            continue

        if guess == number:
            print("برنده شدی")

            if i == 1:
                print("رتبه: عالی")
            elif i == 2:
                print("رتبه: بسیار خوب")
            elif i == 3:
                print("رتبه: خوب")
            elif i == 4:
                print("رتبه: قبول")
            else:
                print("رتبه: با شانس بردی")

            break

        if guess < number:
            print("عدد بزرگ‌تری وارد کن")
        else:
            print("عدد کوچک‌تری وارد کن")

        difference = abs(number - guess)

        if difference <= 5:
            print("خیلی نزدیک هستی")
        elif difference <= 15:
            print("نزدیک هستی، ولی هنوز فاصله داری")
        else:
            print("خیلی دور هستی")

    if guess != number:
        print("باختی، عدد مخفی:", number)

    again = input("دوباره بازی می‌کنی؟ (y/n): ")

    if again != "y":
        break