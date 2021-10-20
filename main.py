import random

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''


def game():
    images = [rock, paper, scissors]
    players_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: \n"))

    if players_choice >= 3 or players_choice < 0:
        print("You entered wrong number. You lose.")
    else:
        print(images[players_choice])
        computers_choice = random.randint(0, 2)
        print(f"Computer chose: \n{computers_choice}")
        print(images[computers_choice])

        if computers_choice == players_choice:
            print("It's a draw.")
        elif (players_choice == 0 and computers_choice == 1) or (players_choice < computers_choice):
            print("You lose.")

        elif (players_choice == 0 and computers_choice == 2) or (players_choice > computers_choice):
            print("You won!")


if __name__ == '__main__':
    game()



