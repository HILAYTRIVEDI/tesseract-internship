import sys
import io

# Redirect stdout to capture the output of help('modules')
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

# List all available modules
help('modules')

# Reset stdout
sys.stdout = old_stdout

# Get the captured output
modules_list = new_stdout.getvalue()

# Display the modules
print("Available Python Modules:\n")
print(modules_list)
