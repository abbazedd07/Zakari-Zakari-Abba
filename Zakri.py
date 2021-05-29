'''
Zakri Zakri Abbah
U19/fns/csc/1075
USSD code for Access Bank(for checking Balance)
'''
ussd_code=input("")
if(ussd_code=='*901#'):
	print("Access Bank\n1>Check Balance\n2>Airtime\n4>Other Services\n5>Access Money\n6>Diamond Xtra\n7>XtraCash Loan\n8>Mobile Wallet")
elif(ussd_code!='*901#'):
	print("Please Enter a Valid USSD code!")
option=input("")
if(option=='1'):
	print("Enter Account")
acc=input("")

print("Enter PIN to continue")

if (acc >="98888888"):
	print("Please Enter valid Account Number!")
pin=input("")
print("Your acct balance is:30000 naira!")
print("Do you want to Make another transaction?\n Choose an option below:\n0>YES\n00>END")
option3=input("")
if(option3=='0'):
		print("Access Bank\n1>Check Balance\n2>Airtime\n4>Other Services\n5>Access Money\n6>Diamond Xtra\n7>XtraCash Loan\n8>Mobile Wallet")
elif(option3=='00'):
	print("THANKS FOR BANKING WITH US!")
	
	