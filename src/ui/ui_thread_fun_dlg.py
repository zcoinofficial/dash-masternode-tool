# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_thread_fun_dlg.ui
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThreadFunDlg(object):
    def setupUi(self, ThreadFunDlg):
        ThreadFunDlg.setObjectName("ThreadFunDlg")
        ThreadFunDlg.setWindowModality(QtCore.Qt.NonModal)
        ThreadFunDlg.resize(391, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ThreadFunDlg.sizePolicy().hasHeightForWidth())
        ThreadFunDlg.setSizePolicy(sizePolicy)
        ThreadFunDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ThreadFunDlg)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblText = QtWidgets.QLabel(ThreadFunDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblText.sizePolicy().hasHeightForWidth())
        self.lblText.setSizePolicy(sizePolicy)
        self.lblText.setText("")
        self.lblText.setWordWrap(False)
        self.lblText.setOpenExternalLinks(True)
        self.lblText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblText.setObjectName("lblText")
        self.verticalLayout.addWidget(self.lblText)
        self.progressBar = QtWidgets.QProgressBar(ThreadFunDlg)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.btnBox = QtWidgets.QDialogButtonBox(ThreadFunDlg)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setCenterButtons(False)
        self.btnBox.setObjectName("btnBox")
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ThreadFunDlg)
        self.btnBox.accepted.connect(ThreadFunDlg.accept)
        self.btnBox.rejected.connect(ThreadFunDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ThreadFunDlg)

    def retranslateUi(self, ThreadFunDlg):
        _translate = QtCore.QCoreApplication.translate
        ThreadFunDlg.setWindowTitle(_translate("ThreadFunDlg", "Dialog"))
