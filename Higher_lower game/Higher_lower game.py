#Display art
from game_data import data,vs,logo
import random
print(logo)
score=0
account_b= random.choice(data)
game_should_continue = True
while game_should_continue:
    #Generate a random account from the game_data
    account_a= account_b
    account_b= random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    #Format the account data into printable format
    def format_data(account):
        account_name=account["name"]
        account_desc=account["description"]
        account_country=account["country"]
        return f"{account_name},a {account_desc},a {account_country}"
    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    #Ask user for a guess
    guess=input("Who has more followers ? Type 'A' or 'B' :").lower()

    #Check if user is correct.
    ##Get follower count of each account.
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    def check_answer(guess,a_followers,b_followers):
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"
    #Give user feedback on their guess
    #Score counting
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score=score+1
        print(f"You're right! current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry,that's wrong.Final Score:{score}")
