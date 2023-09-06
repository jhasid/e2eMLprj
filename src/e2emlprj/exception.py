import sys
from src.e2emlprj.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,err_msg,err_details:sys):
        super().__init__(err_msg)
        self.err_msg=error_message_detail(err_msg,err_details)

    def __str__(self):
        return self.err_msg    