from django.utils import timezone
from datetime import datetime

from plagin.jalali import gregorian_to_jalali

month_names = ('فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند')


def current_jalali_data():
    date_time_now = str(datetime.now())  # Gregorian
    year, month_number, day = int(date_time_now[0:4]), int(date_time_now[5:7]), int(date_time_now[8:10])

    jalali_date_time = gregorian_to_jalali(year, month_number, day)  # Jalali date

    year_j = jalali_date_time[0]
    month_j = month_names[int(jalali_date_time[1]) - 1]
    day_j = jalali_date_time[2]
    if day_j <= 9:
        day_j = f'0{day_j}'

    return f'{day_j} {month_j} {year_j}'


def current_date():
    date_time_now = str(datetime.now())  # Gregorian
    year, month_number, day = int(date_time_now[0:4]), int(date_time_now[5:7]), int(date_time_now[8:10])

    return f'{year}-{month_number}-{day}'


def jpublish_(date):
    try:
        date = str(timezone.localtime(date))  # میلادی
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        hour, min_ = int(date[11:13]), int(date[14:16])
        if hour <= 9:
            hour = f'0{hour}'
        if min_ <= 9:
            min_ = f'0{min_}'
        jalali_date = gregorian_to_jalali(year, month, day)

        return f'{hour}:{min_} , {jalali_date[2]} {month_names[int(jalali_date[1])]} {jalali_date[0]}'

    except AttributeError:
        date = str(date)
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        jalali_date = gregorian_to_jalali(year, month, day)
        return f'{jalali_date[2]} {month_names[int(jalali_date[1])]} {jalali_date[0]}'


def publish_(date_time):
    try:
        date = str(timezone.localtime(date_time))  # میلادی
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        hour, min_ = int(date[11:13]), int(date[14:16])
        if hour <= 9:
            hour = f'0{hour}'
        if min_ <= 9:
            min_ = f'0{min_}'
        return f'{hour}:{min_} , {year} {month} {day}'

    except AttributeError:
        date = str(date_time)
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        return f'{year}/{month}/{day}'


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR')
