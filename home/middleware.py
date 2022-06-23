from base.models import IpAddressModel
from plagin.utils import get_ip


class VisitPostCounterMiddleware:
    def __init__(self, view):
        self.view = view

    def __call__(self, request):
        ip_address = None
        ip = get_ip(request)

        try:
            ip_address = IpAddressModel.objects.get(ip_address=ip)  # if get ip with not error : ip exist
        except IpAddressModel.DoesNotExist:
            ip_address = IpAddressModel(ip_address=ip)
            ip_address.save()
        finally:
            request.user.ip = ip_address
            response = self.view(request)

        return response
