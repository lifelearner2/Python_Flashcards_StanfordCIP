from graphics import Canvas
import time
import random
"""
Python Flashcard game to help students learn and test their knowledge on beginning Python.
If an answer is correct, the user will be congratulated and will see a Hello Kitty image on the canvas. 

This program is a graphics program that draws colored rectangles for the flashcards and draws a hello kitty image
as visual feedback when an answer is correct. It uses a list of dictionaries, where each dictionary represents a
flashcard question and answer as the key/value pair. It utilizes a for loop as well as if/else statements.

There are also several helper functions related to hello kitty drawing.
"""
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PATCH_SIZE = 100
DELAY = 0.05 # Delay in seconds for drawing kitty 
score = 0

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    left_x = 20 #top-left corner for x which runs horizontal, position increases to the right with higher number value
    top_y = 20  #top -left corner for y which runs vertical, position moves downward with higher number value
    flashcard_width = 370
    flashcard_height = 50
    score = 0 #variable to keep track of score. It starts at zero.
    
    #adding color to background on canvas
    canvas.create_rectangle(left_x, top_y, CANVAS_WIDTH-10, CANVAS_HEIGHT-20, 'lightblue')
    #creates a pink colored flashcard
    flash_card = canvas.create_rectangle(left_x, top_y, flashcard_width, flashcard_height, 'pink')
   
    flashcard_questions = [
        {"question": "What is the syntax for defining a function in Python?", "answer": "def function_name():"},
        {"question": "What is the output of the following code? print(2 + 3 * 4)", "answer": "14"},
        {"question": "What is the output of the following code? print('Hello, ' + 'world!')", "answer": "Hello, world!"},
        {"question": "What is the correct syntax to define an empty list called 'my_list'?", "answer": "my_list = []"},
        {"question": "What is the index position for 'Ann'? [Ann, TC, Nailah]", "answer": "0"},
        {"question": "Which is mutable, a list or a tuple?", "answer": "list"},
        {"question": "Ask user 'Enter your name: ' and assign it to name variable", "answer": "name = input('Enter your name: ')"},
        {"question": "Write the function in correct syntax to display output to console", "answer": "print()"},
        {"question": "Type the operator that concatenates two strings", "answer": "+"},
        {"question": "If you know how many times to iterate, which loop do you use? ", "answer": "for loop"},
        {"question": "Type 'True' or 'False', Python is an object-oriented language", "answer": "True"},
        {"question": "Type 'True' or 'False', Python uses {} to define code blocks", "answer": "False"},
        {"question":"Type 'True' or 'False', Python uses indents to define code blocks", "answer": "True"},
        {"question":"Type 'True' or 'False', Python uses == for assignment", "answer": "False"},
        {"question":"Type 'True' or 'False', Python uses = for strict equality/comparison", "answer": "False"}, 
        {"question":"True or False, len() returns number of elements in a list", "answer": "True"},
        {"question":"True or False, 'not' is used for logical negation.", "answer": "True"},
        {"question":"True or False, range() generates numbers including the end value.", "answer": "False"},
        {"question":"True or False, range() generates numbers and excludes end value.", "answer": "True"},
        {"question":"What will this print? range(1,5).", "answer": "[1,2,3,4]"},
        {"question":"Fill in for random number from 1-5: rand_num=random.__(1,5).", "answer": "randint"},
        {"question":"Now print the result of the random_number variable.", "answer": "print(random_number)"},
    ]
    
    # print("Thanks for playing! Let's play again sometime!")
    
    # Welcome message
    print()
    welcome_message = "Welcome to my Python Flashcard game. It's designed to test your knoweledge about some of the basics of Python. Pay attention when you provide answers as it is case sensitive. Good luck and I hope you enjoy it and maybe even learn along the way. There are 22 questions, but you can type 'q' at any time to quit the game."
    print(welcome_message)
    print() #gives a space between this message and the question that will print after

    random.shuffle(flashcard_questions)
    
    #Looping through the flashcard_questions list in random order
    for flashcard in flashcard_questions:
        question = flashcard["question"] #loop retrieves value associated w/key 'question' from the flashcard dictionary & assigns that value to the variable 'question'
        correct_answer = flashcard["answer"] #this does the same for the key 'answer' from dictionary & stores in var 'correct_answer'
        #random.shuffle(flashcard_questions)
        
        #displaying text on the flashcard with create_text() method. 
        #the anchor='nw' parameter is used to align the text to the northwest part of the card (top left corner)
        #flash_card_text = canvas.create_text(left_x + 3, top_y + 20, text=question, anchor="nw")
        
        #adding color to background on canvas
        #canvas.create_rectangle(left_x, top_y, CANVAS_WIDTH-10, CANVAS_HEIGHT-20, 'lightblue')
        #creates a pink colored flashcard
        #flash_card = canvas.create_rectangle(left_x, top_y, left_x + flashcard_width, top_y + flashcard_height, 'pink')
        #flash_card_question = canvas.create_text(left_x + 3, top_y + 10, text=question, anchor="nw")

        # Draw background first
        canvas.create_rectangle(left_x, top_y, CANVAS_WIDTH-10, CANVAS_HEIGHT-20, 'lightblue')

        # Draw flashcard
        canvas.create_rectangle(left_x, top_y, left_x + flashcard_width, top_y + flashcard_height, 'pink')

        # Draw question text LAST (so it sits on top)
        canvas.create_text(left_x + 3, top_y + 10, text=question, anchor="nw")

        time.sleep(0.01)

        # THEN ask for input
        user_answer = input("Type your answer to the question or 'q' to quit: ")
        
        #handling user input, checking the answers to see if they are correct & displaying messages/image to user
        #user_answer = input("Type your answer to the question or 'q' to quit: ")
        if user_answer == 'q':
            # Thank you message
            thank_you_message = "Thanks for playing. Let's play again sometime!"
            print(thank_you_message)
            #display user's score
            print()
            print("Your score:", score, "out of",len(flashcard_questions))
            break
            
        if user_answer == correct_answer:
            print("Great job, that's correct!")
            print()
            draw_kitty(canvas, left_x + 20 + flashcard_width - PATCH_SIZE, top_y - 20)
            score+=1 #increment score for each correct answer, stores number of score in the score variable
        else:
            print("Sorry, that's not correct. The correct answer is", correct_answer)
            print()
            
        #displays answer on flashcard 
        flash_card_answer = canvas.create_text(left_x + 20, top_y + 30, text="Answer: " + correct_answer, anchor="nw") 
            
        # Wait for a delay before clearing the canvas 
        DELAY = 1.5 #defining a new delay time specificially for this 
        time.sleep(DELAY)
        # Wait for a delay before clearing the canvas
        canvas.clear()
  
        #Updating the top_y coordinate for the next flashcard to be displayed
        top_y += flashcard_height -40 
        
    #prints goodbye message and score once user has answered all 22 questions. 
    #added that this message and score will not print if the user presses 'q', as there is already a thank you message and score printing for 'q'
    if len(flashcard_questions) >= score and user_answer != 'q':
        #Goodbye Message
        print()
        goodbye_message = "You've completed the game! Press Run if you'd like to play again!"
        print(goodbye_message)
        
        #display user's score
        print()
        print("Your score:", score, "out of",len(flashcard_questions))
    
    #starts the event loop which will handle the display and interactions with canvas
    canvas.mainloop()

