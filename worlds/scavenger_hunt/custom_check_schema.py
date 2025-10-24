from schema import Schema, And, Use, Optional, SchemaError

custom_check_schema = Schema({
    str: {
        Optional("found_outdoors", default=True): bool
    }
})