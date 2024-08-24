import qrcode

#Takking upi id as a input
upi_id = input("Enter your UPI id :")

#Defining the payment uRL based on the UPI id
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytem_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)
paytem_qr = qrcode.make(paytem_url)
google_pay_qr = qrcode.make(google_pay_url)

#save qr code to img file 
phonepe_qr.save('phonepe_qr.png')
paytem_qr.save('paytem_qr.png')
google_pay_qr.save('google_pay_qr.png')

#show the qr code ( you can install th e qr )

phonepe_qr.show()
paytem_qr.show()
google_pay_qr.show()
