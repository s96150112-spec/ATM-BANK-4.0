balance = 0
name = ""
pin = ""

def load_data():
    global balance, name, pin
    try:
        file = open("bank_data.txt", "r")
        data = file.readlines()
        name = data[0].strip()
        pin = data[1].strip()
        balance = int(data[2].strip())
        file.close()
        print("✅ Old account loaded successfully")
    except:
        print("🆕 Creating new account")

def save_data():
    file = open("bank_data.txt", "w")
    file.write(name + "\n")
    file.write(pin + "\n")
    file.write(str(balance))
    file.close()
    print("💾 Data saved successfully")

def create_bank_account():
    global balance, name, pin
    load_data()
    if name == "":
        name = input('enter the name: ')
        age = int(input('enter the age: '))
        if age >= 18:
            pin = input('set a 4-digit pin: ')
            balance = int(input('enter opening balance: Rs.'))
            save_data()
            print('\n~~~~account created successfully~~~~')
            print('NAME =', name)
            print('AGE =', age)
            print('BALANCE = Rs.', balance)
        else:
            print('\n\t —— SORRY YOU ARE MINOR ——')
            print('parents come')
            exit()
    else:
        print('\n~~~~Welcome back', name, '~~~~')
        print('BALANCE = Rs.', balance)

def deposit_money():
    global balance, pin
    entered_pin = input('enter pin to deposit: ')
    if entered_pin == pin:
        amount = int(input('enter the deposit amount: Rs.'))
        balance = balance + amount
        save_data()
        print('deposite amount RS =', amount)
        print('your amount deposited successfully')
        print('NEW BANK BALANCE = Rs.', balance)
    else:
        print('❌ Wrong PIN! Please enter correct pin')

def withdraw_money():
    global balance, pin
    entered_pin = input('enter pin to withdraw: ')
    if entered_pin == pin:
        amount = int(input('enter the withdraw amount: Rs.'))
        if amount <= balance:
            balance = balance - amount
            save_data()
            print('withdraw amount RS =', amount)
            print('your amount withdraw successfully')
            print('REMAINING BANK BALANCE = Rs.', balance)
        else:
            print('Insufficient Bank Balance please check bank balance')
    else:
        print('❌ Wrong PIN! Please enter correct pin')

def check_balance():
    global pin
    entered_pin = input('enter pin to check balance: ')
    if entered_pin == pin:
        print('\n———account details———')
        print('name =', name)
        print('balance = Rs.', balance)
    else:
        print('❌ Wrong PIN! Access Denied')

def add_interest():
    global balance, pin
    entered_pin = input('enter pin to add interest: ')
    if entered_pin == pin:
        rate = 5
        months = int(input('enter months to calculate: '))
        interest = balance * rate * months / (100 * 12)
        balance = balance + int(interest)
        save_data()
        print('\n💰 INTEREST ADDED 💰')
        print('Months =', months)
        print('Interest @ 5% = Rs.', int(interest))
        print('NEW BANK BALANCE = Rs.', balance)
    else:
        print('❌ Wrong PIN! Access Denied')

create_bank_account()

while True:
    print('\n\t———BMW BANK 4.0———')
    print('1. deposit money')
    print('2. withdraw money')
    print('3. check balance')
    print('4. add interest')
    print('5. exit')
    choice = int(input('enter your choice(1-5): '))
    if choice == 1:
        deposit_money()
    elif choice == 2:
        withdraw_money()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        add_interest()
    elif choice == 5:
        print('thank you visit again', name)
        break
    else:
        print('invalid choice please select (1-5)')
