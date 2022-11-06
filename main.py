from cmu_cs3_graphics import *
import json
import random
import math

#path = 123_0_1

def onAppStart(app):
    f=open('data/data.json')
    app.questionBank = dict()
    jsonData = json.load(f)

    # for question in jsonData["data"]:
    #     app.questionBank[question["question"]] = {"topic":question["topic"],"difficulty":question["difficulty"],"answer":question["answer"],"origin":question["origin"]}
    # #dict (key:value) = id:(question,answer,topic,difficulty,origin)
    
    app.questionBank = jsonData["data"]

    print(app.questionBank)
    print(app.width)
    print(app.height)
    app.welcome = True
    app.about = False
    app.credits = False
    app.topics = False
    app.settings = False
    app.questions = False
    app.results = False
    app.review = False
    app.lackOfQuestions = False
    app.topicList = {0:'Loops',1:'Strings',2:'Animations',3:'1D Lists and Tuples',4:'2D Lists',5:'Sets & Dictionaries',6:'Object Oriented Programming',7:'Recursion',8:'All'}
    app.selectedTopic = set()
    app.difficulty = 0
    app.numberOfQuestions = 0
    app.questionMode = 0
    app.finalQuestions = []
    app.currentQuestion = 0
    app.input = ['']
    app.correct = 0
