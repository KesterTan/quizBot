from cmu_cs3_graphics import *
import json
import random

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
    app.credits = False
    app.topics = False
    app.settings = False
    app.questions = False
    app.topicList = {0:'Loops',1:'Strings',2:'Animations',3:'1D Lists and Tuples',4:'2D Lists',5:'Sets & Dictionaries',6:'Object Oriented Programming',7:'Recursion'}
    app.selectedTopic = set()
    app.difficulty = 0
    app.numberOfQuestions = 0
    app.questionMode = 0
    app.finalQuestions = []
    app.currentQuestion = 0
    app.input = ['']
    

def loadQuestions(app):
    suitableQuestions = set()
    for question in app.questionBank:
        # print(app.questionBank[question]["topic"])
        # print(app.selectedTopic)
        
        # print("-----")
        # print(app.questionBank[question]["difficulty"])
        # print(app.difficulty)
        
        # print("-----")
        # print("topic")
        # print((int(app.questionBank[question]["topic"])) in app.selectedTopic)
        
        # print("difficulty")
        if int(app.questionBank[question]["topic"]) in app.selectedTopic and int(app.questionBank[question]["difficulty"])+1==int(app.difficulty):
            # print(f"adding: {question}")
            suitableQuestions.add(question)
            
    if app.numberOfQuestions<len(suitableQuestions):
        app.finalQuestions = random.sample(suitableQuestions,app.numberOfQuestions)
    else:
        app.finalQuestions = random.shuffle(list(suitableQuestions))
    
def redrawAll(app):
    if app.welcome:
        drawWelcome(app)
    elif app.credits:
        drawCredit(app)
    elif app.topics:
        drawTopics(app)
    elif app.settings:
        drawSettings(app)
    elif app.questions:
        drawQuestions(app)

