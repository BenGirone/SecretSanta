import smtplib
import random
import gmail

emails = [
    'participant1@gmail.com',
    'participant2@gmail.com',
    'participant3@gmail.com',
    'participant4@gmail.com',
    'participant5@gmail.com',
    'participant6@comcast.net'
]

emailToName = {
    'participant1@gmail.com': 'Ben',
    'participant2@gmail.com': 'Alyssa',
    'participant3@gmail.com': 'Will',
    'participant4@gmail.com': 'Maria',
    'participant5@gmail.com': 'Annie',
    'participant6@comcast.net': 'Johnny',
}

illegalCombos = [
    'participant1@gmail.com participant1@gmail.com',
    'participant2@gmail.com participant2@gmail.com',
    'participant3@gmail.com participant3@gmail.com',
    'participant4@gmail.com participant4@gmail.com',
    'participant5@gmail.com participant5@gmail.com',
    'participant6@comcast.net participant6@comcast.net',
    'participant1@gmail.com participant2@gmail.com',
    'participant2@gmail.com participant1@gmail.com',
    'participant3@gmail.com participant4@gmail.com',
    'participant4@gmail.com participant3@gmail.com'
]

def makeCombos():
    emailsToAssign = emails.copy()
    random.shuffle(emailsToAssign)
    combos = []

    for email in emails:
        for i in range(len(emailsToAssign)):
            if not((email + ' ' + emailsToAssign[i]) in illegalCombos):
                combos.append((email, emailsToAssign.pop(i)))
                break
            elif i == (len(emailsToAssign) - 1):
                return False
    
    return combos

combosToSend = makeCombos()
while combosToSend == False:
    combosToSend = makeCombos()

def email_text(combo):
    return "From: %s\nTo: %s\nSubject: %s\n\n%s" % (gmail.user, combo[0], 'Secret Santa', 'You must get a gift for ' + emailToName[combo[1]])

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail.user, gmail.password)

    for combo in combosToSend:
        server.sendmail(gmail.user, combo[0], email_text(combo))
        print('Email sent!')

    server.close()
except:
    print('Something went wrong...')
