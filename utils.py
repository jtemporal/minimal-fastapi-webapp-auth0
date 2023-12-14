import json


def to_pretty_json(obj: dict) -> str:
    """
    Filters for Jinja2 templates to print JSON in a pretty way
    """
    return json.dumps(obj, default=lambda o: dict(o), indent=4)
