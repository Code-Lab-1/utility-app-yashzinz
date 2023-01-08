print("\n"+"\t\t"+"WELCOME TO VENDING MACHINE")
def vending_machine():
    
    drinks=[["COLA",2.50,"#01"],["SPRITE",2.50,"#02"],["FANTA",1.50,"#03"],["HOT CHOCOLATE",5.00,"#04"],["WATER",1.50,"#05"],["COLD COFFEE",2.50,"#06"]]
    chips=[["MAX",4.00,"#11"], ["LAYS",2.00,"#12"],["OMAN",2.50,"#13"]]
    chocolate=[["MARS",3.50,"#21"],["SNICKERS",2.50,"#22"],["GALAXY",3.50,"#23"]]
    ice_cream=[["IGLOO MARK UP ",2.50, "#31"],["IGLOO HYPER LOOP",2.50, "#32"],["MAGUM DOUBLE CHOCOLATE",7.25,"#33"],["MAGNUM CARAMEL",6.50,"#34"]]
    biscuits=[["BOURBON CHOCOLATE CREAM",7.00,"#41"],["RITZ CRACKERS",3.50,"#42"],["OREO COOKIE",3.00,"#43"]]
    entire=[drinks,chips,chocolate,ice_cream,biscuits]
   
    
    from tabulate import tabulate
    print("\n"+"\t"+"DRINKS")
    print(tabulate(drinks,headers=["ITEM","COST","ID"],tablefmt='fancy_grid',stralign='centre',numalign='centre'))
    print("\n"+"\t"+"CHIPS")
    print(tabulate(chips,headers=["ITEM","COST","ID"],tablefmt="fancy_grid",stralign='centre',numalign="centre"))
    print("\n"+"\t"+"CHOCOLATES")
    print(tabulate(chocolate,headers=["ITEM","COST","ID"],tablefmt="fancy_grid",stralign="centre",numalign='centre'))
    print("\n"+'\t'+"ICE CREAMS")
    print(tabulate(ice_cream,headers=["ITEM","COST","ID"],tablefmt="fancy_grid",stralign='left',numalign='centre'))
    print("\n"+'\t'+"BISCUITS")
    print(tabulate(biscuits,headers=["ITEM","COST","ID"],tablefmt="fancy_grid",stralign='left',numalign='centre'))

    selected=[]
    def total():
        Sum=sum(selected)
        print('YOUR TOTAL IS ',Sum)
        insert=float(input("PLEASE ENTER CASH:"))
        if insert>Sum:
            print('HERE IS YOUR CHANGE',insert-Sum)
            print("HERE! PLEASE COLLECT YOUR ITEMS")
            print("THANK YOU FOR PURCHASING WITH US")
        if insert<Sum:
            balance=float(input('INSUFFICIENT AMOUNT,PLEASE ENTER AED '+str(Sum-insert)))
            if balance>Sum-insert:
                print("Here is your balance,",balance-(Sum-insert))
                print('HERE!PLEASE COLLECT YOUR ITEMS')
                print('THANK YOU FOR PURCHASING WITH US.')
            if balance==Sum-insert:
                print('HERE! PLEASE COLLECT YOUR ITEMS')
                print("THANK YOU FOR PURCHASING WITH US!!")
        if insert==Sum:
            print('HERE!PLEASE COLLECT YOUR ITEMS')
            print("THANK YOU FOR PURCHASING WITH US")
        for i in selected:
            selected.remove(i)
    print("TO SELECT AN ITEM, INSERT THE ITEM ID")
    print('TO EXIT THE VENDING MACHINE, ENTER '+'\''+'quit'+'\'')                          
    while True:
        qn1=input("\n"+"ENTER THE ITEM ID:")
             
        for i in entire:
            for x in i:
                if qn1==x[2]:
                    selected.append(x[1])
                    
                    print("A "+x[0]+" WILL BE DISPENSED SHORTLY")
                    if qn1==entire[0][0][2]:
                        qn3=input("WOULD YOU ALSO LIKE TO GET A "+entire[1][0][0]+' CHIPS ALONG WITH YOUR DRINK Y/N:')
                        if qn3=='Y':
                            selected.append(entire[1][0][1])
                            print(entire[1][0][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                            
                        if qn3=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET ANYTHING ELSE?")
                            
                    elif qn1==entire[0][1][2]:
                        qn4=input("WOULD YOU ALSO LIKE TO GET A "+entire[1][1][0]+' CHIPS ALONG WITH YOUR DRINK Y/N:')
                        if qn4=='Y':
                            selected.append(entire[1][1][1])
                            print(entire[1][1][0]+" WILL BE ADDED TO YOUR PURCHASE")
                            total()
                            for i in selected:
                                selected.remove(i)                   
                        if qn4=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET SOMETHING ELSE?")

                    elif qn1==entire[0][2][2]:
                        qn5=input("WOULD YOU ALSO LIKE TO GET A "+entire[1][2][0]+' CHIPS ALONG WITH YOUR DRINK Y/N:')
                        if qn5=='Y':
                            selected.append(entire[1][2][1])
                            print('An '+entire[1][2][0]+'  WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn5=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET SOMETHING ELSE?")
                    elif qn1==entire[0][3][2]:
                        qn6=input("WOULD YOU ALSO LIKE TO GET A "+entire[4][0][0]+' BISCUIT ALONG WITH YOUR DRINK Y/N:')
                        if qn6=='Y':
                            selected.append(entire[4][0][1])
                            print('A '+entire[4][0][0]+' COOKIE WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn6=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET SOMETHING ELSE?")
                    elif qn1==entire[0][4][2]:
                        qn7=input("WOULD YOU ALSO LIKE TO GET A "+entire[4][1][0]+' ALONG WITH YOUR DRINK Y/N:')
                        if qn7=='Y':
                            selected.append(entire[4][1][1])
                            print('A '+entire[4][1][0]+'  WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn7=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET SOMETHING ELSE?")
                    elif qn1==entire[0][5][2]:
                        qn8=input("WOULD YOU ALSO LIKE TO GET A "+entire[4][2][0]+'  ALONG WITH YOUR DRINK Y/N:')
                        if qn8=='Y':
                            selected.append(entire[4][2][1])
                            print('An '+entire[4][2][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn8=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO GET SOMETHING ELSE?")
                    elif qn1==entire[1][0][2]:
                        qn9=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][0][0]+' ALONG WITH YOUR CHIPS Y/N:')
                        if qn9=='Y':
                            selected.append(entire[0][0][1])
                            print('A '+entire[0][0][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn9=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[1][1][2]:
                        qn10=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][1][0]+' ALONG WITH YOUR CHIPS? Y/N')
                        if qn10=='Y':
                            selected.append(entire[0][1][1])
                            print('A '+entire[0][1][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn10=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[1][2][2]:
                        qn11=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][2][0]+' ALONG WITH YOUR CHIPS? Y/N')
                        if qn11=='Y':
                            selected.append(entire[0][2][1])
                            print('A '+entire[0][2][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn11=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[2][0][2]:
                        qn12=input("WOULD YOU ALSO LIKE TO GET AN "+entire[3][0][0]+' ALONG WITH YOUR CHOCOLATE? Y/N')
                        if qn12=='Y':
                            selected.append(entire[3][0][2])
                            print('AN '+entire[3][0][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn12=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[2][1][2]:
                        qn13=input("WOULD YOU ALSO LIKE TO GET AN "+entire[3][1][0]+' ALONG WITH YOUR CHOCOLATE? Y/N')
                        if qn13=='Y':
                            selected.append(entire[3][1][1])
                            print('AN '+entire[3][1][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn13=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")        
                    elif qn1==entire[2][2][2]:
                        qn14=input("WOULD YOU ALSO LIKE TO GET A "+entire[3][2][0]+' ALONG WITH YOUR CHOCOLATE? Y/N')
                        if qn14=='Y':
                            selected.append(entire[3][2][1])
                            print('A '+entire[3][2][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn14=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")                 
                    elif qn1==entire[3][0][2]:
                        qn15=input("WOULD YOU ALSO LIKE TO GET A "+entire[2][0][0]+' CHOCOLATE BAR ALONG WITH YOUR ICE CREAM? Y/N')
                        if qn15=='Y':
                            selected.append(entire[2][0][1])
                            print('A '+entire[2][0][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn15=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[3][1][2]:
                        qn16=input("WOULD YOU ALSO LIKE TO GET A "+entire[2][1][0]+' CHOCOLATE BAR ALONG WITH YOUR ICE CREAM? Y/N')
                        if qn16=='Y':
                            selected.append(entire[2][1][1])
                            print('A '+entire[2][1][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn16=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[3][2][2]:
                        qn17=input("WOULD YOU ALSO LIKE TO GET A "+entire[2][2][0]+' CHOCOLATE BAR ALONG WITH YOUR ICE CREAM? Y/N')
                        if qn17=='Y':
                            selected.append(entire[2][2][1])
                            print('A '+entire[2][2][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn17=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[3][3][2]:
                        qn18=input("WOULD YOU ALSO LIKE TO GET A "+entire[1][0][0]+' CHIPS ALONG WITH YOUR ICE CREAM? Y/N')
                        if qn18=='Y':
                            selected.append(entire[1][0][1])
                            print('A '+entire[1][0][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn18=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[4][0][2]:
                        qn19=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][3][0]+' ALONG WITH YOUR BISCUITS? Y/N')
                        if qn19=='Y':
                            selected.append(entire[0][3][1])
                            print('A '+entire[0][3][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn19=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[4][1][2]:
                        qn20=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][4][0]+' ALONG WITH YOUR BISCUITS? Y/N')
                        if qn20=='Y':
                            selected.append(entire[0][4][1])
                            print('A '+entire[0][4][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn20=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
                    elif qn1==entire[4][2][2]:
                        qn21=input("WOULD YOU ALSO LIKE TO GET A "+entire[0][5][0]+' ALONG WITH YOUR OREO COOKIE? Y/N')
                        if qn21=='Y':
                            selected.append(entire[0][5][1])
                            print('A '+entire[0][5][0]+' WILL BE ADDED TO YOUR PURCHASE')
                            total()
                            for i in selected:
                                selected.remove(i)
                        if qn21=='N':
                            total()
                            for i in selected:
                                selected.remove(i)
                            print("WOULD YOU LIKE TO BUY ANYTHING ELSE?")
        if qn1=='quit':
            break
vending_machine()       
