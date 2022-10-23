
import re
import pandas as pd
import webbrowser

def startsWithDateTime(s):
    pattern = '\[(0?[1-9]|[1-2][0-9]|3[01])\/([1-9]|1[0-2])\/\d\d\d\d\, (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9]) (AM|PM)\]'
    result = re.match(pattern,s)
    if result:
        return True
    return False

def startsWithAuthor(s):
    patterns = [
        '(\w+:)',                          # First Name
        '(\w+\s+\w+\:)',                   # First Name + Last Name
        '(\+\d{2} \d{4} \d{4})',         # Mobile Number (Singapore)
        '([+]\d{2} \d{4} \d{6})',   # Mobile Number (UK)
    ]
    pattern = '(\w+\s+\w+\:)|(\w+:)|(\d{2} \d{4} \d{4})|([+]\d{2} \d{4} \d{6})'
    result = re.findall(pattern, s)
    if result :
        return True
    return False

def getDataPoint(line):
    # line = 18/06/17, 22:47 - Loki: Why do you have 2 numbers, Banner?
    start = line.find('[') 
    end = line.find(']')
    dateTime = line[start+1:end] # dateTime = '18/06/17, 22:47'
    date, time = dateTime.split(', ') # date = '18/06/17'; time = '22:47'
    message = ''.join(line[end+1:]) # message = 'Loki: Why do you have 2 numbers, Banner?'
    if startsWithAuthor(message): # True
        splitMessage = message.split(': ') # splitMessage = ['Loki', 'Why do you have 2 numbers, Banner?']
        author = splitMessage[0] # author = 'Loki'
        message = ' '.join(splitMessage[1:]) # message = 'Why do you have 2 numbers, Banner?'
    else:
        author = None
    return date, time, author, message

def main1():
    parsedData = [] # List to keep track of data so it can be used by a Pandas dataframe
    conversationPath = '_chat.txt'

    with open(conversationPath) as fp:
        fp.readline() # Skipping first line of the file (usually contains information about end-to-end encryption) 
        messageBuffer = [] # Buffer to capture intermediate output for multi-line messages
        date, time, author = None, None, None # Intermediate variables to keep track of the current message being processed
        
        while True:
            line = fp.readline()
            if not line: # Stop reading further if end of file has been reached
                break
            line = line.strip() # Guarding against erroneous leading and trailing whitespaces

            if startsWithDateTime(line): # If a line starts with a Date Time pattern, then this indicates the beginning of a new message
                if len(messageBuffer) >=0: # Check if the message buffer contains characters from previous iterations
                    parsedData.append([date, time, author, ' '.join(messageBuffer)]) # Save the tokens from the previous message in parsedData
                messageBuffer.clear() # Clear the message buffer so that it can be used for the next message
                date, time, author, message = getDataPoint(line) # Identify and extract tokens from the line
                messageBuffer.append(message) # Append message to buffer
            else:
                messageBuffer.append(line) # If a line doesn't start with a Date Time pattern, then it is part of a multi-line message. So, just append to buffer
    return parsedData

writer = pd.ExcelWriter('Whatsapp_Record.xlsx', engine = 'xlsxwriter')

def write (df,name,date,writer):
    df.to_excel(writer,sheet_name=date+'_'+name)
    df.to_csv(f'{date}_{name}.txt')
    df.to_csv(f'{date}_{name}.csv')
    return 

df = pd.DataFrame(main1(), columns=['Date', 'Time', 'Author', 'Message'])
df ['Date']=df['Date'].apply(lambda x: str(x).replace('/','-'))
lens=len(df)-1
date=df.iat[lens,0]
write(df,'Chat_History',date,writer)

dataframe=[]
for message in df['Message']:
    url="(?P<url>https?://[^\s]+)"
    url_found=re.findall(url,message)
    for url in url_found:
        name=df[df['Message']==message]['Author']
        name=name.values[0]
        dataframe.append([name,url])
    
df2= pd.DataFrame(dataframe,columns=['Name','URL'])
write(df2,'Perchase_List',date,writer)

def url_find_price(url):
    webbrowser.open(url, new=1)
    return 0

writer.save()
writer.close()


lens=len(df2)
df2=df2.drop (range(0,lens-5))
#df2['URL'].apply(lambda x: url_find_price(x))
