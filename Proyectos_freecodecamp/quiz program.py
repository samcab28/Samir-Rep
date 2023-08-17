#programa de quiz basico 

quiz = {
    'question1':{
        'question' : 'what is the capital of france?' , 'answer' : 'paris'
    },
    'question2':{
        'question' : 'what is the capital of germany?' , 'answer' : 'berlin'
    },
    'question3':{
        'question' : 'what is the capital of costa rica?' , 'answer' : 'san jose'
    },
    'question4':{
        'question' : 'what is the capital of peru?' , 'answer' : 'lima'
    }
         
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input("write your answer: ")
    if answer.lower() == value['answer'].lower():
        print('good job')
        score += 1
    else:
        print('error, the correct answer is: ',value['answer'])
    
if score == 4:
    print('puntuacion perfecta')
elif score == 3:
    print('3/4')
elif score == 2: 
    print('2/4')
elif score == 1:
    print('1/4')
else: 
    print(0/4)