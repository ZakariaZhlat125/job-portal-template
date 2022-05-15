from urllib import request
from django.core.exceptions import PermissionDenied


def is_user(function):

    def warp(request, *args, **kwargs):
        if request.user.role == 'user':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return warp


def is_company(function):

    def warp(request, *args, **kwargs):
        if request.user.role == 'company':
            return function(request, **args, **kwargs)
        else:
            raise PermissionDenied
    return warp
