import smtplib
import random
import gmail

emails = [
    'benjamingirone@gmail.com',
    'itsalyssagirone@gmail.com',
    'willgironefitness@gmail.com',
    'maria.f.wendt@gmail.com',
    'Anne.Pook04@gmail.com',
    'john.girone@comcast.net'
]

emailToName = {
    'benjamingirone@gmail.com': 'Ben',
    'itsalyssagirone@gmail.com': 'Alyssa',
    'willgironefitness@gmail.com': 'Will',
    'maria.f.wendt@gmail.com': 'Maria',
    'Anne.Pook04@gmail.com': 'Annie',
    'john.girone@comcast.net': 'Johnny',
}

illegalCombos = [
    'benjamingirone@gmail.com benjamingirone@gmail.com',
    'itsalyssagirone@gmail.com itsalyssagirone@gmail.com',
    'willgironefitness@gmail.com willgironefitness@gmail.com',
    'maria.f.wendt@gmail.com maria.f.wendt@gmail.com',
    'Anne.Pook04@gmail.com Anne.Pook04@gmail.com',
    'john.girone@comcast.net john.girone@comcast.net',
    'benjamingirone@gmail.com itsalyssagirone@gmail.com',
    'itsalyssagirone@gmail.com benjamingirone@gmail.com',
    'willgironefitness@gmail.com maria.f.wendt@gmail.com',
    'maria.f.wendt@gmail.com willgironefitness@gmail.com'
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
