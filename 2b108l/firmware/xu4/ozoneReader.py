#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD

dataFolder  = mD.dataFolder
ozonePort    = mD.ozonePort

# def changeAveragingTime(averageTimeIndex,ser):
#
#     # ser.write(str.encode('m'))
#     while(True):
#         readAndPrintSerialLine(ser)


    # for c in ser.read():
    #                     # print(chr(c))
    #     line.append(chr(c))
    #     if chr(c) == '\n':
    #     dataString     = (''.join(line)).replace("\n","").replace("\r","")
    #     dateTime  = datetime.datetime.now()
    #     print(dataString)
    #     if("," in dataString):
    #         ser.write(str.encode('m'))
    #                             # mSR.TB108LWrite(dataString,dateTime)
    #         line = []
    #     break
    #             # except:



def readAndPrintSerialLine(ser,stringFind):
    line = []
    while True:
        for c in ser.read():
            line.append(chr(c))
            # print(line)
            if chr(c) == stringFind:
                dataString     = (''.join(line))
                dateTime  = datetime.datetime.now()
                print(dataString)
                # line = []
                return dataString;


def changeAveragingTime(ser):
    readAndPrintSerialLine(ser,">")
    ser.write(str.encode('a'))
    readAndPrintSerialLine(ser,":")
    ser.write(str.encode('1'))
    readAndPrintSerialLine(ser,">")
    ser.write(str.encode('x'))               # break





def main():
    if(ozonePort[0]):

        ser = serial.Serial(
        port= ozonePort[1],\
        baudrate=2400,\
        parity  =serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)
        print("connected to: " + ser.portstr)
        # readAndPrintSerialLine(ser)
        #this will store the line

        #
        # changeAveragingTime(1,ser)







        #
        line = []
        while True:
            # print("looping")
            # try:
            # readAndPrintSerialLine(ser)
            for c in ser.read():
                    # print(chr(c))
                line.append(chr(c))
                if chr(c) == '\n':
                    dataString     = (''.join(line)).replace("\n","").replace("\r","")
                    dateTime  = datetime.datetime.now()
                    print(dataString)
                    if("," in dataString):
                        # changeAveragingTime(ser)
                        ser.write(str.encode('m'))
                        readAndPrintSerialLine(ser,">")
                        ser.write(str.encode('a'))
                        readAndPrintSerialLine(ser,":")
                        ser.write(str.encode('1'))
                        readAndPrintSerialLine(ser,">")
                        # ser.write(str.encode('a'))
                        # readAndPrintSerialLine(ser,":")
                        # ser.write(str.encode('1'))
                        # readAndPrintSerialLine(ser,">")
                        # ser.write(str.encode('x'))



                    line = []
                    break
            # except:
                # print("Incomplete String Read")
                # line = []
        #     #
        #
        #
        #
        #
        # # while True:
        # #     try:
        # #         for c in ser.read():
        # #             # print(chr(c))
        # #             line.append(chr(c))
        # #             if chr(c) == '\n':
        # #                 dataString     = (''.join(line)).replace("\n","").replace("\r","")
        # #                 dateTime  = datetime.datetime.now()
        # #                 if("," in dataString):
        # #                     mSR.TB108LWrite(dataString,dateTime)
        # #                 line = []
        # #                 break
        # #     except:
        # #         print("Incomplete String Read")
        # #         line = []
        #
        # ser.close()


if __name__ == "__main__":
   main()
