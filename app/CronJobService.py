class CronJobService:
    
    #refresh rate in minutes (default 5min)
    refreshRateInMinutes: int = 5
    
    #init cron job
    def __init__(self, refreshRateInMinutes):
        self.refreshRateInMinutes = refreshRateInMinutes

    def execCronJob():
        #TODO:
        return