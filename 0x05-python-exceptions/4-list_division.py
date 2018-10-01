#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    q_list = []
    quote = 0
    for num in range(list_length):
        try:
            quote = my_list_1[num] / my_list_2[num]
        except TypeError:
            quote = 0
            print('wrong type')
        except ZeroDivisionError:
            quote = 0
            print('division by 0')
        except IndexError:
            quote = 0
            print('out of range')
        finally:
                q_list.append(quote)
    return q_list
