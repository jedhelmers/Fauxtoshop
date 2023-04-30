from datatypes.window import Window

def get_windows():
    return {
            'Actions': Window(**{'tooltip': 'actions', 'name': 'Actions', 'path': u':/images/images/window_actions.svg'}),
            'Adjustments': Window(**{'tooltip': 'adjustments', 'name': 'Adjustments', 'path': u':/images/images/window_adjustments.svg'}),
            'Brush_settings': Window(**{'tooltip': 'brush settings', 'name': 'Brush Settings', 'path': u':/images/images/window_brush_settings.svg'}),
            'Brushes': Window(**{'tooltip': 'brushes', 'name': 'Brushes', 'path': u':/images/images/window_brushes.svg'}),
            'Channels': Window(**{'tooltip': 'channels', 'name': 'Channels', 'path': u':/images/images/window_channels.svg'}),
            'Characters': Window(**{'tooltip': 'characters', 'name': 'Characters', 'path': u':/images/images/window_characters.svg'}),
            'Comments': Window(**{'tooltip': 'comments', 'name': 'Comments', 'path': u':/images/images/window_comments.svg'}),
            'Gradients': Window(**{'tooltip': 'gradients', 'name': 'Gradients', 'path': u':/images/images/window_gradients.svg'}),
            'History': Window(**{'tooltip': 'history', 'name': 'History', 'path': u':/images/images/window_history.svg'}),
            'Layers': Window(**{'tooltip': 'layers', 'name': 'Layers', 'path': u':/images/images/window_layers.svg'}),
            'Libraries': Window(**{'tooltip': 'libraries', 'name': 'Libraries', 'path': u':/images/images/window_libraries.svg'}),
            'Paragraph': Window(**{'tooltip': 'paragraph', 'name': 'Paragraph', 'path': u':/images/images/window_paragraph.svg'}),
            'Paths': Window(**{'tooltip': 'paths', 'name': 'Paths', 'path': u':/images/images/window_paths.svg'}),
            'Swatches': Window(**{'tooltip': 'swatches', 'name': 'Swatches', 'path': u':/images/images/window_swatches.svg'}),
            'Patterns': Window(**{'tooltip': 'patterns', 'name': 'Patterns', 'path': u':/images/images/window_patterns.svg'}),
            'Properties': Window(**{'tooltip': 'properties', 'name': 'Properties', 'path': u':/images/images/window_properties.svg'}),
    }