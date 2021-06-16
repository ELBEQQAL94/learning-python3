global_var = True

def change_global_var():
    global global_var
    global_var = False

change_global_var()
print(global_var)