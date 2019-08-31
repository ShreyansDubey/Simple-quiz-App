//Makes a string out of the options chosen by the user

//gets a list of all questions

document.getElementById('submit_quiz').onclick = function() {
    q_elements = document.getElementsByClassName('q');
    ques = []
    for (let i = 0; i < q_elements.length; i++) {
        ques[i] = q_elements[i].innerText; 
    }

    answers_selected = []
    for (let i = 0; i < ques.length; i++) {
        try{
            curr_ans = document.querySelector('input[name="' + ques[i] + '"]:checked').value;
        }
        catch(err) {
            curr_ans = null
        }
        if(curr_ans == null) {
            answers_selected[i] = 'Z';
        } 
        else {
            answers_selected[i] = curr_ans;
        }
    }
    //Now answers_selected is a list of all the answers
    //console.log(answers_selected);
    ans_selected_string = "";
    for (let i = 0; i < answers_selected.length; i++) {
        if(i != answers_selected.length - 1)
            ans_selected_string += (answers_selected[i] + ' ');   
        else
            ans_selected_string += (answers_selected[i]);   
    }
    //Setting the hidden form field value
    document.getElementById('ans').value = ans_selected_string;
    //Submitting the form with answers
    document.getElementById('ans_form').submit();
}



