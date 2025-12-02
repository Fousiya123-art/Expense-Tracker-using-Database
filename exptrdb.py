
import  sqlite3
conn=sqlite3.connect('exp.db')
c=conn.cursor()
c.execute("""
          CREATE TABLE IF NOT EXISTS expense
         (id INTEGER PRIMARY KEY AUTOINCREMENT,       
         category TEXT,
         price REAL,
         date  TEXT );
         """)
def Add_expense():
                  a=input("Enter your category/item")
                  b=float(input("Enter your price"))
                  date=input("Enter your date")
                  c.execute("""
              insert into expense(category,price,date)values(?,?,?);
        """,(a,b,date))
conn.commit()
def view_expense():
                   c.execute("""
                   select * from expense;
                   """)
                   rows = c.fetchall()
                   print("All Expenses/n")
                   print(rows)
def total_expense():
                    c.execute("""
                    select SUM(price) from expense;
    """)
                    total = c.fetchone()[0]
                    print("Total Expenses",total)
                    print(total)
while True:
    print("1.Add  2.View  3.Total  4.Exit")
    ch = input("Choice: ")
    if ch == "1":Add_expense()
    elif ch == "2":view_expense()
    elif ch == "3":total_expense()
    elif ch == "4": break







