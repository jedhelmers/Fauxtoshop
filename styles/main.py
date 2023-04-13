def main_style():
    return """
    QMainWindow {
        background-color: #383838;
    }
    QPushButton {
        padding: 10px;
        border: 1px solid #606060;
        background-color: #404040;
    }
    QPushButton::hover {
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
    }
    QTabBar::tab {
        background-color: #303030;
    }
    QTabWidget::tab-bar {
        left: 0;
        bottom: 0px;
    }
    QTabWidget::pane {
        background-color: #404040;
        border: none;
    }
    QComboBox::selected {
        background-color: pink;
    }
    """