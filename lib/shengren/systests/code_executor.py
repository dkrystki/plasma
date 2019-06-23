"""Purpose of this file is to run code in clear environment, without any unnecessary imports etc."""


def execute(__code) -> bytearray:
    """Function where the injected code will be executed.
       Helps to avoid local variable conflicts."""
    try:
        exec(__code)
    except SyntaxError as exc:
        _results: dict = {'_exception': exc}
    else:
        _results: dict = locals()

    import pickle
    import types
    _cleared_results: dict = {}
    for key, value in _results.items():
        if isinstance(value, types.ModuleType):
            continue
        if isinstance(value, types.FunctionType):
            continue
        if isinstance(value, types.MethodType):
            continue

        _cleared_results[key] = value

    ret: bytearray = pickle.dumps(_cleared_results)

    return ret
