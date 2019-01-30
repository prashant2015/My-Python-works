TICKET_PRICE=10
service_charge=2
REMAINING_TICKET=100

def price_cal(no_of_tickets):
      
      return (no_of_tickets*TICKET_PRICE)+service_charge

while REMAINING_TICKET >=1:
      print("Tickets Remaining {}. ".format(REMAINING_TICKET))

      #gather user name and assign it to new variable#

      name=input("What is your name ")

      #ask user how many tickets he/she want#
      try:
            no_of_tickets=int(input("hey {} how many tickets do you want to buy ".format(name)))
            if no_of_tickets > REMAINING_TICKET:
                  raise ValueError ("There are only {} number of tickets".format(REMAINING_TICKET))

      # except value error & handle in code #
      except ValueError as err:
            print("Oh no some thing went wrong {}, please try again: ".format(err))
      #ValueError 
      
      #calculate the price#
      else: 
            total_price=price_cal(no_of_tickets)

      #output the price#
            print(" Total due is ${} ".format(total_price))

            #promt user if they want to buy the tickets#
            confirm=input("Please press Y to proceed or any other key to cancel the transaction ")

            #decrement the tickets from total tickets#
            if confirm.lower()=='y':
                  print("TICKET SOLD")
                  REMAINING_TICKET -=no_of_tickets

print("Sorry we ran out of ticket :( ")
