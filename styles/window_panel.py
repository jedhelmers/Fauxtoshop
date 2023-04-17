def window_panel_style():
    return """
    QFrame {
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 4px;
    }

    QFrame * QPushButton {
        margin-left: 0px;
    }

    QWidget#grabHandleWidget {
        margin-bottom: 2px;
    }
    """