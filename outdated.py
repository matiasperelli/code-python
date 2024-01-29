months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    txt = input("Date: ")

    try:
        Y = txt.split('/')[2]
        M = int(str(txt.split('/')[0]))
        D = int(str(txt.split('/')[1]))
        if M <= 12:
            print(f"{Y}-{M:02}-{D:02}")
            break
    except:
        YYYY = txt.split(' ')[2]
        MM = txt.split(' ')[0]
        DD = txt.split(',')[0]
        if MM in months:
            ND = int(str(DD.split(' ')[1]))
            NM = months.index(MM)
            if ND <= 31:
                print(f"{YYYY}-{NM+1:02}-{ND:02}")
                break

#Harvard CS50
