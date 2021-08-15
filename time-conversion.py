while True :
 print("Converse To Second , Minute , Hour , Day , Year ")
 con = str(input('What you Whant to convert ? (second / minute / hour / day / year) : '))
 value=float(input('Enter The Value : '))
 ct = str(input('What You Want to convers to ? (s/m/h/d/y) : '))
 if con == "second" :
        if ct == "s" :
            print(f"There is : {value} second")
        elif ct == "m" :
            print(f"There is : {value / 60 } minute in {value} second ")
        elif ct =="h" :
            print(f"There is : {value / (60*60)} hour in {value} second ")
        elif ct == "d" :
            print(f"There is : {value / (24*60*60)} day in {value} second")
        elif ct == "y":
            print(f"There is : {value / (365*30*24*60*60)} year in {value} second")
 elif con == "minute" : 
        if ct == "s" :
            print(f"There is : {value * 60} second in {value} minute")
        elif ct == "m" :
            print(f"There is : {value} minute")
        elif ct =="h" :
            print(f"There is : {value /(60*60)} hour in {value} minute ")
        elif ct == "d" :
            print(f"There is : {value /(24*60*60)} day in {value} minute ")
        elif ct == "y":
            print(f"There is : {value /(365*30*24*60*60)} year in {value} minute ")
 elif con =="hour" :
        if ct == "s" :
            print(f"There is : {value * (60 *60 )} second")
        elif ct == "m" :
            print(f"There is : {value * 60 } minute in {value} hour  ")
        elif ct =="h" :
            print(f"There is : {value} hour")
        elif ct == "d" :
            print(f"There is : {value / (24)} day in {value} hour ")
        elif ct == "y":
            print(f"There is : {value / (365*30*24*60)} year in {value} hour")
 elif con == "day" :
        if ct == "s" :
            print(f"There is : {value * 86400 } second in {value} day")
        elif ct == "m" :
            print(f"There is : {value * 1440} minute in {value} day")
        elif ct =="h" :
            print(f"There is : {value * 24} hour in {value} day ")
        elif ct == "d" :
            print(f"There is : {value} day")
        elif ct == "y":
            print(f"There is : {value / (365)} year in {value} second")
 elif con == "year":

        if ct == "s" :
            print(f"There is : {value * (365 * 24 * 60*60 )}in {value} year ")
        elif ct == "m" :
            print(f"There is : {value * 525600} minute in {value} year  ")
        elif ct =="h" :
            print(f"There is : {value * 8760} hour in {value} year")
        elif ct == "d" :
            print(f"There is : {value * (365)} day in {value} year ")
        elif ct == "y":
            print(f"There is : {value} year")
 else :
        print("Error")
 g = str(input('Again?(y/n):'))
 if g == "y":
  True
 elif g == "n":
  break


