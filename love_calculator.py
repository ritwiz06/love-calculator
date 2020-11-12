
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



lower_n1=name1.lower()
lower_n2=name2.lower()
f_name=lower_n1 + lower_n2
n_of_t = f_name.count("t")
n_of_r = f_name.count("r")
n_of_u = f_name.count("u")
n_of_e = f_name.count("e")
n_of_l = f_name.count("l")
n_of_o = f_name.count("o")
n_of_v = f_name.count("v")
n_of_e = f_name.count("e")
true= n_of_t + n_of_r + n_of_u + n_of_e
love = n_of_l + n_of_o + n_of_v + n_of_e
love_percent= str(true)+ str(love)
percentage_love= int(love_percent)
if percentage_love<10 or percentage_love>90:
  print(f"Your score is {percentage_love}, you go together like coke and mentos.")
elif 40 <= percentage_love <= 50 :
  print(f"Your score is {percentage_love}, you are alright together.")
else:
  print(f"Your score is {percentage_love}.")

