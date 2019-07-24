import imapclient
from twilio.rest import Client

"""Twilio account id and authorization token"""
accountSID = 'accountSID' #insert accountSID from twilio
authToken = 'authToken' #insert authToken from twilio

"""Call Twilio Client and pass the accountid and authtoken
    then give the numbers"""
twilioCli = Client(accountSID,authToken)
myTwilioNumber = 'twilioPhoneNumber' #insert twilio phone number to send text
myCellPhone = 'cellPhoneNumber' #insert cellphone number to receive texts

def emailCall():
    """Imap client information"""
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login('somemail@gmail.com', 'somePassword') #enter email and password
    imapObj.select_folder('INBOX') # could change to another folder in email
    messages = imapObj.search(['FROM', 'emailaddress@domain.com']) #supply from email address to search from

    """declare two lists msgIDs will hold the stored message ids from the 
        messageID.txt file and ids will hold the IDs from gmail """
    msgIDs=[]
    ids = []

    """Open messageID.txt and append items to the msgIDs list
        will create a file if one does not exist"""
    with open('messageID.txt','r+') as mFile:
        for item in mFile:
            msgIDs.append(item.rstrip('\n'))
    mFile.close()
    #print(msgIDs)

    """find all the message information from the email """
    for msgid, data in imapObj.fetch(messages,['ENVELOPE']).items():
        envelope = data[b'ENVELOPE']
        """convert the msgid to a string and append to the ids list"""
        msid = str(msgid)
        ids.append(msid)
        #print(ids)
        
        """if the msid is not in the msgIDs list then send a text and write to the messageid.txt file"""
        if msid not in msgIDs:
            twilioCli.messages.create(body='ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date),from_=myTwilioNumber,to=myCellPhone)
            with open('messageID.txt','a+') as f:
                f.write('%s\n' % msid)
            f.close()

if __name__ == "__main__":
    emailCall()

