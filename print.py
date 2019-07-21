from escpos.connections import getUSBPrinter

printer = getUSBPrinter()(idVendor=0x0416,
                          idProduct=0x5011)


printer.qr('https://drive.google.com/uc?id=1dIPgCtEDMHmJgv9TneBgDqBwhUqnK-U5')
printer.lf()
