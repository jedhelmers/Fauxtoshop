def main_style():
    return """
    QMainWindow {
        background-color: #383838;
    }

    QPushButton {
        padding: 10px;
        border: none;
        background-color: transparent;
        border-radius: 4px;
    }
    QPushButton::hover {
        border: 1px solid rgba(255, 255, 255, 0.2);
        background-color: #383838;
    }
    QPushButton::pressed {
        background-color: #606060;
    }

    QTabBar {
        background-color: #303030;
    }
    QTabBar::tab::selected {
        background-color: #404040;
        border: 1px solid rgba(0, 0, 0, .5);
        border-bottom: none;
    }
    QTabBar::tab {
        background-color: #303030;
        padding: 4px 20px;
        min-width: 100px;
    }
    QTabWidget::tab-bar {
        left: 0;
        bottom: 0px;
    }
    QTabWidget::pane {
        background-color: #101010;
        border: 1px solid rgba(0, 0, 0, .5);
    }

    QComboBox::selected {
        background-color: pink;
    }

    QWidget#toolOptionsWidget {
        border-bottom: 1px solid rgba(0, 0, 0, .5);
    }

    QToolTip {
        padding: 0px 2px;
        border: 1px solid rgba(255, 255, 255, .15);
        border-radius: 2px;
        background-color: black;
    }
    """