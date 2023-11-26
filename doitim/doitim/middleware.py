import pytz
from django.utils import timezone

# 事先激活用户所在的时区
class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tz_name = request.COOKIES.get('timezone')
        if tz_name:
            timezone.activate(pytz.timezone(tz_name))
            print('激活了')
        else:
            pass
        return self.get_response(request)
