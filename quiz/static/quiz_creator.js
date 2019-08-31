//Creates a dynamic form

document.getElementById("sub_noq").onclick = function() {
    // labels = '<label for="id_q' + no + '"> Q.1. </label><label for="id_q'+ no +'o1"> A </label><label for="id_q' + no + 'o2"> B </label><label for="id_q' + no + 'o3"> C </label>'
    // question = '<input id="id_q' + no + '" type="text" name="q' + no + '">'
    // options = '<input id="id_q' + no + 'o1" type="text" name="q' + no + 'o1"><input id="id_q' + no + 'o2" type="text" name="q' + no + 'o2"><input id="id_q' + no + 'o3" type="text" name="q' + no + 'o3">'
    // ans = '<label> Ans<input id="id_q' + no + 'a_a" type="radio" name="q' + 1 + 'a" value="A">A<br><input id="id_q' + no + 'a_b" type="radio" name="q' + no + 'a" value="B">B<br><input id="id_q' + no + 'a_c" type="radio" name="q' + no + 'a" value="C">C<br></label>'

    form = document.getElementById('q_form')

    html_to_be_ins = ''
    var noq = parseInt(document.getElementById("noq").value);
    for (let index = 1; index <= noq; index++) {
        html_to_be_ins += gen_ques(index)
        html_to_be_ins += '<br>'
    }
    html_to_be_ins += '<button type="submit">Save Quiz</button>'
    form.insertAdjacentHTML('beforeend', html_to_be_ins)
    document.getElementById('sub_noq').style.display = 'none';
    document.getElementById('noq').style.display = 'none';
}

function gen_ques(no) {
    //labels = '<label for="id_q' + no + '"> Q.1. </label><label for="id_q'+ no +'o1"> A </label><label for="id_q' + no + 'o2"> B </label><label for="id_q' + no + 'o3"> C </label>'
    question = 'Question ' + no + '<br>' + '<input id="id_q' + no + '" type="text" name="q' + no + '"><br>'
    options = 'A:<br><input id="id_q' + no + 'o1" type="text" name="q' + no + 'o1"><br>B:<br><input id="id_q' + no + 'o2" type="text" name="q' + no + 'o2"><br>C:<br><input id="id_q' + no + 'o3" type="text" name="q' + no + 'o3"><br>'
    ans = '<label> Ans<br><input id="id_q' + no + 'a_a" type="radio" name="q' + no + 'a" value="A">A<br><input id="id_q' + no + 'a_b" type="radio" name="q' + no + 'a" value="B">B<br><input id="id_q' + no + 'a_c" type="radio" name="q' + no + 'a" value="C">C<br></label>'
    number_of_questions = '<input id="noq" name="noq" type="hidden" value="' + no + '">'
    temp = ''
    temp += question;
    temp += options;
    temp += ans;
    temp += number_of_questions;
    return temp;
}