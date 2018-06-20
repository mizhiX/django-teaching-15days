
from flask import session, redirect, url_for

from functools import wraps


def is_login(view_func):
    """
    装饰器用于登录验证
    session['user_id']
    """
    @wraps(view_func)
    def check_login(*args, **kwargs):
        # 验证登录
        if 'user_id' in session:
            return view_func(*args, **kwargs)
        else:
            # 验证失败
            return redirect(url_for('user.login'))
    return check_login





