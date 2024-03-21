def copy_string(original):
    if not original:
        return ""
    else:
        return original[0] + copy_string(original[1:])


original_string = input()


copied_string = copy_string(original_string)


print("The copied string is:", copied_string)
