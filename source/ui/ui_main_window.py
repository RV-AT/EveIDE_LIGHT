# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 637)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        icon = QIcon()
        icon.addFile(u":/pic/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionopen.setIcon(icon)
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        icon1 = QIcon()
        icon1.addFile(u":/pic/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionnew.setIcon(icon1)
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        icon2 = QIcon()
        icon2.addFile(u":/pic/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsave.setIcon(icon2)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        icon3 = QIcon()
        icon3.addFile(u":/pic/save_as.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionOpenProject = QAction(MainWindow)
        self.actionOpenProject.setObjectName(u"actionOpenProject")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.actiontest_2 = QAction(MainWindow)
        self.actiontest_2.setObjectName(u"actiontest_2")
        self.actionModules = QAction(MainWindow)
        self.actionModules.setObjectName(u"actionModules")
        self.actionModules.setCheckable(True)
        self.actionModules.setChecked(True)
        self.actionOutputs = QAction(MainWindow)
        self.actionOutputs.setObjectName(u"actionOutputs")
        self.actionOutputs.setCheckable(True)
        self.actionOutputs.setChecked(True)
        self.actionAssembly = QAction(MainWindow)
        self.actionAssembly.setObjectName(u"actionAssembly")
        self.actionNewCompile = QAction(MainWindow)
        self.actionNewCompile.setObjectName(u"actionNewCompile")
        self.actionNewSimulate = QAction(MainWindow)
        self.actionNewSimulate.setObjectName(u"actionNewSimulate")
        self.actionSelectWorkspace = QAction(MainWindow)
        self.actionSelectWorkspace.setObjectName(u"actionSelectWorkspace")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuProject = QMenu(self.menubar)
        self.menuProject.setObjectName(u"menuProject")
        self.menuNewProject = QMenu(self.menuProject)
        self.menuNewProject.setObjectName(u"menuNewProject")
        self.menuModules = QMenu(self.menubar)
        self.menuModules.setObjectName(u"menuModules")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuModules.menuAction())
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuView.addAction(self.actionModules)
        self.menuView.addAction(self.actionOutputs)
        self.menuProject.addAction(self.menuNewProject.menuAction())
        self.menuProject.addAction(self.actionSelectWorkspace)
        self.menuNewProject.addAction(self.actionNewCompile)
        self.menuNewProject.addAction(self.actionNewSimulate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionsave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"SaveAs", None))
        self.actionOpenProject.setText(QCoreApplication.translate("MainWindow", u"OpenProject", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actiontest_2.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actionModules.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.actionOutputs.setText(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.actionAssembly.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.actionNewCompile.setText(QCoreApplication.translate("MainWindow", u"Compile", None))
        self.actionNewSimulate.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.actionSelectWorkspace.setText(QCoreApplication.translate("MainWindow", u"SelectWorkspace", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuProject.setTitle(QCoreApplication.translate("MainWindow", u"Project", None))
        self.menuNewProject.setTitle(QCoreApplication.translate("MainWindow", u"NewProject", None))
        self.menuModules.setTitle(QCoreApplication.translate("MainWindow", u"Modules", None))
    # retranslateUi

