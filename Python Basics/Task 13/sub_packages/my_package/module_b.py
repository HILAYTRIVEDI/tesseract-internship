from my_package import module_a


def absolute_import_greet():
    return module_a.greet()

def relative_import_greet():
    return module_a.greet()
