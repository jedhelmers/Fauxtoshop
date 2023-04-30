def window_panel_style():
    return """
    QFrame {
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 2px;
    }

    QFrame * QPushButton {
        margin-left: 0px;
    }

    QWidget#grabHandleWidget {
        margin-bottom: 2px;
    }
    """

def flyout_panel():
    return """
        QTabBar::tab {
            padding: 4px 4px;
            min-width: 80px;
        }
        QTabWidget::tab-bar {
            left: 0;
            bottom: 0px;
        }
        QLabel,
        QWidget[objectName^=layout] {
            background: transparent;
        }
        QPushButton {
            background: transparent;
            border-radius: 0px;
        }
        QPushButton::hover,
        QPushButton::pressed {
            background: rgba(0, 0, 0, .2);
        }
        """