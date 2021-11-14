import time, os


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    Menu = "    M E N U   G L O W N E  \n" + "1 - Wylicz ile potrzebujesz bazy nikotynowej \n" + "0 - Zakoncz program        \n";
    print("Witaj w programie")
    while(True):
        print(Menu)
        if(input()=="1"):
            clear()
            try:
                ilosc = float(input("Podaj ile bedziesz robic liquidu(ml): "))
                moc = float(input("Podaj jaka chcesz uzyskac moc roztworu(mg/ml): "))
                moc_tworcza = 72 #float(input("Podaj sile pierdolniecia bazy nikotynowej: "))
                wynik = moc*ilosc/moc_tworcza
                print("Bedzuesz potrzebowal: ", round(wynik, 4), " ml danej bazy nikotynowej (72mg/ml) na ", ilosc, "ml roztowu")
                print("Koszt nikotyny ktora trzeba dodac wynosi: ", round(wynik*1.5, 2), " PLN")
                print("Koszt bazy wynosi: ", round(ilosc*44/1800, 2), " PLN")
                print("Razem daje to: ", round((wynik*1.4) + (ilosc*50/1800), 2), " PLN")
            except:
                print("An error occurred, try again.")
                time.sleep(2)
                clear()
        else:
            exit(0)