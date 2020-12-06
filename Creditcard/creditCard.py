# Write your code here
import random as rand
# Importing database module
import sqlite3

# Creating a connection
conn = sqlite3.connect('card.s3db')
# Creating a table

table = "CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);"
cur = conn.cursor()
cur.execute(table)
conn.commit()
def luhnCheck(cardNo):
    checkSum = list(cardNo)
    mySum = 0
    for j in range(0, 15):
        if j % 2 == 0:
            checkSum[j] *= 2
        if checkSum[j] > 9:
            checkSum[j] -= 9
        mySum += checkSum[j]
    if mySum % 10 == 0:
        cardNo.append(0)
    else:
        cardNo.append(10 - (mySum % 10))
    return cardNo

def isLuhn(cardNo):
    mylist = []
    val2 = []
    val = list(str(cardNo))
    val1 = list(str(cardNo))
    val.pop()
    for i in val:
        mylist.append(int(i))
    for j in val1:
        val2.append(int(j))
    if(val2 == luhnCheck(mylist)):
        return True
    else:
        return False

check = True
while check:
    resp = int(input("""1. Create an account
2. Log into account
0. Exit
>"""))

    if resp == 0:
        break
    elif resp == 1:
        cardNo = list()
        for i in range(0, 16):
            if i == 0:
                cardNo.append(4)
            elif 0 < i < 6:
                cardNo.append(0)
            elif 6 <= i < 15:
                cardNo.append(rand.randint(0, 9))
            else:
                ## Sumcheck
                cardNo = luhnCheck(cardNo)
        num = "".join([str(elm) for elm in cardNo])
        pin = list()
        for i in range(0, 4):
            pin.append(rand.randint(0, 9))
        newPin = "".join([str(elm) for elm in pin])
        # Populating database

        cur.execute("INSERT INTO card(number, pin) VALUES (?,?);", (num, newPin))
        conn.commit()
        print()
        print("Your card has been created")
        print("Your card number:")
        print(num)
        print("Your card PIN:")
        print(newPin)
        print()
    elif resp == 2:
        print("Enter your card number:")
        logCard = input(">")
        print("Enter you PIN:")
        logPin = input(">")
        cur.execute("SELECT * FROM card WHERE number = ?", (logCard,))
        conn.commit()
        value = cur.fetchone()
        if value:
            if int(value[2]) == int(logPin):
                print()
                print("You have successfully logged in!")
                while True:
                    print()
                    print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
                    resp1 = int(input(">"))
                    if resp1 == 1:
                        print()
                        cur.execute("SELECT balance FROM card WHERE number=?", (logCard,))
                        conn.commit()
                        print(cur.fetchall()[0])
                    elif resp1 == 2:
                        print("Enter income:")
                        income = int(input(">"))
                        cur.execute("SELECT balance FROM card where number=?", (logCard,))
                        conn.commit()
                        income += int(cur.fetchone()[0])
                        cur.execute("UPDATE card SET balance = ? where number = ?", (income, logCard))
                        conn.commit()
                        print("Income was added!")
                    elif resp1 == 3:
                        print("Enter card number:")
                        newCard = int(input(">"))
                        if isLuhn(newCard):
                            if cur.execute("SELECT balance FROM card where number=?", (newCard,)):
                                conn.commit()
                                bal11 = cur.fetchone()
                                if bal11:
                                    bal1 = int(bal11[0])
                                else:
                                    print("Such a card does not exist.")
                                    continue

                                if newCard == logCard:
                                    print("You can't transfer money to the same account!")
                                else:
                                    cur.execute("SELECT balance FROM card where number=?", (logCard,))
                                    conn.commit()
                                    bal = int(cur.fetchone()[0])
                                    print("Enter how much money you want to transfer:")
                                    trans = int(input(">"))
                                    if bal < trans:
                                        print("Not enough money!")
                                    else:
                                        bal1 += trans
                                        cur.execute("UPDATE card SET balance = ? where number = ?", (bal1, newCard))
                                        conn.commit()
                                        bal = bal - trans
                                        cur.execute("UPDATE card SET balance = ? where number = ?", (bal, logCard))
                                        conn.commit()
                                        print("Success!")
                            else:
                                conn.commit()
                                print("Such a card does not exist.")
                        else:
                            print("Probably you made a mistake in the card number. Please try again!")
                    elif resp1 == 4:
                        cur.execute("DELETE FROM card WHERE number = ?", (logCard,))
                        conn.commit()
                        print("The account has been closed!")
                        break
                    elif resp1 == 5:
                        print()
                        print("You have successfully logged out!")
                        break
                    elif resp1 == 0:
                        check = False
                        break
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")
        print()
print("Bye")
conn.close()
