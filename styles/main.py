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
    QWidget#toolOptionsWidget {
        border-bottom: 1px solid black;
    }
    """