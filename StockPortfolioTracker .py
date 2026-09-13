# ✅ TASK 2: Stock Portfolio Tracker
# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock prices.
# ● Simplified Scope:
# ○ User inputs stock names and quantity.
# ○ Use a hardcoded dictionary to define stock prices
# (e.g., {"AAPL": 180, "TSLA": 250}). 
# ○ Display total investment value and optionally save the result in a .txt or .csv file. 
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional). 


stocks={
       'APPL': 180,
       'TSLA':250,
       'GOOG':150
       }
portfolio=[]
total_investment=0
print("========== STOCK PORTFOLIO ==========")
n=int(input('How many stocks do you want to add:'))

for i in range(n):
    stock=input('Enter Stock Name:').upper()
    quantity=int(input('Enter a Quantity:'))
    if stock in stocks:
        price=stocks[stock]
        value=price*quantity
        
        total_investment += value
        
        portfolio.append(
            
                f'{stock}|Price: rs{price} | Quality:{quantity} |Value:{value}'
            
        )
    else:
        print('Stock is not available')
print()

for item in portfolio:
    print(item)
print()
print("Total Investment: Rs", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("========== STOCK PORTFOLIO ==========\n")

    for item in portfolio:
        file.write(item + "\n")

    file.write(f"\nTotal Investment: Rs{total_investment}\n")

print("Portfolio saved successfully in portfolio.txt")
    
    



    