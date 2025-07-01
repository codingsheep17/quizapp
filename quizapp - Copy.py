#Quiz App Using free API of a random MCQS generator with options 
#importing modules
import requests
import sys
import random
import html
#creating class 

class QuizApp:
    def __init__(self,levels: int, difficulty:str):
        self.difficulty = difficulty
        self.levels = levels
        self.score = 0
        self.question_no = 1
        self.fetch_questions_api()
        self.quiz_logic()
    #method for fecthing questions
    def fetch_questions_api(self):
        self.api_url = f"https://opentdb.com/api.php?amount={self.levels}&category=9&difficulty={self.difficulty}&type=multiple"
        self.fetched_data = requests.get(self.api_url)
        self.json_data = self.fetched_data.json() #conversion to json form
    #logic of printing questions along option and checking correct or not
    def quiz_logic(self):
        for self.i,self.j in enumerate((self.json_data["results"])):   
            self.question = html.unescape(self.j['question'])
            correct_option = html.unescape(self.j['correct_answer'])
            incorrect_options = []
            for opt in self.j['incorrect_answers']:
                  unescaped_opt = html.unescape(opt)
                  incorrect_options.append(unescaped_opt)
            options = incorrect_options + [correct_option]
            random.shuffle(options)
            print(f"-->{self.question_no}: {self.question}")
            for index, opt in enumerate(options, 1):
                    print(f"{index}. {opt}")
            correct_option_index = options.index(correct_option)
            try:
                    answer = int(input("Your Answer --> ")) - 1
                    if answer == correct_option_index:
                            print("Correct")
                            self.score += 10
                    else:
                            print("Wrong Answer")
                    self.question_no += 1
            except ValueError:
                    print("Kindly enter only option number")
        self.total_score()
    def total_score(self):
        print(f"Your Total Score is --> {self.score}/{self.levels*10}")
        if self.score > (self.levels*10)//2:
            print("Good Performance")
        elif self.score < (self.levels*10)//2:
            print("Try again, You failed")
        else:
            print("Score Error")

#adding the difficulty level selection logic and amount of levels logic
amount_of_levels = int(input("Enter the amount of levels (5-50)--> "))
if amount_of_levels >= 5 and amount_of_levels <= 50:
    try:
        user_difficulty_choice = str(input("""Enter the Difficulty Level
        1: Easy
        2: Medium
        3: Hard --> """)).lower()
    except ValueError:
            print("Kindly Enter The Only Choices Given Above")
    try:
        QuizApp(amount_of_levels, user_difficulty_choice)
    except:
          print("Try again error while loading app!")
else:
    print("Not in Range")