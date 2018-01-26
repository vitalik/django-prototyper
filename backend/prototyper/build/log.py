import logging
import traceback
from datetime import datetime


class LogHandler(logging.Handler):
    def __init__(self, logger):
        super(LogHandler, self).__init__()
        self.logger = logger
        
    def emit(self, record):
        print ('%20s %s' % (record.created, record.msg))
        self.logger.records.append(record)


class Logger(logging.Logger):
    def __init__(self):
        super(Logger, self).__init__('prototyper', logging.DEBUG)
        self.records = []
        self.addHandler(LogHandler(self))
    
    def serialize(self):
        result = []
        for rec in self.records:
            result.append({
                'time': str(datetime.fromtimestamp(rec.created).time()),#.strftime('%H:%m:%s'),
                'level': rec.levelname,
                'message': str(rec.msg),
            })
        return result


def get_logger():
    return Logger()
