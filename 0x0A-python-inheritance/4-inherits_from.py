#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Determines if the object is an instance of a class or inherited (directly or indirectly)
    Args:
        obj (object): object
        a_class (class): class to compare to
    Returns:
        True if object is instance or inherited from class, False otherwise
    """
    obj_class = type(obj)
    
    # Check if the object's class is not the specified class
    if obj_class is not a_class:
        # Check if the specified class is in the object's class MRO (Method Resolution Order)
        for inherited_class in obj_class.__mro__:
            if inherited_class is a_class:
                return True
    
    return False
