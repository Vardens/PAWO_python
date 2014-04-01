#!/usr/bin/env python
import random

def main():
    """Main function that perform general logic for game"""
    print 'Game started!\n'
    number_of_rounds = raw_input('How many rounds? ')
    answer = generate_answer()
    for item_id in range(int(number_of_rounds)):
        user_response = get_user_response()
        if answer == user_response:
            print 'Correct! You won'
            return
        print 'Incorrect answer.'
        give_clue(user_response, answer)
    print 'Game over!'	
	
def generate_answer():
    """Generate answer using random numbers"""
    numbers = []
    answer = ''
    numbers.extend(range(1, 9, 1))	
    for item in range(4):
        digit = random.choice(numbers)
        answer += str(digit)
    return answer
	

def get_user_response():
    """Get user input from keyboard"""
    if_exit_loop = True
    while True:
        user_response = raw_input('Please enter a 4-digit number(1-9): ').strip()
        if len(user_response) != 4:
            print 'Wrong number of digits'
            continue
        for item_id in range(4):
            if is_number(user_response[item_id]) == False:
                print 'Some signs in response are not valid'
                if_exit_loop = False				
                break
            else:
                if_exit_loop = True				
        if if_exit_loop == False:			
            continue
        else:
            return user_response
		
		
def is_number(sign):
    """Check if parameter is a number"""
    try:
        int(sign)
        return True
    except ValueError:
        return False
			
def give_clue(user_response, answer):
    """Give a clue in order to help user guess the answer"""
    print 'Here is a hint(X is correct, O has wrong postion, - is wrong):'
    for item_id in range(4):
        if user_response[item_id] == answer[item_id ]:
            print 'X',
            continue
	elif user_response[item_id] in answer:
	    print 'O',	
        else:
            print '-',
    print '\n'	
	

	
if __name__ == '__main__':
    main()
