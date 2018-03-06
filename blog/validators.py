from django.core.exceptions import ValidationError



def validate_justin(value):
    if not "justin" in value:
        raise ValidationError("Not Justin")
    return value