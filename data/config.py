import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
import requests
import shutil 
import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1ThYANJ2x2FAcFM4htgc3C3mQ03mIEMvjjhVjEyQ-gzA'
SAMPLE_RANGE_NAME = 'A1:AA1000'

def main():
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../credentials.json', SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input:
        print('No data found.')

main()

df=pd.DataFrame(values_input[1:], columns=values_input[0])

total = ""

class Question(object):
    def __init__(self, answer, topic, difficulty, origin):
        self.topic = topic
        self.difficulty = difficulty
        self.origin = origin
        self.question = question
        self.answer = answer
        
dict = {}
big_dict = {}

# Getting images from link
for i in range(len(df)):
    question = df['Question'][i]
    # res = requests.get(url, stream = True)
    id = df['ID'][i]
    # file_name = "../images/" + id + '.png'
    topic = df['Topic'][i]
    difficulty = df['Difficulty'][i]
    origin = df["Origin"][i]
    answer = df['Answer'][i]

    # img_data = requests.get(url).content
    # if res.status_code == 200:
    #     with open(file_name,'wb') as f:
    #         shutil.copyfileobj(res.raw, f)
    #         # f.write(img_data)
    #         print('Image sucessfully Downloaded: ',file_name)
    # else:
    #     print(res.status_code)
    #     print('Image Couldn\'t be retrieved')
        
    id = Question(answer, topic, difficulty, origin)
    # jsonString = json.dumps(id.__dict__)
    dict[question] = vars(id)

big_dict["data"] = dict
with open("data.json", "w") as outfile:
    outfile.write(json.dumps(big_dict))
    
    
        