#helper functions:
def draw_kitty(canvas, left_x, top_y):
    draw_hello_outline(canvas, left_x, top_y)
    draw_hello_kitty(canvas, left_x, top_y)
    draw_hello_left_eye(canvas, left_x, top_y)
    draw_hello_right_eye(canvas, left_x, top_y)
    draw_hello_nose_outline(canvas, left_x, top_y)
    draw_hello_nose(canvas, left_x, top_y)
    draw_hello_whiskers(canvas, left_x, top_y)
    draw_hello_ears(canvas, left_x, top_y)
    draw_hello_bow(canvas, left_x, top_y)
    
def draw_hello_outline(canvas, left_x, top_y):
    end_x = left_x + PATCH_SIZE
    end_y = top_y + PATCH_SIZE
    inset = 11
    canvas.create_oval(left_x+inset, top_y+inset, end_x-inset, end_y-inset, 'black')
    time.sleep(DELAY)
    
def draw_hello_kitty(canvas, left_x, top_y):  
    draw_hello_outline(canvas, left_x, top_y)
    end_x = left_x + PATCH_SIZE
    end_y = top_y + PATCH_SIZE
    inset = 13
    canvas.create_oval(left_x+inset, top_y+inset, end_x-inset, end_y-inset, 'white')
    draw_hello_left_eye(canvas, left_x, top_y)
    draw_hello_right_eye(canvas, left_x, top_y)
    draw_hello_nose(canvas, left_x, top_y)
    time.sleep(DELAY)
  
  
