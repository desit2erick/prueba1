import requests, settings, datetime
import threading, time

class LoginSAP():
    cookyRLT: str = ''

    def getCookyRLT():
        return LoginSAP.getCookyRLT
    
    def loginRLT():
        while True:
            loginRequest = requests.post(settings.SAP_URL + 'Login', verify=False, json={
                "CompanyDB": settings.SAP_RLT_USER[0], 
                "UserName": settings.SAP_RLT_USER[1], 
                "Password": settings.SAP_RLT_USER[2]
            })
            cooky = 'B1SESSION=' + \
                loginRequest.cookies['B1SESSION'] + \
                '; ROUTEID=' + loginRequest.cookies['ROUTEID']

            LoginSAP.cookyRLT = cooky
            a = datetime.datetime.now()
            time.sleep(settings.SAP_LOGIN_TIME)
            b = datetime.datetime.now()

    def loginFARINCA():
        loginRequest = requests.post(settings.SAP_URL + 'Login', verify=False, json={
            "CompanyDB": settings.SAP_RLT_USER[0], 
            "UserName": settings.SAP_RLT_USER[1], 
            "Password": settings.SAP_RLT_USER[2]
        })
        cooky = 'B1SESSION=' + \
            loginRequest.cookies['B1SESSION'] + \
            '; ROUTEID=' + loginRequest.cookies['ROUTEID']

        return cooky

    def loginThread():
        hilo = threading.Thread(target=LoginSAP.loginRLT)
        hilo.daemon = True
        hilo.start()