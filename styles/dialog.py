def dialog_styles():
    return """
    QPushButton {
        padding: 0;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, .2)
    }
    QPushButton#save {
        border: 1px solid rgba(255, 255, 255, .5)
    }
    QComboBox * QListView {
        padding: 4px;
        border-bottom: 5px solid white;
    } 
    QComboBox * QListView:selected {
        border-bottom: 5px solid black;
        margin: 3px;
        color: black;
    }                               
    QComboBox * QListView:checked {
        background-color: green;
        color: green;
    }
    QLineEdit {

    }
    QComboBox {
        background: #202020;
        padding-left: 2px;
    }
    """