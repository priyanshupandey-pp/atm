class ATM(object):
    def __init__(self,BalanceInquiry,MoneyTransfer,CashWithdral):
        self.BalanceInquiry=BalanceInquiry
        self.MoneyTransfer=MoneyTransfer
        self.CashWithdrawl=CashWithdral
        
    def start(self):
        print(self.CashWithdrawl,"started")
        
    def stop(self):
        print(self.MoneyTransfer,"stop")
        
CashWithdrawl=ATM("Aadhar Card","ATM Card","check","State Bank India")
MoneyTransfer=ATM("Online Transavtion","Aadhar Card","State Bank India")

CashWithdrawl.start()
MoneyTransfer.stop()