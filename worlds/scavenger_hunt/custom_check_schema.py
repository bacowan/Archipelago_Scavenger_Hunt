from schema import Schema, And, Use, Optional, SchemaError

custom_check_schema = Schema({
    str: And(
        Schema({
            Optional("found_indoors"): bool,
            Optional("found_outdoors"): bool
        }),
        lambda values: values["found_indoors"] or values["found_outdoors"] # one of these should be true
    )
})