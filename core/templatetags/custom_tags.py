from django import template
from core.models import Notification
from authentication.models import Account
import readtime


register = template.Library()


@register.inclusion_tag('partials/show_notifications.html', takes_context=True)
def show_notifications(context):
	request_user = Account.objects.get(id=context['request'].session['user_id'])
	notifications = Notification.objects.filter(
		to_user=request_user).exclude(user_has_seen=True).order_by('-timestamp')
	return {'notifications': notifications}

@register.filter('readtime')
def read(html):
    return readtime.of_html(html)