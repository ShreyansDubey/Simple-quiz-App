from django.shortcuts import render
from createQuiz.models import quizzes
# Create your views here.

def quiz_list(request) :
    all_quizzes = quizzes.objects.all()
    quiz_names = [q.quiz_name for q in all_quizzes]
    quiz_ids = [q.quiz_index for q in all_quizzes]
    return render(request, 'quiz_list.html', {'q_names_ids' : zip(quiz_names, quiz_ids)})

def attempt_quiz(request) :
    #getting the quiz index from the link clicked
    quiz_idx = request.GET.get('quiz_idx')
    all_quizzes = quizzes.objects.all()
    quiz_req = None
    for q in all_quizzes :
        if int(quiz_idx) == q.quiz_index :
            quiz_req = q.quiz_string
            break
    #print(quiz_req)
    #After getting the quiz object, parse the quiz string to retrieve the questions and options
    
    quiz_questions = quiz_req.split('|')
    for i in range(len(quiz_questions)) :
        quiz_questions[i] = quiz_questions[i].split(',')
        quiz_questions[i] = quiz_questions[i][:-1]
    
    quiz_q = []
    quiz_op_A = []
    quiz_op_B = []
    quiz_op_C = []
    quiz_number = []
    for idx in range(len(quiz_questions)) :
        quiz_number.append(idx+1)
        quiz_q.append(quiz_questions[i][0])
        quiz_op_A.append(quiz_questions[i][1])
        quiz_op_B.append(quiz_questions[i][2])
        quiz_op_C.append(quiz_questions[i][3])

    #context_dict
    d = {
        'q_questions' : zip(quiz_number, quiz_q, quiz_op_A, quiz_op_B, quiz_op_C)
    }
    return render(request, 'attempt_quiz.html', d)
    