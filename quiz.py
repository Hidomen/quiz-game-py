import random
from questions import q_list


def main() :
    question_counter = 1

    while question_counter != 0 or question_counter > 10:
        # picking question
        while True :
            random_question = random.choice(q_list)
            if random_question[0] == question_counter :
                break
        #
        display(random_question, question_counter)
        # getting input
        answer = input("> ").upper()
        while answer not in ["A", "B", "C", "D"] :
            print("INVALID")
            answer = input("> ").upper()
        # RIGHT ANSWER
        if answer == random_question[6].upper() :
            print("CORRECT")
            question_counter += 1
        # WRONG ANSWER
        else :
            print("WRONG")
            print("GAME OVER")
            question_counter = 0
        # WINNING THE GAME
        if question_counter == 11 :
            print("WOAH YOU WON")
            break





def display (question, question_counter) :
    print(f"QUESTION NUM-{question_counter} : \n     {question[1].upper()}? \nA : {question[2].upper()} \nB : {question[3].upper()} \nC : {question[4].upper()} \nD : {question[5].upper()}" )

main()

