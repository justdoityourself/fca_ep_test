import imaplib
import time 

def get_last_email_code():
    time.sleep( 3 ) 
    mail = imaplib.IMAP4('firstchairanalytics.com',143)
    mail.login('test@firstchairanalytics.com', 'fca12345$$$')
    mail.list()

    mail.select("inbox") 

    result, data = mail.search(None, "ALL")
    
    ids = data[0] 
    id_list = ids.split() 
    latest_email_id = id_list[-1] 
    
    result, data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = data[0][1] 

    return raw_email.decode().rpartition('activation_code>')[2][0:6]
  
    #return raw_email.decode().rpartition('Use this code to activate EchoPractice: ')[2][0:19]

