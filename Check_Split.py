import math
def split_per_person(total_amount,number_of_people):
      if total_amount <=0:
            raise ValueError("Looks like it's a treat") 
      elif number_of_people <=1:
            raise ValueError("more than 1 person is required to split")
      else:
            return math.ceil(total_amount/number_of_people)

try:
      total_amount=float(input("Enter the total amount: "))
      number_of_people=int(input("Enter the number of people: "))
      print("Contribution per person is:",split_per_person(total_amount,number_of_people))
except ValueError as err:
      print("ops ,not a valid number:")
      print("{}".format(err))

