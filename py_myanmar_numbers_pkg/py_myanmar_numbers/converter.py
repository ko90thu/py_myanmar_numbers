# -*- coding: utf-8 -*-
def convert(input_numbers):
    '''
    input_numbers must be string with myanmar numbers.
    example:
        convert('၁၂၃၄၅၇')
    '''
    mm_numbers = [u'\u1040',u'\u1041',u'\u1042',u'\u1043',u'\u1044',u'\u1045',u'\u1046',u'\u1047',u'\u1048',u'\u1049']
    lst_input_numbers = list(str(input_numbers))
    result = int(''.join([str(mm_numbers.index(inn)) for inn in lst_input_numbers]))
    return result


