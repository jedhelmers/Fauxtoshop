def key_mappings(key):
    switch = {
        # TOOLS
        '73': 'eyedropper',
        '86': 'move',
        '77': 'dashed_box',
        '76': 'polygon_lasso',
        '65': 'a_pointer',
        '85': 'rectangle',
        '66': 'brush',
        '67': 'crop',
        '0': 'eraser',
        '0': 'frame',
        '0': 'gradient',
        '0': 'pointer_finger',
        '0': 'pin',
        '80': 'pen',
        '0': 'quick_selection',
        '0': 'spot_headling',
        'S': 'stamp',
        '84': 'text',
        '0': 'rotate_view',
        '73_16777248_16777249': 'zoom',
        # MAIN FUNCTIONS
        '78_16777249': 'NEW_FILE',
        '88': 'SWAP_SWATCHES',
        '39_16777249': 'GRID',
        # WORKSPACE
        '82_16777249': 'HIDE_RULERS',
        '78_16777248_16777249': 'NEW_LAYER',
        '73_16777249': 'INVERT_IMAGE',
        '61_16777249': 'ZOOM_IN',
        '45_16777249': 'ZOOM_OUT',
        '67_16777249': 'COPY',
        '86_16777249': 'PASTE',
        '88_16777249': 'CUT',
        '90_16777249': 'UNDO',
        '90_16777248_16777249': 'REDO',
    }
    return switch[key] if key in switch else None