#     app.testAnswer='''haha123
# 098
# [1,2]'''
    app.currentQuestionCorrect = 0
    app.tries = 0
    app.incorrectAnswers = []
    app.stepsPerSecond = 1
    app.timeBulbX = app.width//2
    app.timePerCT = (app.timeBulbX - app.width//4)*360//(app.width//2) # 0 to 360
    app.timeLeft = app.timePerCT
    app.bulbClicked = False

def loadQuestions(app):
    suitableQuestions = set()
    for question in app.questionBank:
        print(app.questionBank[question]["topic"])
        print(app.selectedTopic)
        
        print("-----")
        print(app.questionBank[question]["difficulty"])
        print(app.difficulty)
        
        print("-----")
        print("topic")
        print((int(app.questionBank[question]["topic"])) in app.selectedTopic)

        
        print("difficulty")
        print(int(app.questionBank[question]["difficulty"])+1==int(app.difficulty))
        if int(app.questionBank[question]["topic"]) in app.selectedTopic and int(app.questionBank[question]["difficulty"])+1==int(app.difficulty):
            # print(f"adding: {question}")
            suitableQuestions.add(question)
            
    # print(suitableQuestions)
            
    if app.numberOfQuestions<len(suitableQuestions):
        app.finalQuestions = random.sample(suitableQuestions,app.numberOfQuestions)
    else:
        app.finalQuestions = random.shuffle(list(suitableQuestions))

def reset(app):
    app.correct = 0
    app.currentQuestion = 0
    app.currentQuestionCorrect = 0
    app.tries = 0
    app.incorrectAnswers = []
    app.input = ['']
    app.timeLeft = app.timePerCT

def redrawAll(app):
    if app.welcome:
        drawWelcome(app)
    elif app.about:
        drawAbout(app)
    elif app.credits:
        drawCredit(app)
    elif app.topics:
        drawTopics(app)
    elif app.settings:
        drawSettings(app)
    elif app.questions:
        drawQuestions(app)
    elif app.results:
        drawResults(app)
    if app.review:
        drawReview(app)

def drawWelcome(app):
    drawLabel("112 Study Buddy",app.width//2,app.height//4,bold = True, size = 60)
    #import 112 dragon or smth
    drawRect(app.width//2,app.height//2-60,150,75,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Study!",app.width//2,app.height//2-60,size = 30, bold = True)
    drawRect(app.width//2,app.height//2+60,150,75,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("About",app.width//2,app.height//2+60,size = 30, bold = True)
    drawRect(app.width//2,app.height//2+180,150,75,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Credits",app.width//2,app.height//2+180,size = 30, bold = True)

def drawAbout(app):
    drawLabel("Information:",app.width//2,app.height//3,size = 40)
    drawLabel("Study buddy is an application that assists 15-112 students ",app.width//2, app.height//2-app.height//16, size = 20)
    drawLabel("in revising and practicing code-tracing questions.",app.width//2, app.height//2-10,size = 20)
    drawLabel("Questions are taken from previous 15-112 tests.",app.width//2,app.height//2+app.height//16, size = 20)
    drawLabel("Users can choose between 2 modes, Practice, and Exam",app.width//2,app.height//2+2*app.height//16,size = 20)
    drawLabel("Difficulties: Question difficulty levels can be selected by users",app.width//2,app.height//2+3*app.height//16,size =20)
    drawLabel("Topics: Users can select question topics they want to practice",app.width//2,app.height//2+4*app.height//16,size =20)
    drawRect(app.width//2,app.height//2+7*app.height//20,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Back",app.width//2,app.height//2+7*app.height//20,size = 25, bold = True)

def drawCredit(app):
    drawLabel("112 Study Buddy made at Hack 112",app.width//2,app.height//3,size = 40)
    drawLabel("Made by:",app.width//2, app.height//2-40, size = 40)
    drawLabel("Shermern Ang (shermera)",app.width//2,app.height//2+app.height//20-40, size = 30)
    drawLabel("Kester Tan (kestert)",app.width//2,app.height//2+2*app.height//20-40,size = 30)
    drawLabel("Joshua Tsang (jtsang2)",app.width//2,app.height//2+3*app.height//20-40,size =30)
    drawLabel("Nita Chen (kthavees)",app.width//2,app.height//2+3*app.height//20,size =30)
    drawRect(app.width//2,app.height//2+5*app.height//20,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Back",app.width//2,app.height//2+5*app.height//20,size = 25, bold = True)

def drawTopics(app):
    drawLabel("Topics:",app.width//2,app.height//8, size = 50,bold = True)
    drawLabel("Select all the topics you want to study!",app.width//2,app.height//5, size =30)
    for i in range(len(app.topicList)):
        drawRect(app.width//6,3*app.height//10+i*40,30,30,fill = None, border = 'black')
    for key in app.topicList:
        drawLabel(app.topicList[key],app.width//4,3*app.height//10+key*40+15,align = 'left',size =25)
    
    for checkIndex in app.selectedTopic:
        drawLine(app.width//6,3*app.height//10+checkIndex*40+10,app.width//6+15,3*app.height//10+checkIndex*40+30,fill= 'lightGreen',lineWidth = 5)
        drawLine(app.width//6+15,3*app.height//10+checkIndex*40+30,app.width//6+40,3*app.height//10+checkIndex*40-10,fill= 'lightGreen',lineWidth = 5)
    drawRect(app.width-60,app.height-35,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Next",app.width-60,app.height-35,size = 25, bold = True)


def drawSettings(app):
    drawLabel("Settings:",app.width//2,app.height//10-40, size = 50,bold = True)
    drawLabel("Customize your study session!",app.width//2,app.height//8-20, size =20)
    drawLabel("Difficulty",app.width//2,app.height//6,size = 30, bold = True)
    if app.difficulty==0:
        bonusCol = None
        normalCol = None
    elif app.difficulty==1:
        bonusCol = None
        normalCol = 'lightGreen'
    elif app.difficulty==2:
        bonusCol = 'lightGreen'
        normalCol = None
    drawRect(app.width//2-app.width//12,app.height//4,100,50,align = 'center',fill=normalCol,borderWidth = 2, border = 'black')
    drawRect(app.width//2+app.width//12,app.height//4,100,50,align = 'center',fill=bonusCol,borderWidth = 2, border = 'black')
    drawLabel('Normal',app.width//2-app.width//12,app.height//4,size=25)
    drawLabel('Hard',app.width//2+app.width//12,app.height//4,size=25)
    
    drawLabel("Number of Questions",app.width//2,app.height//3,size = 30, bold = True)
    if app.numberOfQuestions == 0:
        fiveQ = None
        tenQ = None
        fifteenQ = None
        twentyQ = None
    elif app.numberOfQuestions == 1:
        fiveQ = 'lightGreen'
        tenQ = None
        fifteenQ = None
        twentyQ = None
    elif app.numberOfQuestions == 2:
        fiveQ = None
        tenQ = 'lightGreen'
        fifteenQ = None
        twentyQ = None
    elif app.numberOfQuestions == 3:
        fiveQ = None
        tenQ = None
        fifteenQ = 'lightGreen'
        twentyQ = None
    elif app.numberOfQuestions == 4:   
        fiveQ = None
        tenQ = None
        fifteenQ = None
        twentyQ = 'lightGreen'
    drawRect(app.width//2-3*app.width//12,app.height//2-75,100,50,align = 'center',fill=fiveQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2-app.width//12,app.height//2-75,100,50,align = 'center',fill=tenQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2+app.width//12,app.height//2-75,100,50,align = 'center',fill=fifteenQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2+3*app.width//12,app.height//2-75,100,50,align = 'center',fill=twentyQ,borderWidth = 2, border = 'black')
    drawLabel('1',app.width//2-3*app.width//12,app.height//2-75,size=25)
    drawLabel('2',app.width//2-app.width//12,app.height//2-75,size=25)
    drawLabel('3',app.width//2+app.width//12,app.height//2-75,size=25)
    drawLabel('4',app.width//2+3*app.width//12,app.height//2-75,size=25)

    drawLabel("Mode",app.width//2,app.height//2,size=30,bold =True)
    if app.questionMode == 0:
        examCol = None
        practiceCol = None
    elif app.questionMode == 1:
        examCol = 'lightGreen'
        practiceCol = None
    elif app.questionMode == 2:
        examCol = None
        practiceCol = 'lightGreen'
    drawLabel("Exam Mode: Timed & 1 Attempt per Question",app.width//2,app.height//2+30,size=20)
    drawLabel("Practice Mode: Untimed & 4 Attempts Per Question",app.width//2,app.height//2+55,size=20)
    drawRect(app.width//2-app.width//12,2*app.height//3-25,100,50,align='center',borderWidth=2,border='black',fill=examCol)
    drawRect(app.width//2+app.width//12,2*app.height//3-25,100,50,align='center',borderWidth=2,border='black',fill=practiceCol)
    drawLabel("Exam",app.width//2-app.width//12,2*app.height//3-25,size = 25)
    drawLabel("Practice",app.width//2+app.width//12,2*app.height//3-25,size = 25)

    if app.questionMode == 1:
        drawLabel("Time Per CT",app.width//2,3*app.height//4,size = 30, bold = True)
        drawLine(app.width//4,3*app.height//4+50,3*app.width//4,3*app.height//4+50,lineWidth = 10, fill = 'grey')
        drawCircle(app.timeBulbX,app.height*3//4+50,20,fill='grey')
        drawRect(app.width//2,app.height*4//5+80,125,50,align= 'center',fill = None, border = 'black', borderWidth = 2)
        drawLabel(f'{app.timePerCT} seconds',app.width//2,app.height*4//5+80,size = 20)
        

    drawRect(app.width-110,app.height-60,100,50,fill='yellow',border='black',borderWidth = 5)
    drawRect(app.width-220,app.height-60,100,50,fill='yellow',border='black',borderWidth = 5)
    drawLabel("Next",app.width-60,app.height-35,size = 25, bold = True)
    drawLabel("Back",app.width-170,app.height-35,size = 25, bold = True)

def drawQuestions(app):
    print(f"final: {app.finalQuestions}")
    if app.finalQuestions!=None:
        drawLabel(f'Question {app.currentQuestion+1}:',app.width//5,app.height//8,size = 50,bold = True)
        question = app.finalQuestions[app.currentQuestion]
        print(f"question: {question}")
        # imageWidth, imageHeight = getImageSize(question)

        drawImage(question, app.width//2, app.height//12*5, align='center',width=app.width-app.width//5, height=app.height//2.5)

        drawRect(app.width//2,app.height*6//7,700,220,align='center',fill=None,border = 'black', borderWidth = 5)
        drawLabel("Type your answer here:",app.width//2-675/2,app.height*6//7-130,size = 30, bold = True,align='left')
        for lineIndex in range(len(app.input)):
            drawLabel(app.input[lineIndex],app.width//2-650/2,app.height*6//7-80+lineIndex*25,size = 20,align = 'left')
        drawLabel(">",app.width//2-675/2,app.height*6//7-80+(len(app.input)-1)*25,size = 20,align='left',fill="yellow", border="black")
                
        drawRect(650,app.height*6//7+60,100,50,fill='yellow',border ='black',borderWidth=5)
        if app.questionMode == 2:
            drawLabel('Enter',700,app.height*6//7+85,size= 25, bold = True)
        elif app.questionMode == 1:
            drawLabel('Next',700,app.height*6//7+85,size= 25, bold = True)
        drawRect(50,app.height*6//7+60,100,50,fill='yellow',border ='black',borderWidth=5)
        drawLabel('Clear',100,app.height*6//7+85,size= 25, bold = True)
        
        if app.questionMode == 2:
            if app.currentQuestionCorrect==2:
                drawRect(app.width//4,app.height//4,app.width//2,app.height//2,fill='white',border = 'black', borderWidth = 5)
                drawLabel('Well Done!',app.width//2,app.height//2 - 30, size = 40, bold = True)
                drawLabel('Your Answer Is Correct!',app.width//2,app.height//2+20, size = 30, bold = True)
                drawRect(3*app.width//4-100,3*app.height//4-50,100,50,fill='yellow',border = 'black',borderWidth = 5)
                drawLabel('Next',3*app.width//4-50,3*app.height//4-25,size = 25, bold = True)
            elif app.currentQuestionCorrect==1 and app.tries<3:
                drawRect(app.width//4,app.height//4,app.width//2,app.height//2,fill='white',border = 'black', borderWidth = 5)
                drawLabel('Try Again!',app.width//2,app.height//2 - 30, size = 40, bold = True)
                drawLabel(f'You have {3-app.tries} tries left',app.width//2,app.height//2+20, size = 30, bold = True)
                drawRect(3*app.width//4-100,3*app.height//4-50,100,50,fill='yellow',border = 'black',borderWidth = 5)
                drawLabel('Next',3*app.width//4-50,3*app.height//4-25,size = 25, bold = True)
            elif app.currentQuestionCorrect==1 and app.tries>=3:
                drawRect(app.width//4,app.height//4,app.width//2,app.height//2,fill='white',border = 'black', borderWidth = 5)
                drawLabel('The Correct',app.width//2,app.height//2 - 100, size = 40, bold = True)
                drawLabel('Answer Was:',app.width//2,app.height//2 - 50, size = 40, bold = True)
                answerSplittedLine = app.questionBank[question]["answer"].splitlines()
                #answerSplittedLine  = app.testAnswer.splitlines()
                for i in range(len(answerSplittedLine)):
                    drawLabel(answerSplittedLine[i],app.width//4+30,app.height//2+25*i, align= 'left',size = 20)
                drawRect(3*app.width//4-100,3*app.height//4-50,100,50,fill='yellow',border = 'black',borderWidth = 5)
                drawLabel('Next',3*app.width//4-50,3*app.height//4-25,size = 25, bold = True)

        elif app.questionMode == 1:
            seconds = app.timeLeft%60
            minutes = (app.timeLeft - seconds)//60
            if len(str(seconds))<2:
                seconds = '0'+str(seconds)
            drawLabel(f'{minutes}:{seconds} left', app.width*4//5,app.height//8, size = 40, bold = True)
    elif app.finalQuestions == None:
        drawLabel('Erorr',app.width//2,app.height//4,size = 40, bold = True)
        drawLabel('We currently do not have sufficient questions',app.width//2,app.height//3,size = 25)
        drawLabel('in our question bank that match your needs ',app.width//2,app.height//3+40,size = 25)
        drawLabel('Please modify your settings',app.width//2,app.height//3+120,size = 25)
        drawLabel('by reducing number of questions or selecting more topics.',app.width//2,app.height//3+160,size = 25)
        drawLabel('We are sorry for the inconvenience. :(',app.width//2,app.height//3+200,size = 25)
        drawRect(app.width//2,app.height//3+300,150,75,align='center',fill='yellow',border='black',borderWidth = 5)
        drawLabel('Back',app.width//2,app.height//3+300,size = 30, bold = True)
        

def drawResults(app):
    drawLabel("Results:",app.width//2,app.height//3-100, size = 70,bold = True)
    if app.correct/len(app.finalQuestions)>0.5:
        drawLabel(f"Well Done! You got {app.correct} out of {len(app.finalQuestions)}",app.width//2,app.height//2-100, size =50)
    else:
        drawLabel(f"You got {app.correct} out of {len(app.finalQuestions)}.",app.width//2,app.height//2-100, size =50)
        drawLabel(f"Practice some more!",app.width//2,app.height//2-40, size =50)
    if app.questionMode == 2:
        drawLabel('Replay with the same settings, or change your selections!',app.width//2,app.height*2//3,size=30)
        drawRect(app.width//2-app.width//8,app.height*2//3+100,150,75,fill='yellow',border='black',borderWidth = 5,align = 'center')
        drawRect(app.width//2+app.width//8,app.height*2//3+100,150,75,fill='yellow',border='black',borderWidth = 5,align = 'center')
        drawLabel("Replay",app.width//2-app.width//8,app.height*2//3+100,size = 30,bold = True)
        drawLabel("Settings",app.width//2+app.width//8,app.height*2//3+100,size = 30, bold = True)
    elif app.questionMode == 1:
        drawLabel("Check your answers!",app.width//2,app.height*2//3-75,size = 30)
        drawRect(app.width//2,app.height*2//3,150,75,fill='yellow',border='black',borderWidth = 5,align = 'center')
        drawLabel("Review",app.width//2,app.height*2//3,size = 30,bold = True)

        drawLabel('Replay with the same settings, or change your selections!',app.width//2,app.height*2//3+75,size=30)
        drawRect(app.width//2-app.width//8,app.height*2//3+150,150,75,fill='yellow',border='black',borderWidth = 5,align = 'center')
        drawRect(app.width//2+app.width//8,app.height*2//3+150,150,75,fill='yellow',border='black',borderWidth = 5,align = 'center')
        drawLabel("Replay",app.width//2-app.width//8,app.height*2//3+150,size = 30,bold = True)
        drawLabel("Settings",app.width//2+app.width//8,app.height*2//3+150,size = 30, bold = True)
 
def drawReview(app):
    print(app.incorrectAnswers)
    drawRect(app.width//2,app.height//2,4*app.width//5,4*app.height//5,align = 'center', fill = 'white',border = 'black', borderWidth = 5)
    drawLabel(f"Review: Question {app.currentQuestion+1}",app.width//2,app.height//10+30,size = 30, bold = True)
    correct = True
    userInput = None
    for number,answer in app.incorrectAnswers:
        if number == app.currentQuestion:
            correct = False
            userInput = answer
    print('user input:',userInput)
    if correct: status = 'Correct'
    else: status = 'Incorrect'
    drawLabel(f'Answer: {status}',app.width//2, app.height//10+60, size = 20)
    question = app.finalQuestions[app.currentQuestion]
    print(f"question: {question}")
        # imageWidth, imageHeight = getImageSize(question)

    drawImage(question, app.width//2, app.height*4//10, align='center',width=4*app.width//6, height=app.height*4//10)

    drawLabel("Your Answer:",app.width//2-app.width//6,app.height*6//10+10,size = 20,bold = True)
    drawLabel("Actual Answer:",app.width//2+app.width//6,app.height*6//10+10, size = 20, bold = True)

    if correct == False:
        answerSplittedLine = app.questionBank[question]["answer"].splitlines()
        #answerSplittedLine  = app.testAnswer.splitlines()
        for i in range(len(answerSplittedLine)):
            drawLabel(answerSplittedLine[i],app.width//2+30,app.height*6//10+50+i*25, align= 'left',size = 20)
        for lineIndex in range(len(userInput)):
            drawLabel(userInput[lineIndex],app.width//10+30,app.height*6//10+50+lineIndex*25,size = 20,align = 'left')
    
    else:
        answerSplittedLine = app.questionBank[question]["answer"].splitlines()
        #answerSplittedLine  = app.testAnswer.splitlines()
        for i in range(len(answerSplittedLine)):
            drawLabel(answerSplittedLine[i],app.width//2+30,app.height*6//10+50+i*25, align= 'left',size = 20)
            drawLabel(answerSplittedLine[i],app.width//10+30,app.height*6//10+50+i*25, align= 'left',size = 20)

    drawRect(app.width//10+10,app.height*9//10-60,100,50,fill = 'yellow',border = 'black', borderWidth = 5)
    drawRect(9*app.width//10-110,app.height*9//10-60,100,50,fill = 'yellow',border = 'black', borderWidth = 5)
    drawRect(app.width//2,app.height*9//10-35,100,50,fill = 'yellow',border = 'black', borderWidth = 5,align = 'center')
    drawLabel("Back",app.width//10+60,app.height*9//10-35,size = 20, bold = True)
    drawLabel("Next",app.width*9//10-60,app.height*9//10-35,size = 20, bold = True)
    drawLabel("Close",app.width//2,app.height*9//10-35,size = 20, bold = True)

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def stripSpaces(input):
    strippedInput = ''
    for line in input:
        for character in line:
            if character == ' ':
                pass
            else:
                strippedInput+=character
        strippedInput+='\n'
    strippedInput = strippedInput.strip()
    return strippedInput

def checkInput(app):
    strippedInput = stripSpaces(app.input)
    strippedAnswer = ''
    for i in app.questionBank[app.finalQuestions[app.currentQuestion]]["answer"]:
        if i!=' ':
            strippedAnswer+=i


    print(strippedAnswer,strippedInput)
    print(strippedAnswer == strippedInput)
    print("\n")
    print(f"stripped: {strippedInput}")
    #if strippedInput == app.testAnswer:
    if app.questionMode == 2:
        if strippedInput == strippedAnswer:
            print('ANSWER IS THE SAME')
            app.currentQuestionCorrect = 2
        else:
            app.currentQuestionCorrect = 1
            print(strippedInput)
            print('ANSWER IS WRONG')
    elif app.questionMode == 1:
        if strippedInput == strippedAnswer:
            app.correct+=1
        else:
            app.incorrectAnswers.append((app.currentQuestion,app.input))

def onStep(app):
    if app.questions and app.questionMode == 1:
        if app.timeLeft>0:
            app.timeLeft-=1
        elif app.timeLeft<=0:
            checkInput(app)
            if app.currentQuestion+1>=len(app.finalQuestions):
                app.results = True
                app.questions = False
            else: 
                app.currentQuestion+=1
                app.input=['']
                app.timeLeft = app.timePerCT



def onMousePress(app,mouseX,mouseY):
    if app.welcome:
        if app.width//2-75<=mouseX<=app.width//2+75 and app.height//2-97.5<=mouseY<=app.height//2-22.5:
            app.welcome = False
            app.topics = True
        elif app.width//2-75<=mouseX<=app.width//2+75 and app.height//2+22.5<=mouseY<=app.height//2+97.5:
            app.welcome = False
            app.about = True
        elif app.width//2-75<=mouseX<=app.width//2+75 and app.height//2+142.5<=mouseY<=app.height//2+217.5:
            app.welcome = False
            app.credits = True
    elif app.about:
        if app.width//2-50<=mouseX<=app.width//2+50 and app.height//2+7*app.height//20-25<=mouseY<=app.height//2+7*app.height//20+25:
            app.about = False
            app.welcome = True
    elif app.credits:
        if app.width//2-50<=mouseX<=app.width//2+50 and app.height//2+5*app.height//20-25<=mouseY<=app.height//2+5*app.height//20+25:
            app.credits = False
            app.welcome = True
    elif app.topics:
        app.width-60,app.height-35,100,50
        for i in range(len(app.topicList)):
            if app.width//6<=mouseX<=app.width//6+30 and 3*app.height//10+i*40<=mouseY<=3*app.height//10+i*40+30:
                if i==len(app.topicList)-1 and i not in app.selectedTopic:
                    for j in range(len(app.topicList)):
                        app.selectedTopic.add(j)
                elif i==len(app.topicList)-1 and i in app.selectedTopic:
                    app.selectedTopic = set()
                elif i not in app.selectedTopic:
                    app.selectedTopic.add(i)
                else:
                    app.selectedTopic.remove(i)
        if app.width-110<=mouseX<=app.width-10 and app.height-60<=mouseY<=app.height-10 and app.selectedTopic!=set():
            app.topics = False
            app.settings = True
    elif app.settings:
        if app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and app.height//4-25<=mouseY<=app.height//4+25:
            if app.difficulty != 1:
                app.difficulty = 1
            else:
                app.difficulty = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and app.height//4-25<=mouseY<=app.height//4+25:
            if app.difficulty != 2:
                app.difficulty = 2
            else:
                app.difficulty = 0
        elif app.width//2-3*app.width//12-50<=mouseX<=app.width//2-3*app.width//12+50 and app.height//2-75-25<=mouseY<=app.height//2-75+25:
            if app.numberOfQuestions != 1:
                app.numberOfQuestions = 1
            else:
                app.numberOfQuestions = 0
        elif app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and app.height//2-75-25<=mouseY<=app.height//2-75+25:
            if app.numberOfQuestions != 2:
                app.numberOfQuestions = 2
            else:
                app.numberOfQuestions = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and app.height//2-75-25<=mouseY<=app.height//2-75+25:
            if app.numberOfQuestions != 3:
                app.numberOfQuestions = 3
            else:
                app.numberOfQuestions = 0
        elif app.width//2+3*app.width//12-50<=mouseX<=app.width//2+3*app.width//12+50 and app.height//2-75-25<=mouseY<=app.height//2-75+25:
            if app.numberOfQuestions != 4:
                app.numberOfQuestions = 4
            else:
                app.numberOfQuestions = 0
        elif app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and 2*app.height//3-50<=mouseY<=2*app.height//3:
            if app.questionMode!=1:
                app.questionMode = 1
            else:
                app.questionMode = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and 2*app.height//3-50<=mouseY<=2*app.height//3:
            if app.questionMode!=2:
                app.questionMode = 2
            else:
                app.questionMode = 0    
        elif app.width-220<=mouseX<=app.width-110 and app.height-60<=mouseY<=app.height-10:
            app.topics = True
            app.settings = False
        elif (app.width-110<=mouseX<=app.width-10 and 
              app.height-60<=mouseY<=app.height-10 and 
              app.numberOfQuestions!=0 and
              app.questionMode!=0 and
              app.difficulty!=0):
                    app.settings = False    
                    app.questions = True
                    app.timeLeft = app.timePerCT
                    loadQuestions(app) 
        elif app.questionMode==1 and distance(app.timeBulbX,app.height*3//4+50,mouseX,mouseY)<=20:
            print('bulb is clickedd')
            app.bulbClicked = True
        
    elif app.questions:
        if app.finalQuestions == None:
            if app.width//2-75<=mouseX<=app.width//2+75 and app.height//3+300-75/2<=mouseY<=app.height//3+300+75/2:
                app.questions = False
                app.topics = True      
        elif app.questionMode == 2:
            if 3*app.width//4-100<=mouseX<=3*app.width//4 and 3*app.height//4-50<=mouseY<=3*app.height//4 and app.currentQuestionCorrect==2:
                app.currentQuestionCorrect = 0
                if app.currentQuestion+1>=len(app.finalQuestions):
                    app.results = True
                    app.questions = False
                else: 
                    app.currentQuestion+=1
                    app.input=['']
                    app.tries = 0
                    app.correct+=1
            elif 3*app.width//4-100<=mouseX<=3*app.width//4 and 3*app.height//4-50<=mouseY<=3*app.height//4 and app.currentQuestionCorrect==1:
                app.tries += 1
                app.input=['']
                app.currentQuestionCorrect = 0
                if app.tries>3:
                    if app.currentQuestion+1>=len(app.finalQuestions):
                        app.results = True
                        app.questions = False
                    else: 
                        app.currentQuestion+=1
                        app.input=['']
                        app.tries = 0
            elif 650<=mouseX<=750 and app.height*6//7+60<=mouseY<=app.height*6//7+110:
                checkInput(app)
            elif 50<=mouseX<=150 and app.height*6//7+60<=mouseY<=app.height*6//7+110:
                app.input = ['']
        elif app.questionMode == 1:
            if 650<=mouseX<=750 and app.height*6//7+60<=mouseY<=app.height*6//7+110:
                checkInput(app)
                if app.currentQuestion+1>=len(app.finalQuestions):
                    app.results = True
                    app.questions = False
                else: 
                    app.currentQuestion+=1
                    app.input=['']
                    app.timeLeft = app.timePerCT
        

    elif app.results:
        if app.questionMode == 2:
            if app.width//2-app.width//8-75<=mouseX<=app.width//2-app.width//8+75 and app.height*2//3+100-75/2<=mouseY<=app.height*2//3+100+75/2:
                app.result = False
                loadQuestions(app)
                reset(app)
                app.questions = True
            elif app.width//2+app.width//8-75<=mouseX<=app.width//2+app.width//8+75 and app.height*2//3+100-75/2<=mouseY<=app.height*2//3+100+75/2:
                app.topics = True
                app.result = False
                reset(app)
        elif app.questionMode == 1: 
            if app.width//2-75<=mouseX<=app.width//2+75 and app.height*2//3-75/2<=mouseY<=app.height*2//3+75/2:
                print('review time')
                app.currentQuestion = 0
                app.review = True
            elif not app.review and app.width//2-app.width//8-75<=mouseX<=app.width//2-app.width//8+75 and app.height*2//3+150-75/2<=mouseY<=app.height*2//3+150+75/2:
                app.result = False
                loadQuestions(app)
                reset(app)
                app.questions = True
            elif not app.review and app.width//2+app.width//8-75<=mouseX<=app.width//2+app.width//8+75 and app.height*2//3+150-75/2<=mouseY<=app.height*2//3+150+75/2:
                app.topics = True
                app.result = False
                reset(app)


        if app.review:
            if app.width//10+10<=mouseX<=app.width//10+110 and app.height*9//10-60<=mouseY<=app.height*9//10-10:
                if app.currentQuestion>0:
                    app.currentQuestion-=1
            elif app.width*9//10-110<=mouseX<=app.width*9//10-10 and app.height*9//10-60<=mouseY<=app.height*9//10-10:
                if app.currentQuestion<len(app.finalQuestions)-1:
                    app.currentQuestion+=1
            elif app.width//2-50<=mouseX<=app.width//2+50 and app.height*9//10-60<=mouseY<=app.height*9//10-10:
                app.review = False
    print(app.selectedTopic)

def onMouseDrag(app,mouseX,mouseY):
    if app.questionMode == 1 and app.bulbClicked:
        app.timePerCT = (app.timeBulbX - app.width//4)*360//(app.width//2)
        if mouseX>=3*app.width//4:
            app.timeBulbX = 3*app.width//4
        elif mouseX<=app.width//4:
            app.timeBulbX = app.width//4
        else:
            app.timeBulbX = mouseX

def onMouseRelease(app,mouseX,mouseY):
    if app.questionMode == 1 and app.bulbClicked:
        app.bulbClicked = False

def onKeyPress(app,key):
    if app.questions:
        if key == 'enter':
            app.input.append('')
        elif key == 'tab':
            pass
        elif key == 'backspace' or key == 'delete':
            if app.input!=[] and app.input!=['']:
                if app.input[-1]=='':
                    app.input.pop()
                else:
                    app.input[-1]=app.input[-1][:-1]
        elif key == 'space':
            app.input[-1]+=' '
        elif key.isdigit():
            app.input[-1]+=str(key)
        elif key.isalpha():
            app.input[-1]+=str(key)
        else:
            app.input[-1]+=str(key)
        
    print(key)

def main():
    runApp()
main()