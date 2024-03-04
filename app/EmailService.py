class EmailService:

    #email addresses to send notifications to
    emails = []

    #message to show once printing is done
    printingDoneMessage = ""


    """
    init email service
    """
    def __init__(self, emails, printingDoneMessage):
        self.emails = emails
        self.printingDoneMessage = printingDoneMessage


    """
    update emails
    send "ON" to turn on
    send "OFF" to turn off
    """
    def updateEmails(self):
        #TODO:
        return

    
    """
    send email
    """
    def sendEmails(self):
        #TODO:
        print(self.printingDoneMessage)
        return
