import gmailImap
import threading

"""function that calls the gmailImap.emailcall function every 
    five minutes, and returns a string that it was checked """
def checkEmail():
    threading.Timer(300.0,checkEmail).start()
    gmailImap.emailCall()
    print('email checked')

"""main function"""
if __name__ == '__main__':
    checkEmail()

