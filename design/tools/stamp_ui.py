# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stamp.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)
import resources_rc

class Ui_StampOptions(object):
    def setupUi(self, StampOptions):
        if not StampOptions.objectName():
            StampOptions.setObjectName(u"StampOptions")
        StampOptions.resize(873, 44)
        self.gridLayout = QGridLayout(StampOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.StampOptionsWidget = QWidget(StampOptions)
        self.StampOptionsWidget.setObjectName(u"StampOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.StampOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.StampOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(StampOptions)

        QMetaObject.connectSlotsByName(StampOptions)
    # setupUi

    def retranslateUi(self, StampOptions):
        StampOptions.setWindowTitle(QCoreApplication.translate("StampOptions", u"Form", None))
    # retranslateUi

