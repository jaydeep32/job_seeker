from django.shortcuts import redirect


def allow_user(func):
    def inner(*args, **kwargs):
        request = args[0]
        if request.user.profile.is_company:
            return redirect('job:home')
        return func(*args, **kwargs)
    return inner


def allow_company(func):
    def inner(*args, **kwargs):
        request = args[0]
        if not request.user.profile.is_company:
            return redirect('job:home')
        return func(*args, **kwargs)
    return inner