# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hardware.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import cpuinfo
import distro
import os
from psutil import virtual_memory
from PyQt5 import QtCore, QtGui, QtWidgets
import platform
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("system information")
        Dialog.resize(1068, 759)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(160, 130, 751, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 710, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 690, 441, 41))
        self.label_2.setStyleSheet("font-size:20px;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Information"))
        self.label.setText(_translate("Dialog", "developer:benjamin"))
        self.label_2.setText(_translate("Dialog", "pycloud"))
        #a = platform.platform()+"\n"+platform.system()+"\n"+platform.architecture+"\n"+platform.processor()+"\n"+platform.machine()+"\n"+platform.node()+"\n"+platform.platform()+"\n"
        self.textBrowser.append(platform.system()+":"+platform.processor())
        a = platform.architecture()
        self.textBrowser.append(str(distro.linux_distribution()))
        self.textBrowser.append("OS Type:"+str(a))
        self.textBrowser.append("host:"+platform.node())
        self.textBrowser.append(platform.platform())
        self.textBrowser.append(platform.version())
        self.textBrowser.append("cpu count:"+str(os.cpu_count()))
        self.textBrowser.append("core i"+str(os.cpu_count()-1))
        self.textBrowser.append("ram:"+str(virtual_memory().total))
        self.textBrowser.append(f"Processor:{cpuinfo.get_cpu_info()['brand']}")
    #print('Platform architecture:', platform.architecture())
    #print(colored("Platform processor:"+platform.processor(),"green"))
    #print(colored('Machine type:'+platform.machine(),"green"))
    #print(colored('Systems network name:'+ platform.node(),"green"))
    #print(colored('Platform information:'+ platform.platform(),"green"))
    #print(colored('Platform processor:'+ platform.platform(),"green"))
    #print(colored('Operating system:'+ platform.system(),"green"))
    #print(colored('System info:'+ platform.system(),"green"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
