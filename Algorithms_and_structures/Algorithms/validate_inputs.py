def validate_inputs(func):
    def wrapper(self, key, value=None):
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")

        if value is not None and not isinstance(value, str):
            value = str(value)
        
        return func(self, key, value)
    return wrapper