def draw_hello_left_eye(canvas, left_x, top_y):
    inset_x = 62
    inset_y = 50
    eye_width = 10
    eye_height = 12
    canvas.create_oval(left_x + inset_x, top_y + inset_y,
                       left_x + inset_x + eye_width, top_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)

def draw_hello_right_eye(canvas, left_x, top_y):
    inset_x = 26
    inset_y = 50
    eye_width = 10
    eye_height = 12
    canvas.create_oval(left_x + inset_x, top_y + inset_y,
                       left_x + inset_x + eye_width, top_y + inset_y + eye_height, 'black')
    time.sleep(DELAY)
                       
def draw_hello_nose(canvas, left_x, top_y):
    draw_hello_nose_outline(canvas,left_x, top_y)
    inset_x = 45
    inset_y = 62
    nose_width = 7
    nose_height = 5
    canvas.create_oval(left_x + inset_x, top_y + inset_y, left_x + inset_x + nose_width, top_y + inset_y + nose_height, 'orange')
    time.sleep(DELAY)
    
 
def draw_hello_nose_outline(canvas, left_x, top_y):
    inset_x = 44
    inset_y = 61
    nose_width = 9
    nose_height = 7
    canvas.create_oval(left_x + inset_x, top_y + inset_y, left_x + inset_x + nose_width, top_y + inset_y + nose_height, 'black')
    time.sleep(DELAY)
    
def draw_hello_whiskers(canvas, left_x, top_y):
    # Left whiskers
    whisker_left_x = left_x + 32
    whisker_top_y = top_y + 65

    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x - 20, whisker_top_y - 10, 'black')
    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x - 20, whisker_top_y, 'black')
    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x - 20, whisker_top_y + 10, 'black')

    # Right whiskers
    whisker_left_x = left_x + 68
    whisker_top_y = top_y + 65

    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x + 20, whisker_top_y - 10, 'black')
    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x + 20, whisker_top_y, 'black')
    canvas.create_line(whisker_left_x, whisker_top_y, whisker_left_x + 20, whisker_top_y + 10, 'black')

def draw_hello_ears(canvas, left_x, top_y):
    # Left ear
    canvas.create_line(left_x + 25, top_y + 20, left_x + 35, top_y + 5, 'black')
    canvas.create_line(left_x + 35, top_y + 5, left_x + 45, top_y + 20, 'black')
    canvas.create_line(left_x + 25, top_y + 20, left_x + 45, top_y + 20, 'black')

    # Right ear
    canvas.create_line(left_x + 55, top_y + 20, left_x + 65, top_y + 5, 'black')
    canvas.create_line(left_x + 65, top_y + 5, left_x + 75, top_y + 20, 'black')
    canvas.create_line(left_x + 55, top_y + 20, left_x + 75, top_y + 20, 'black')

def draw_hello_bow(canvas, left_x, top_y):
    #center circle
    canvas.create_oval(left_x + 55, top_y + 10, left_x + 78, top_y + 30, 'red')
    
    #left triangle
    canvas.create_line(left_x + 65, top_y + 16, left_x + 50, top_y + 24, 'red')
    canvas.create_line(left_x + 70, top_y + 36, left_x + 50, top_y + 24, 'red')
    #right triangle
    canvas.create_line(left_x + 80, top_y + 26, left_x + 70, top_y + 34, 'red')        
      

if __name__ == '__main__':
    main()














