def get_dates_between_dates(date):
    yy,mm,dd = date.split('-')
    
    if ((int(yy)%4==0 and int(yy)%100!=0) or int(yy)%400==0):
        day=(((int(yy)*365)+1)+int(mm)*30+int(dd))
    else:
        day=(int(yy)*365+int(mm)*30+int(dd))
        
    return day
    
def get_elapsed_date(d1, d2):
    date1 = get_dates_between_dates(d1)
    date2 = get_dates_between_dates(d2)
    a = date2 - date1
    return a
    
def main():
    dates = [("2022-10-15", "2024-9-19", 705),
             ("2020-1-15", "2023-3-15", 1154),
            ]
            
    for ele in dates:
        days = get_elapsed_date(ele[0], ele[1])
        print(days, end=" ")
        
        if (days!=ele[2]):
        
            print("fail")
        else:
            print("pass")
if (__name__=="__main__"):
    main ()
