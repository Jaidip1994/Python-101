import functools
user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        # This is to ensure that the decorator function, is only registered and also the function doc string remains of the original function and not of the decorator function.
        @functools.wraps(func)
        def secure_function(*args,  **kwargs):
            if user["access_level"] == access_level:
                return func(*args,  **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}."
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
# print(get_password.__name__)
# help(get_password)
