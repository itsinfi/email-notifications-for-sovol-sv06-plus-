from app.JsonParser import readConfig
from app.HtmlParser import HtmlParser
from app.CronJobService import CronJobService
from app.EmailService import EmailService

#settings
config = {}

#read config
config = readConfig()

#init HtmlParser
htmlParser = HtmlParser(config['ip'], config['sovolUIlanguage'])

#init cron job
cronJobService = CronJobService(int(config['refreshRateInMinutes']))

#init email service
emailService = EmailService(config['emails'], config['printingDoneMessage'])



#update emails
#send "ON" to turn on
#send "OFF" to turn notifications off
# emailService.updateEmails()#TODO:

#check temp and send mail if temperature is lower (printer is turning off again)
sendNotification = htmlParser.checkTemp(float(config['threshold']))
print(sendNotification)

#send notification
if (sendNotification):
    emailService.sendEmails()



