# Format string with str.format() function
title = "General"
name = "Kenobi"
print("Hello there, {} {}".format(title, name))

# Format using variable names
title = "General"
name = "Kenobi"
print("Hello there, {name} {title}".format(name=name, title=title))

# Format using variable order
title = "General"
name = "Kenobi"
print("Hello there, {1} {0}".format(title, name))

# Format using the f-string approach
title = "General"
name = "Kenobi"
print(f"Hello there, {title} {name}")