# -*- coding: utf-8 -*-
import qrcode

data = input("请输入一个任意的数据：")
img=qrcode.make(data)
img.save("qrcode.jpg")
img.show()

input("\n\n按回车键退出！")


'''
ipa="https://fir.im/z1n5"
qr=qrcode.QRCode(version=1,
				 error_correction=qrcode.constants.ERROR_CORRECT_L,
				 box_size=8,
				 border=8,
				 )
qr.add_data(ipa)
qr.make(fit=True)
img=qr.make_image()
img.save('ios_qr_code.png')
'''