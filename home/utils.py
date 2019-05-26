from datetime import date, datetime

def get_filename(filename):
    return filename.upper()

@property
def is_today(self):
    return self.date() == datetime.today().date()