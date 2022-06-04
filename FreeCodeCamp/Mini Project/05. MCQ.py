class questions:

    def __init__(self, questionprompt, solution):

        self.prompt = questionprompt
        self.ans = solution

def define_questions():

    promptlist = []

    promptlist.append("\nWhat is the color of a banana?\n(a) Red\n(b) Blue\n(c) Yellow\n(d) Transparent\n\nYour answer: ")
    promptlist.append("\nWhat is the shape of a ball?\n(a) Cube\n(b) Sphere\n(c) Rod\n(d) Irregular\n\nYour answer: ")
    promptlist.append("\nWhat is the brand of Mac Studio?\n(a) Apple\n(b) Microsoft\n(c) Samsung\n(d) Unknown\n\nYour answer: ")

    questionlist = [
        questions(promptlist[0], 'c'),
        questions(promptlist[1], 'b'),
        questions(promptlist[2], 'a')
    ]

    return questionlist

def run_main(): 

    score = 0
    questionlist = define_questions()

    for question in questionlist:

        user_answer = input(question.prompt)[0]

        if((user_answer == question.ans.upper()) | (user_answer == question.ans.lower())):
            score += 1
        else:
            continue
    
    print("You got %d/%d correct!" % (score, len(questionlist)))

run_main()