from oop.Question import Question

question_prompt = [
    "sadfasdfas1",
    "asdfasdfa2",
    "kjsdjfasjdf3"
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"c")
]


def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(questions)) + " correct")


run_test(questions)