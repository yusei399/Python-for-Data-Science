def NULL_not_found(obj: any) -> int:
    obj_type = type(obj).__name__
    if obj_type == 'NoneType':
        print(f"Nothing: {obj} {type(obj)}")
    elif obj_type == 'float' and obj != obj:  # Check for NaN
        print(f"Cheese: {obj} {type(obj)}")
    elif obj_type == 'int' and obj == 0:
        print(f"Zero: {obj} {type(obj)}")
    elif obj_type == 'str' and len(obj) == 0:
        print(f"Empty: {type(obj)}")
    elif obj_type == 'bool' and obj is False:
        print(f"Fake: {obj} {type(obj)}")
    else:
        print("Type not Found")
        return 1
    return 0

