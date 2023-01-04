# Snake Water Gun game
import random

no_of_rounds = 1
computer_score = 0
person_score = 0
tied_rounds =0
round_no = 1

choice_list = ['s', 'w', 'g']

while no_of_rounds <= 10:

    try: 
        print(f"\nRound : {round_no}")


        computer_choice = random.choice(choice_list)
        person_choice = str(input("\nPress 's' for snake\n'w' for water\n'g for gun'\n\nEnter your choice: "))

        if computer_choice == 's':

            if person_choice == 's':
                print("\nYou choose snake and computer choose snake too.\nRound tied.\nNo score will be given to both of you.")
                no_of_rounds += 1
                tied_rounds += 1
                round_no += 1

            elif person_choice == 'w':
                print("\nYou choose water and computer choose snake.\nYou lost.")
                computer_score += 1
                no_of_rounds += 1
                round_no += 1

            elif person_choice == 'g':
                print("\nYou choose gun and computer choose snake.\nYou won.")
                person_score += 1
                no_of_rounds += 1
                round_no += 1

            else:
                print("Check your input!")


        if computer_choice == 'w':

            if person_choice == 'w':
                print("\nYou choose water and computer choose water too.\nRound tied.\nNo score will be given to both of you.")
                no_of_rounds += 1
                tied_rounds += 1
                round_no += 1

            elif person_choice == 's':
                print("\nYou choose snake and computer choose water.\nYou won.")
                person_score += 1
                no_of_rounds += 1
                round_no += 1

            elif person_choice == 'g':
                print("\nYou choose gun and computer choose water.\nYou lost.")
                computer_score += 1
                no_of_rounds += 1
                round_no += 1

            else:
                print("Check your input!")
            
        if computer_choice == 'g':

            if person_choice == 'g':
                print("\nYou choose gun and computer choose gun too.\nRound tied.\nNo score will be given to both of you.")
                no_of_rounds += 1
                tied_rounds += 1
                round_no += 1

            elif person_choice == 's':
                print("\nYou choose snake and computer choose gun.\nYou lost.")
                computer_score += 1
                no_of_rounds += 1
                round_no += 1

            elif person_choice == 'w':
                print("\nYou choose water and computer choose gun.\nYou won")
                person_score += 1
                no_of_rounds += 1
                round_no += 1

            else:
                print("Check your input!")
    
    except:
        print("Check your input!")


print(f"\nYou won {person_score} rounds\nComputer won {computer_score} rounds\n{tied_rounds} rounds tied.")

if(computer_score > person_score):
    print("\nFinal score: Computer won.")

elif(person_score > computer_score):
    print("\nFinal score: You won.")

else:
    print("\nFinal Score: Match tied")
