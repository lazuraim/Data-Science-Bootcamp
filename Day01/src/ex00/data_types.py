def data_types():
    int_var = 1
    str_var = "string"
    float_var = 1.12
    bool_var = True
    list_var = [1, 2, 3]
    dict_var = {"key" : "value", "key2" : "Value2"}
    tuple_var = (1, "dva", 3.333)
    set_var = {1, 2, 3}
    all_vars = [int_var, str_var, float_var, bool_var, list_var, dict_var, tuple_var, set_var]
    print('[', end='')
    for var in all_vars:
        if var == all_vars[-1]:
            print(type(var).__name__ + ']', end='')
        else:
            print(type(var).__name__ + ', ', end='')

if __name__ == "__main__":
    data_types()