from django.shortcuts import render
from createQuiz.models import quizzes

# Create your views here.

def create_quiz(request) :
    if request.method == 'POST' :
        #the quiz index is +1 the previous index
        q_index = quizzes.objects.count() + 1
        
        #number of questions
        noq = int(request.POST.get('noq', ''))
        
        #iterating through the POST data to generate a parsable 'quiz string'
        #this will be stored in the DB
        q_string = ''
        for i in range(noq) :
            #string of current question
            curr_q_string = ''

            curr_q = 'q' +  str(i + 1)
            #get the question
            q = request.POST.get(curr_q, '')

            #get the options
            op1 = request.POST.get(curr_q+'o1', '')
            op2 = request.POST.get(curr_q+'o2', '')
            op3 = request.POST.get(curr_q+'o3', '')

            #get the answer
            ans = request.POST.get(curr_q+'a', '')

            #append this to the current parsable string
            if i != 0 :
                #if this is not the first question append '|' at the start
                curr_q_string += '|'
            
            #the commas and | will later be used to parse and split the string into individual questions
            curr_q_string = curr_q_string + q + ',' + op1 + ',' + op2 + ',' + op3 + ',' + ans
            
            #append this to the main quiz string
            q_string += curr_q_string

        #Below is the way to retrieve qustions from this string
        # for q in quiz_string.split('|') :
        #     print(q.split(','))

        p = quizzes(quiz_index=q_index, quiz_string=q_string)
        p.save(force_insert=True)
            


    return render(request, 'create_quiz.html')