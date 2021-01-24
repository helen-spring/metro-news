import datetime
import re

MONTHS = {
        'Января': 'Jan',
        'Февраля': 'Feb',
        'Марта': 'Mar',
        'Апреля': 'Apr',
        'Мая': 'May',
        'Июня': 'Jun',
        'Июля': 'Jul',
        'Августа': 'Aug',
        'Сентября': 'Sep',
        'Октября': 'Oct',
        'Ноября': 'Nov',
        'Декабря': 'Dec'
    }


def get_date(date):
    pub_mon = date
    pub_mon = re.sub(r"\d+", '', pub_mon)
    month = MONTHS[pub_mon.strip(' ')]
    date = date.replace(pub_mon, month)
    temp = datetime.datetime.strptime(date, '%d%b%Y')
    date = temp.strftime('%Y-%m-%d')
    return date
