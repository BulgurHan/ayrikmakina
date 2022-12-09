from page.models import Notification



def nav_data(request):
    context = dict()
    if request.user.is_authenticated:
        bildirimler = Notification.objects.filter(alici = request.user).order_by("goruldu")
        context['bildirimler'] = bildirimler[0:10:1]
        badge = list()
        for i in context['bildirimler']:
            if i.goruldu==False:
                badge.append(i)
        context['badge'] = len(badge)
    return context