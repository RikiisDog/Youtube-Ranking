from django.conf import settings
from django.http import HttpResponseForbidden

class AdminProtect:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        url = request.get_full_path()
        print(url)

        #DEBUGがFalseであり、管理サイトに対するアクセスである
        if settings.ADMIN_PATH in url and not settings.DEBUG == False:

            #送信元のIPアドレスを手に入れる
            ip_list = request.META.get('HTTP_X_FORWARDED_FOR')
            print(ip_list)
            if ip_list:
                ip = ip_list.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            #送信元IPが許可IPアドレスリストに含まれていない場合はForbiddenを返す。
            if ip not in settings.ALLOWED_ADMIN:
                return HttpResponseForbidden()

        response = self.get_response(request)
        print(response)

        return response