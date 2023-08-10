from django import template

register = template.Library()


@register.filter(name='user_in_groups')
def user_in_groups(user, group_ids):
    group_ids = [int(id) for id in group_ids.split(",")]
    return user.groups.filter(id__in=group_ids).exists()
