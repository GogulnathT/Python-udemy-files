result = True
another_result = result

# here both result and another_result are bound to the same bool value true
print(id(result))
print(id(another_result))

# now if change the value of result, the id will change i.e variable result is bound to
# another value now, so True is immutable, it is the variable that changes
result = False
print(id(result))

# unlike langs liek c and java, variable values are not overwritten when they are changed
# instead they are bound to a different(changed value)
