import lib.clock as clock
import config


class Status:
    def __init__(self):
        self.result = bool
        self.time = clock.get_now()
        self.crash_info = str

    def get_now_inform(self):
        return self.time.strftime(config.TIME_FORMAT)

    def get_report_time_inform(self):
        return self.time.strftime(config.CRASH_REPORT_NAME_FORMAT)
