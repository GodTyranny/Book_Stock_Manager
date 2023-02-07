#MY PERSONAL UTILITY CODE


#Integer clamp method that return clamped value
def method_clamp(int_min : int, int_max : int, int_value : int) -> int:
    if int_value > int_max:
        return int_max
    elif int_value < int_min:
        return int_min

#If integer have been clamp return True
def method_clamp_Bool(int_min : int, int_max : int, int_value : int) -> bool:
    if int_value > int_max:
        return True
    elif int_value < int_min:
        return True
    else:
        return False

#Return the list of string insert spaced by chosen amount with chosen character to be clear for reading, you can insert even ending character
def method_textAlignmentCorrector(local_list_string : "list[str]", local_int_increaser : int = 5, local_string_spacing : str = " ",
 local_bool_ending : bool = False, local_string_ending : str = ":") -> "list[str]":

    #Create a copy of the list sended as reference to prevent the change of the original list
    #That may be not desired in every case
    local_list_string = local_list_string[:]
    local_int_lenght = 0

    #Look for the longest string and its index inside the list
    for i in range(len(local_list_string)):
        if local_int_lenght < len(local_list_string[i]):
            local_int_lenght = len(local_list_string[i])

    for i in range(len(local_list_string)):
        if local_bool_ending:
            local_list_string[i] += (local_string_spacing * (local_int_lenght - len(local_list_string[i]) + local_int_increaser - 1)) + local_string_ending
        else:
            local_list_string[i] += local_string_spacing * (local_int_lenght - len(local_list_string[i]) + local_int_increaser)            
    return local_list_string


#Class contined printing colour and mode
class Class_TextMod():
    reset = "\033[0m"
    blue = "\033[94m"
    cyan = "\033[96m"
    darkcyan = "\033[36m"
    green = "\033[92m"
    yellow = "\033[93m"
    lightred = "\033[91m"
    pink = "\033[95m"
    bold = "\033[1m"
    underline = "\033[4m"
