import inspect


class Sentry:
    def __init__(self, client):
        self.client = client

    def sentry_fun(self, fun):
        def wrapper(*args, **kwargs):
            try:
                fun(*args, **kwargs)
            except Exception:
                self.client.captureException()
                raise

        return wrapper

    def sentry_cls(self, cls):
        for name, fn in inspect.getmembers(cls, inspect.isfunction):
            if name in cls.__dict__:
                setattr(cls, name, self.sentry_fun(fn))
        return cls

    def __call__(self, obj):
        if inspect.isclass(obj):
            return self.sentry_cls(obj)
        elif inspect.isfunction(obj):
            return self.sentry_fun(obj)
        else:
            raise RuntimeError("Should be applied only to classes or functions.")