def drawWelcome(app):
    drawLabel("112 Study Buddy",app.width//2,app.height//4,bold = True, size = 60)
    #import 112 dragon or smth
    drawRect(app.width//2,app.height//2-60,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Study!",app.width//2,app.height//2-60,size = 25, bold = True)
    drawRect(app.width//2,app.height//2+60,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Credits",app.width//2,app.height//2+60,size = 25, bold = True)

def drawCredit(app):
    drawLabel("112 Study Buddy made at Hack 112",app.width//2,app.height//3,size = 40)
    drawLabel("Made by:",app.width//2, app.height//2, size = 40)
    drawLabel("Shermern Ang (shermera)",app.width//2,app.height//2+app.height//20, size = 30)
    drawLabel("Kester Tan (kestert)",app.width//2,app.height//2+2*app.height//20,size = 30)
    drawLabel("Joshua Tsang (jtsang2)",app.width//2,app.height//2+3*app.height//20,size =30)
    drawRect(app.width//2,app.height//2+5*app.height//20,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Back",app.width//2,app.height//2+5*app.height//20,size = 25, bold = True)

def drawTopics(app):
    drawLabel("Topics:",app.width//2,app.height//8, size = 50,bold = True)
    drawLabel("Select all the topics you want to study!",app.width//2,app.height//5, size =30)
    for i in range(8):
        drawRect(app.width//6,3*app.height//10+i*40,30,30,fill = None, border = 'black')
    for key in app.topicList:
        drawLabel(app.topicList[key],app.width//4,3*app.height//10+key*40+15,align = 'left',size =25)
    
    for checkIndex in app.selectedTopic:
        drawLine(app.width//6,3*app.height//10+checkIndex*40+10,app.width//6+15,3*app.height//10+checkIndex*40+30,fill= 'lightGreen',lineWidth = 5)
        drawLine(app.width//6+15,3*app.height//10+checkIndex*40+30,app.width//6+40,3*app.height//10+checkIndex*40-10,fill= 'lightGreen',lineWidth = 5)
    drawRect(app.width-60,app.height-35,100,50,align = 'center', fill='yellow',borderWidth = 5, border = 'black')
    drawLabel("Next",app.width-60,app.height-35,size = 25, bold = True)


def drawSettings(app):
    drawLabel("Settings:",app.width//2,app.height//8, size = 50,bold = True)
    drawLabel("Customize your study session!",app.width//2,app.height//5, size =20)
    drawLabel("Difficulty",app.width//2,app.height//4+10,size = 30, bold = True)
    if app.difficulty==0:
        bonusCol = None
        normalCol = None
    elif app.difficulty==1:
        bonusCol = None
        normalCol = 'lightGreen'
    elif app.difficulty==2:
        bonusCol = 'lightGreen'
        normalCol = None
    drawRect(app.width//2-app.width//12,app.height//3,100,50,align = 'center',fill=normalCol,borderWidth = 2, border = 'black')
    drawRect(app.width//2+app.width//12,app.height//3,100,50,align = 'center',fill=bonusCol,borderWidth = 2, border = 'black')
    drawLabel('Normal',app.width//2-app.width//12,app.height//3,size=25)
    drawLabel('Bonus',app.width//2+app.width//12,app.height//3,size=25)
    
    drawLabel("Number of Questions",app.width//2,app.height//2-50,size = 30, bold = True)
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
    drawRect(app.width//2-3*app.width//12,app.height//2+20,100,50,align = 'center',fill=fiveQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2-app.width//12,app.height//2+20,100,50,align = 'center',fill=tenQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2+app.width//12,app.height//2+20,100,50,align = 'center',fill=fifteenQ,borderWidth = 2, border = 'black')
    drawRect(app.width//2+3*app.width//12,app.height//2+20,100,50,align = 'center',fill=twentyQ,borderWidth = 2, border = 'black')
    drawLabel('1',app.width//2-3*app.width//12,app.height//2+20,size=25)
    drawLabel('2',app.width//2-app.width//12,app.height//2+20,size=25)
    drawLabel('3',app.width//2+app.width//12,app.height//2+20,size=25)
    drawLabel('4',app.width//2+3*app.width//12,app.height//2+20,size=25)

    drawLabel("Mode",app.width//2,2*app.height//3-30,size=30,bold =True)
    if app.questionMode == 0:
        examCol = None
        practiceCol = None
    elif app.questionMode == 1:
        examCol = 'lightGreen'
        practiceCol = None
    elif app.questionMode == 2:
        examCol = None
        practiceCol = 'lightGreen'
    drawLabel("Exam Mode: Timed & 1 Attempt per Question",app.width//2,2*app.height//3,size=20)
    drawLabel("Practice Mode: Untimed & Unlimited Attempts",app.width//2,2*app.height//3+25,size=20)
    drawRect(app.width//2-app.width//12,3*app.height//4+20,100,50,align='center',borderWidth=2,border='black',fill=examCol)
    drawRect(app.width//2+app.width//12,3*app.height//4+20,100,50,align='center',borderWidth=2,border='black',fill=practiceCol)
    drawLabel("Exam",app.width//2-app.width//12,3*app.height//4+20,size = 25)
    drawLabel("Practice",app.width//2+app.width//12,3*app.height//4+20,size = 25)

    drawRect(app.width-110,app.height-60,100,50,fill='yellow',border='black',borderWidth = 5)
    drawRect(app.width-220,app.height-60,100,50,fill='yellow',border='black',borderWidth = 5)
    drawLabel("Next",app.width-60,app.height-35,size = 25, bold = True)
    drawLabel("Back",app.width-170,app.height-35,size = 25, bold = True)

def drawQuestions(app):
    print(f"final: {app.finalQuestions}")
    question = app.finalQuestions[app.currentQuestion]
    print(f"question: {question}")
    # imageWidth, imageHeight = getImageSize(question)

    drawImage(question, 325, 200, align='center',width=400, height=300)

    drawRect(app.width//2,app.height*6//7,700,220,align='center',fill=None,border = 'black', borderWidth = 5)
    drawLabel("Type your answer here:",app.width//2-675/2,app.height*6//7-130,size = 30, bold = True,align='left')
    for lineIndex in range(len(app.input)):
        drawLabel(app.input[lineIndex],app.width//2-650/2,app.height*6//7-80+lineIndex*25,size = 20,align = 'left')
    drawRect(650,app.height*6//7+60,100,50,fill='yellow',border ='black',borderWidth=5)
    drawLabel('Enter',700,app.height*6//7+85,size= 25, bold = True)
    drawRect(50,app.height*6//7+60,100,50,fill='yellow',border ='black',borderWidth=5)
    drawLabel('Clear',100,app.height*6//7+85,size= 25, bold = True)

def checkInput(app):
    pass

def onMousePress(app,mouseX,mouseY):
    if app.welcome:
        if app.width//2-50<=mouseX<=app.width//2+50 and app.height//2-85<=mouseY<=app.height//2-35:
            app.welcome = False
            app.topics = True
        if app.width//2-50<=mouseX<=app.width//2+50 and app.height//2+35<=mouseY<=app.height//2+85:
            app.welcome = False
            app.credits = True
    elif app.credits:
        if app.width//2-50<=mouseX<=app.width//2+50 and app.height//2+5*app.height//20-25<=mouseY<=app.height//2+5*app.height//20+25:
            app.credits = False
            app.welcome = True
    elif app.topics:
        app.width-60,app.height-35,100,50
        for i in range(8):
            if app.width//6<=mouseX<=app.width//6+30 and 3*app.height//10+i*40<=mouseY<=3*app.height//10+i*40+30:
                if i not in app.selectedTopic:
                    app.selectedTopic.add(i)
                else:
                    app.selectedTopic.remove(i)
        if app.width-110<=mouseX<=app.width-10 and app.height-60<=mouseY<=app.height-10 and app.selectedTopic!=set():
            app.topics = False
            app.settings = True
    elif app.settings:
        if app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and app.height//3-25<=mouseY<=app.height//3+25:
            if app.difficulty != 1:
                app.difficulty = 1
            else:
                app.difficulty = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and app.height//3-25<=mouseY<=app.height//3+25:
            if app.difficulty != 2:
                app.difficulty = 2
            else:
                app.difficulty = 0
        elif app.width//2-3*app.width//12-50<=mouseX<=app.width//2-3*app.width//12+50 and app.height//2+20-25<=mouseY<=app.height//2+20+25:
            if app.numberOfQuestions != 1:
                app.numberOfQuestions = 1
            else:
                app.numberOfQuestions = 0
        elif app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and app.height//2+20-25<=mouseY<=app.height//2+20+25:
            if app.numberOfQuestions != 2:
                app.numberOfQuestions = 2
            else:
                app.numberOfQuestions = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and app.height//2+20-25<=mouseY<=app.height//2+20+25:
            if app.numberOfQuestions != 3:
                app.numberOfQuestions = 3
            else:
                app.numberOfQuestions = 0
        elif app.width//2+3*app.width//12-50<=mouseX<=app.width//2+3*app.width//12+50 and app.height//2+20-25<=mouseY<=app.height//2+20+25:
            if app.numberOfQuestions != 4:
                app.numberOfQuestions = 4
            else:
                app.numberOfQuestions = 0
        elif app.width//2-app.width//12-50<=mouseX<=app.width//2-app.width//12+50 and 3*app.height//4-5<=mouseY<=3*app.height//4+45:
            if app.questionMode!=1:
                app.questionMode = 1
            else:
                app.questionMode = 0
        elif app.width//2+app.width//12-50<=mouseX<=app.width//2+app.width//12+50 and 3*app.height//4-5<=mouseY<=3*app.height//4+45:
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
                    loadQuestions(app) 
    elif app.questions:
        if 650<=mouseX<=750 and app.height*6//7+60<=mouseY<=app.height*6//7+110:
            checkInput(app)
        elif 50<=mouseX<=150 and app.height*6//7+60<=mouseY<=app.height*6//7+110:
            app.input = ['']
    print(app.selectedTopic)

def onKeyPress(app,key):
    if app.questions:
        if key == 'enter':
            app.input.append('')
        elif key == 'tab':
            pass
        elif key == 'backspace' or key == 'delete':
            if app.input!=[]:
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