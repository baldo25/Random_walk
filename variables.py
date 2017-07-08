''' Variables support file to be imported in main file

This file contains all variables declare and will be imported to main file '''

# Initially defining variables to 0, will be further appended.

test= " This is test sentence to check if it is working "


E = 0  # Equity
# Capitals
ini_cap = 0     # Initial Capital
curr_cap = 0    # Current Capital
invest_cap = 0  # Invested Capital
avail_cap = 0   # Available Capital


# Prices
pe = 0      # Entry Prices
ps1 = 0     # Stop Price 1
ps2 = 0     # Stop Price 2
pp1 = 0     # Profit Price 1
pp2 = 0     # Profit price 2
pp3 = 0     # Profit price 3
pp4 = 0     # Profit price 4

pstn = 0    # Position

N = input("Enter the Entry Amount")       # Entry Amount

# Win/loss Ration = wlr%
wlr30 = 0.3
wlr40 = 0.4
wlr50 = 0.5
wlr60 = 0.6
wlr70 = 0.7

l = 0       # Loop number range(1-2000)

# Exit Percentages
a = 0       # the percentage that is sold at Pp1
b = 0       # the percentage that is sold at Pp2
c = 0       # the percentage that is sold at Pp3
d = 0       # the percentage that is sold at Pp4
g = 0       # the percentage that is sold at Ps1
h = 0       # the percentage that is sold at Ps2

# Risk Percentage range(0.5,2.5)
rsk = 0

# Profit
profit1 = (pp1-pe)*N*a
profit2 = (pp2-pe)*N*b
profit3 = (pp3 - pe)*N*c
profit4 = (pp4 -pe)*N*d

# Loss
loss1 = (ps1 - pe)*N*g
loss2 = (ps2 - pe)*N*h
