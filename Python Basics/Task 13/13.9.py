from sub_packages.my_package import module_b

print("Using Absolute Import:")
print(module_b.absolute_import_greet())

print("\nUsing Relative Import:")
print(module_b.relative_import_greet())
