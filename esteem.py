"""





Choice	Points
Strongly Disagree	3
Disagree	2
Agree	1
Strongly Agree	0


"""

negative_scoring = {"D":3, "d":2, "a":1, "A":0}
positive_scoring = {"D":0, "d":1, "a":2, "A":3}


def get_answer():
    while True:
        user_input = input("Enter D, d, a, or A: ")
        if user_input in ['D','d','a','A']:
            return user_input

# place the strings in a list of lists, with the scoring mechanism as ascending or descending

QUESTION = 0
SCORING_SORTING = 1
POSITIVE = 0
NEGATIVE =1
            
question_list = [
    ["I feel that I am a person of worth, at least on an equal plane with others.",0],
    ["I feel that I have a number of good qualities.",0],
    ["All in all, I am inclined to feel that I am a failure.",1],
    ["I am able to do things as well as most other people.",0],
    ["I feel I do not have much to be proud of.",1],
    ["I take a positive attitude toward myself.",0],
    ["On the whole, I am satisfied with myself.",0],
    ["I wish I could have more respect for myself.",1],
    ["I certainly feel useless at times.",1],
    ["At times I think I am no good at all.",1]
]
#print the header
print("This program is an implementation of the Rosenberg Self-Esteem Scale. \n\
This program will show you ten statements that you could possibly apply to yourself. \n\
Please rate how much you agree with each of the statements by responding with one of these four letters:\n\n")
      
print("D means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.\n")

total_score = 0

#loop through the questions in the list
for item in question_list:
    
    #print question
    print(item[QUESTION])

    #get user response
    response = get_answer()
    
    #score the response
    if item[SCORING_SORTING] == POSITIVE:
        score = positive_scoring[response]
    else:
        score = negative_scoring[response]
    
    #add to the score based on the scale
    total_score += score

#print the result
print(f"Your score is {total_score}")
#Your score is 21.
print("A score below 15 may indicate problematic low self-esteem.")
#A score below 15 may indicate problematic low self-esteem.