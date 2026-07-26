import requests
import html
quiz="https://opentdb.com/api.php?amount=20&category=17&difficulty=easy&type=multiple"

response=requests.get(url=quiz)
data=response.json()['results']

questions=[]

for question in data:
    questions.append([html.unescape(question['question']),html.unescape(question['incorrect_answers'])+html.unescape([question['correct_answer']])])

class QuestionBank:
    def __init__(self):
        self.question_no=0
    
    def get_question(self):
        if self.question_no<len(questions):
            question=questions[self.question_no][0]
            question_options=questions[self.question_no][1]
            question_answer=questions[self.question_no][1][3]

            self.question_no+=1
        return self.question_no,question,question_options,question_answer
