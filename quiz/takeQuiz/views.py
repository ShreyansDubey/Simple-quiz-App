from django.shortcuts import render
from createQuiz.models import quizzes
from takeQuiz.models import taken_quiz
import json
# Create your views here.

def quiz_list(request) :
    all_quizzes = quizzes.objects.all()
    quiz_names = [q.quiz_name for q in all_quizzes]
    quiz_ids = [q.quiz_index for q in all_quizzes]
    return render(request, 'quiz_list.html', {'q_names_ids' : zip(quiz_names, quiz_ids)})

def attempt_quiz(request) :
    all_quizzes = quizzes.objects.all()
    if request.method == 'POST' :
        q_ans = str(request.POST.get('quiz_ans_string', ''))    
        q_idx = int(request.POST.get('q_idx', ''))
        quiz_req = None
        for q in all_quizzes :
            if int(q_idx) == q.quiz_index :
                quiz_req = q.quiz_string
                break
        #list to contain answers
        ans = []
        quiz_questions = quiz_req.split('|')
        for i in range(len(quiz_questions)) :
            quiz_questions[i] = quiz_questions[i].split(',')
            ans.append(quiz_questions[i][-1])
        q_ans = q_ans.split(' ')
        # print(q_ans)
        # print(ans)
        correct = 0
        for i in range(len(q_ans)) :
            if q_ans[i] == ans[i] :
                correct += 1            
        # print(correct)
        # print(len(ans) - correct)
        curr_username = request.user.username
        user_quiz_obj = list(taken_quiz.objects.filter(user = curr_username))
        print(user_quiz_obj)
        #Add the quiz score (correct / incorrect) in the database
        text = ""
        if len(user_quiz_obj) == 1 :
            print('in 1')
            #record already exists (user has previously taken some quizzes)
            user_quiz_obj = taken_quiz.objects.get(user = curr_username)
            j = user_quiz_obj.quiz_taken_JSON
            u_q_o = json.loads(j)
            print(u_q_o)
            try :
                #user has already attempted this quiz
                #do not increment the quiz taken count
                temp = u_q_o[str(q_idx)]
                print(temp)
                text = 'You have already submitted this quiz'
            except :
                #user has not attempted this quiz
                #increment the quiz taken count
                quiz = quizzes.objects.get(quiz_index=q_idx)
                quiz.times_attempted += 1
                quiz.save()

                #add this quiz entry to the JSON
                q_dict = {
                    'correct' : correct,
                    'incorrect' : len(ans) - correct
                }
                #change existing record
                u_q_o[str(q_idx)] = q_dict
                #stringify the JSON and save
                user_quiz_obj.quiz_taken_JSON = json.dumps(u_q_o)
                user_quiz_obj.save()
        elif len(user_quiz_obj) == 0 :
            print('in 0')
            #record does not exist (this is the first quiz user has submitted)
            
            #increment the quiz taken count
            quiz = quizzes.objects.get(quiz_index=q_idx)
            quiz.times_attempted += 1
            quiz.save()

            #create new record for the user
            quiz_taken_j = {
                str(q_idx) : {
                    'correct' : correct,
                    'incorrect' : len(ans) - correct
                }
            }
            new_record = taken_quiz(user=curr_username, quiz_taken_JSON=json.dumps(quiz_taken_j))
            new_record.save(force_insert=True)
            text = 'Responses Saved'
        return render(request, 'attempt_quiz.html', {'text' : text})
    else :

        #getting the quiz index from the link clicked
        quiz_idx = request.GET.get('quiz_idx')
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
            quiz_q.append(quiz_questions[idx][0])
            quiz_op_A.append(quiz_questions[idx][1])
            quiz_op_B.append(quiz_questions[idx][2])
            quiz_op_C.append(quiz_questions[idx][3])

        #context_dict
        d = {
            'q_questions' : zip(quiz_number, quiz_q, quiz_op_A, quiz_op_B, quiz_op_C),
            'q_idx' : quiz_idx,
        }
        return render(request, 'attempt_quiz.html', d)
