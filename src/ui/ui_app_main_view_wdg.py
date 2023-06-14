# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_app_main_view_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgAppMainView(object):
    def setupUi(self, WdgAppMainView):
        WdgAppMainView.setObjectName("WdgAppMainView")
        WdgAppMainView.resize(873, 634)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(WdgAppMainView)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pnlNavigation = QtWidgets.QFrame(WdgAppMainView)
        self.pnlNavigation.setStyleSheet("QLabel#lblNavigation1, QLabel#lblNavigation2, QLabel#lblNavigation3, QLabel#lblNavigation4 {\n"
"  padding: 2px;\n"
"  border: 1px solid lightgray;\n"
"  border-radius: 2px;\n"
"  background-color: lightgray;\n"
"}")
        self.pnlNavigation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pnlNavigation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnlNavigation.setObjectName("pnlNavigation")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pnlNavigation)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblNavigation1 = QtWidgets.QLabel(self.pnlNavigation)
        self.lblNavigation1.setStyleSheet("")
        self.lblNavigation1.setText("")
        self.lblNavigation1.setOpenExternalLinks(False)
        self.lblNavigation1.setObjectName("lblNavigation1")
        self.horizontalLayout.addWidget(self.lblNavigation1)
        self.lblNavigation2 = QtWidgets.QLabel(self.pnlNavigation)
        self.lblNavigation2.setStyleSheet("")
        self.lblNavigation2.setText("")
        self.lblNavigation2.setOpenExternalLinks(False)
        self.lblNavigation2.setObjectName("lblNavigation2")
        self.horizontalLayout.addWidget(self.lblNavigation2)
        self.lblNavigation3 = QtWidgets.QLabel(self.pnlNavigation)
        self.lblNavigation3.setStyleSheet("")
        self.lblNavigation3.setText("")
        self.lblNavigation3.setObjectName("lblNavigation3")
        self.horizontalLayout.addWidget(self.lblNavigation3)
        self.lblNavigation4 = QtWidgets.QLabel(self.pnlNavigation)
        self.lblNavigation4.setText("")
        self.lblNavigation4.setObjectName("lblNavigation4")
        self.horizontalLayout.addWidget(self.lblNavigation4)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnRefreshMnStatus = QtWidgets.QPushButton(self.pnlNavigation)
        self.btnRefreshMnStatus.setObjectName("btnRefreshMnStatus")
        self.horizontalLayout.addWidget(self.btnRefreshMnStatus)
        self.btnMnActions = QtWidgets.QPushButton(self.pnlNavigation)
        self.btnMnActions.setObjectName("btnMnActions")
        self.horizontalLayout.addWidget(self.btnMnActions)
        self.btnMnListColumns = QtWidgets.QPushButton(self.pnlNavigation)
        self.btnMnListColumns.setObjectName("btnMnListColumns")
        self.horizontalLayout.addWidget(self.btnMnListColumns)
        self.btnMoveMnUp = QtWidgets.QPushButton(self.pnlNavigation)
        self.btnMoveMnUp.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnMoveMnUp.setText("")
        self.btnMoveMnUp.setObjectName("btnMoveMnUp")
        self.horizontalLayout.addWidget(self.btnMoveMnUp)
        self.btnMoveMnDown = QtWidgets.QPushButton(self.pnlNavigation)
        self.btnMoveMnDown.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnMoveMnDown.setText("")
        self.btnMoveMnDown.setObjectName("btnMoveMnDown")
        self.horizontalLayout.addWidget(self.btnMoveMnDown)
        self.lblMnListMessage = QtWidgets.QLabel(self.pnlNavigation)
        self.lblMnListMessage.setText("")
        self.lblMnListMessage.setObjectName("lblMnListMessage")
        self.horizontalLayout.addWidget(self.lblMnListMessage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.pnlNavigation)
        self.frmMain = QtWidgets.QFrame(WdgAppMainView)
        self.frmMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMain.setObjectName("frmMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frmMain)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frmMain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageNetworkInfo = QtWidgets.QWidget()
        self.pageNetworkInfo.setObjectName("pageNetworkInfo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageNetworkInfo)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblNetworkInfo = QtWidgets.QLabel(self.pageNetworkInfo)
        self.lblNetworkInfo.setText("")
        self.lblNetworkInfo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblNetworkInfo.setObjectName("lblNetworkInfo")
        self.verticalLayout_5.addWidget(self.lblNetworkInfo)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.pageNetworkInfo)
        self.pageMasternodeList = QtWidgets.QWidget()
        self.pageMasternodeList.setObjectName("pageMasternodeList")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageMasternodeList)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.viewMasternodes = QtWidgets.QTableView(self.pageMasternodeList)
        self.viewMasternodes.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.viewMasternodes.setProperty("showDropIndicator", False)
        self.viewMasternodes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.viewMasternodes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.viewMasternodes.setShowGrid(False)
        self.viewMasternodes.setObjectName("viewMasternodes")
        self.viewMasternodes.verticalHeader().setVisible(False)
        self.viewMasternodes.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_4.addWidget(self.viewMasternodes)
        self.lblNoMasternodeMessage = QtWidgets.QLabel(self.pageMasternodeList)
        self.lblNoMasternodeMessage.setStyleSheet("QLabel{\n"
"  margin-top: 10px;\n"
"}")
        self.lblNoMasternodeMessage.setText("")
        self.lblNoMasternodeMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblNoMasternodeMessage.setObjectName("lblNoMasternodeMessage")
        self.verticalLayout_4.addWidget(self.lblNoMasternodeMessage)
        self.stackedWidget.addWidget(self.pageMasternodeList)
        self.pageSingleMasternode = QtWidgets.QWidget()
        self.pageSingleMasternode.setObjectName("pageSingleMasternode")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pageSingleMasternode)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frmMasternodeDetails = QtWidgets.QFrame(self.pageSingleMasternode)
        self.frmMasternodeDetails.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmMasternodeDetails.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmMasternodeDetails.setObjectName("frmMasternodeDetails")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmMasternodeDetails)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layMasternodesControl = QtWidgets.QHBoxLayout()
        self.layMasternodesControl.setContentsMargins(0, 0, 0, 0)
        self.layMasternodesControl.setSpacing(3)
        self.layMasternodesControl.setObjectName("layMasternodesControl")
        self.btnEditMn = QtWidgets.QPushButton(self.frmMasternodeDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditMn.sizePolicy().hasHeightForWidth())
        self.btnEditMn.setSizePolicy(sizePolicy)
        self.btnEditMn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnEditMn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnEditMn.setObjectName("btnEditMn")
        self.layMasternodesControl.addWidget(self.btnEditMn)
        self.btnCancelEditingMn = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnCancelEditingMn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancelEditingMn.setObjectName("btnCancelEditingMn")
        self.layMasternodesControl.addWidget(self.btnCancelEditingMn)
        self.btnApplyMnChanges = QtWidgets.QPushButton(self.frmMasternodeDetails)
        self.btnApplyMnChanges.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnApplyMnChanges.setObjectName("btnApplyMnChanges")
        self.layMasternodesControl.addWidget(self.btnApplyMnChanges)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layMasternodesControl.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.layMasternodesControl)
        spacerItem4 = QtWidgets.QSpacerItem(20, 353, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frmMasternodeDetails)
        self.stackedWidget.addWidget(self.pageSingleMasternode)
        self.pageAllMasternodes = QtWidgets.QWidget()
        self.pageAllMasternodes.setObjectName("pageAllMasternodes")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pageAllMasternodes)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblAllMasternodesInfo = QtWidgets.QLabel(self.pageAllMasternodes)
        self.lblAllMasternodesInfo.setObjectName("lblAllMasternodesInfo")
        self.verticalLayout_8.addWidget(self.lblAllMasternodesInfo)
        self.gbFilterCondType = QtWidgets.QGroupBox(self.pageAllMasternodes)
        self.gbFilterCondType.setTitle("")
        self.gbFilterCondType.setObjectName("gbFilterCondType")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.gbFilterCondType)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.rbFilterTypeAnd = QtWidgets.QRadioButton(self.gbFilterCondType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbFilterTypeAnd.sizePolicy().hasHeightForWidth())
        self.rbFilterTypeAnd.setSizePolicy(sizePolicy)
        self.rbFilterTypeAnd.setChecked(True)
        self.rbFilterTypeAnd.setObjectName("rbFilterTypeAnd")
        self.horizontalLayout_8.addWidget(self.rbFilterTypeAnd)
        self.rbFilterTypeOr = QtWidgets.QRadioButton(self.gbFilterCondType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbFilterTypeOr.sizePolicy().hasHeightForWidth())
        self.rbFilterTypeOr.setSizePolicy(sizePolicy)
        self.rbFilterTypeOr.setChecked(False)
        self.rbFilterTypeOr.setObjectName("rbFilterTypeOr")
        self.horizontalLayout_8.addWidget(self.rbFilterTypeOr)
        self.btnAllMnsApplyFilter = QtWidgets.QPushButton(self.gbFilterCondType)
        self.btnAllMnsApplyFilter.setObjectName("btnAllMnsApplyFilter")
        self.horizontalLayout_8.addWidget(self.btnAllMnsApplyFilter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_8.addWidget(self.gbFilterCondType)
        self.wdgAllMns = QtWidgets.QWidget(self.pageAllMasternodes)
        self.wdgAllMns.setObjectName("wdgAllMns")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.wdgAllMns)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.wdgAllMnsList = QtWidgets.QWidget(self.wdgAllMns)
        self.wdgAllMnsList.setObjectName("wdgAllMnsList")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.wdgAllMnsList)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frameAllMnsTop = QtWidgets.QFrame(self.wdgAllMnsList)
        self.frameAllMnsTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAllMnsTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAllMnsTop.setObjectName("frameAllMnsTop")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameAllMnsTop)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.edtAllMnsFilterPlatformNodeId = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterPlatformNodeId.setClearButtonEnabled(True)
        self.edtAllMnsFilterPlatformNodeId.setObjectName("edtAllMnsFilterPlatformNodeId")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterPlatformNodeId, 1, 5, 1, 1)
        self.edtAllMnsFilterPayee = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterPayee.setClearButtonEnabled(True)
        self.edtAllMnsFilterPayee.setObjectName("edtAllMnsFilterPayee")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterPayee, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.edtAllMnsFilterIP = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterIP.setClearButtonEnabled(True)
        self.edtAllMnsFilterIP.setObjectName("edtAllMnsFilterIP")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterIP, 3, 1, 1, 1)
        self.cboAllMnsFilterStatus = QtWidgets.QComboBox(self.frameAllMnsTop)
        self.cboAllMnsFilterStatus.setObjectName("cboAllMnsFilterStatus")
        self.cboAllMnsFilterStatus.addItem("")
        self.cboAllMnsFilterStatus.addItem("")
        self.cboAllMnsFilterStatus.addItem("")
        self.gridLayout_2.addWidget(self.cboAllMnsFilterStatus, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.edtAllMnsFilterProtx = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterProtx.setClearButtonEnabled(True)
        self.edtAllMnsFilterProtx.setObjectName("edtAllMnsFilterProtx")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterProtx, 4, 1, 1, 1)
        self.edtAllMnsFilterCollateralAddress = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterCollateralAddress.setClearButtonEnabled(True)
        self.edtAllMnsFilterCollateralAddress.setObjectName("edtAllMnsFilterCollateralAddress")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterCollateralAddress, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 4, 1, 1)
        self.cboAllMnsFilterType = QtWidgets.QComboBox(self.frameAllMnsTop)
        self.cboAllMnsFilterType.setObjectName("cboAllMnsFilterType")
        self.cboAllMnsFilterType.addItem("")
        self.cboAllMnsFilterType.addItem("")
        self.cboAllMnsFilterType.addItem("")
        self.gridLayout_2.addWidget(self.cboAllMnsFilterType, 0, 1, 1, 1)
        self.edtAllMnsFilterCollateralHash = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterCollateralHash.setClearButtonEnabled(True)
        self.edtAllMnsFilterCollateralHash.setObjectName("edtAllMnsFilterCollateralHash")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterCollateralHash, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)
        self.edtAllMnsFilterOwnerAddress = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterOwnerAddress.setClearButtonEnabled(True)
        self.edtAllMnsFilterOwnerAddress.setObjectName("edtAllMnsFilterOwnerAddress")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterOwnerAddress, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 2, 1, 1)
        self.edtAllMnsFilterVotingAddress = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterVotingAddress.setClearButtonEnabled(True)
        self.edtAllMnsFilterVotingAddress.setObjectName("edtAllMnsFilterVotingAddress")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterVotingAddress, 4, 3, 1, 1)
        self.edtAllMnsFilterOperatorPubkey = QtWidgets.QLineEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterOperatorPubkey.setObjectName("edtAllMnsFilterOperatorPubkey")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterOperatorPubkey, 3, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frameAllMnsTop)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 4, 1, 1)
        self.edtAllMnsFilterWasActiveOn = QtWidgets.QDateEdit(self.frameAllMnsTop)
        self.edtAllMnsFilterWasActiveOn.setCalendarPopup(True)
        self.edtAllMnsFilterWasActiveOn.setTimeSpec(QtCore.Qt.LocalTime)
        self.edtAllMnsFilterWasActiveOn.setObjectName("edtAllMnsFilterWasActiveOn")
        self.gridLayout_2.addWidget(self.edtAllMnsFilterWasActiveOn, 4, 5, 1, 1)
        self.chbAllMnsFilterWasActiveOn = QtWidgets.QCheckBox(self.frameAllMnsTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chbAllMnsFilterWasActiveOn.sizePolicy().hasHeightForWidth())
        self.chbAllMnsFilterWasActiveOn.setSizePolicy(sizePolicy)
        self.chbAllMnsFilterWasActiveOn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chbAllMnsFilterWasActiveOn.setObjectName("chbAllMnsFilterWasActiveOn")
        self.gridLayout_2.addWidget(self.chbAllMnsFilterWasActiveOn, 4, 4, 1, 1)
        self.verticalLayout_10.addWidget(self.frameAllMnsTop)
        self.viewAllMasternodes = QtWidgets.QTableView(self.wdgAllMnsList)
        self.viewAllMasternodes.setObjectName("viewAllMasternodes")
        self.verticalLayout_10.addWidget(self.viewAllMasternodes)
        self.widget = QtWidgets.QWidget(self.wdgAllMnsList)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10.addWidget(self.widget)
        self.verticalLayout_7.addWidget(self.wdgAllMnsList)
        self.verticalLayout_8.addWidget(self.wdgAllMns)
        self.stackedWidget.addWidget(self.pageAllMasternodes)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_6.addWidget(self.frmMain)
        self.lblMnStatusLabel = QtWidgets.QLabel(WdgAppMainView)
        self.lblMnStatusLabel.setObjectName("lblMnStatusLabel")
        self.verticalLayout_6.addWidget(self.lblMnStatusLabel)
        self.lblMnStatus = QtWidgets.QLabel(WdgAppMainView)
        self.lblMnStatus.setStyleSheet("")
        self.lblMnStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblMnStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblMnStatus.setText("")
        self.lblMnStatus.setWordWrap(False)
        self.lblMnStatus.setOpenExternalLinks(False)
        self.lblMnStatus.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblMnStatus.setObjectName("lblMnStatus")
        self.verticalLayout_6.addWidget(self.lblMnStatus)

        self.retranslateUi(WdgAppMainView)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(WdgAppMainView)
        WdgAppMainView.setTabOrder(self.btnRefreshMnStatus, self.btnMnActions)
        WdgAppMainView.setTabOrder(self.btnMnActions, self.btnMnListColumns)
        WdgAppMainView.setTabOrder(self.btnMnListColumns, self.btnMoveMnUp)
        WdgAppMainView.setTabOrder(self.btnMoveMnUp, self.btnMoveMnDown)
        WdgAppMainView.setTabOrder(self.btnMoveMnDown, self.viewMasternodes)

    def retranslateUi(self, WdgAppMainView):
        _translate = QtCore.QCoreApplication.translate
        WdgAppMainView.setWindowTitle(_translate("WdgAppMainView", "Form"))
        self.btnRefreshMnStatus.setText(_translate("WdgAppMainView", "Refresh status"))
        self.btnMnActions.setText(_translate("WdgAppMainView", "MN actions"))
        self.btnMnListColumns.setText(_translate("WdgAppMainView", "Columns..."))
        self.btnMoveMnUp.setToolTip(_translate("WdgAppMainView", "Move up the selected masternode entry"))
        self.btnMoveMnDown.setToolTip(_translate("WdgAppMainView", "Move down the selected masternode entry"))
        self.btnEditMn.setToolTip(_translate("WdgAppMainView", "Edit masternode details"))
        self.btnEditMn.setText(_translate("WdgAppMainView", "Edit"))
        self.btnCancelEditingMn.setText(_translate("WdgAppMainView", "Cancel changes"))
        self.btnApplyMnChanges.setText(_translate("WdgAppMainView", "Apply changes"))
        self.lblAllMasternodesInfo.setText(_translate("WdgAppMainView", "..."))
        self.rbFilterTypeAnd.setText(_translate("WdgAppMainView", "All conditions are met (AND)"))
        self.rbFilterTypeOr.setText(_translate("WdgAppMainView", "Any condition is met (OR)"))
        self.btnAllMnsApplyFilter.setText(_translate("WdgAppMainView", "Apply"))
        self.label.setText(_translate("WdgAppMainView", "IP/port:"))
        self.label_5.setText(_translate("WdgAppMainView", "Collateral address:"))
        self.label_3.setText(_translate("WdgAppMainView", "Type:"))
        self.label_10.setText(_translate("WdgAppMainView", "Status:"))
        self.cboAllMnsFilterStatus.setItemText(0, _translate("WdgAppMainView", "Any"))
        self.cboAllMnsFilterStatus.setItemText(1, _translate("WdgAppMainView", "ENABLED"))
        self.cboAllMnsFilterStatus.setItemText(2, _translate("WdgAppMainView", "POSE_BANNED"))
        self.label_4.setText(_translate("WdgAppMainView", "Payment address:"))
        self.label_2.setText(_translate("WdgAppMainView", "Collateral hash:"))
        self.cboAllMnsFilterType.setItemText(0, _translate("WdgAppMainView", "Any"))
        self.cboAllMnsFilterType.setItemText(1, _translate("WdgAppMainView", "Regular (1k)"))
        self.cboAllMnsFilterType.setItemText(2, _translate("WdgAppMainView", "High performance (4k)"))
        self.label_8.setText(_translate("WdgAppMainView", "Protx hash:"))
        self.label_9.setText(_translate("WdgAppMainView", "Platform Node Id:"))
        self.label_6.setText(_translate("WdgAppMainView", "Owner address:"))
        self.label_7.setText(_translate("WdgAppMainView", "Voting address:"))
        self.label_12.setText(_translate("WdgAppMainView", "Operator pubkey:"))
        self.chbAllMnsFilterWasActiveOn.setText(_translate("WdgAppMainView", "Was active in DMT on:"))
        self.lblMnStatusLabel.setText(_translate("WdgAppMainView", "Status details:"))
