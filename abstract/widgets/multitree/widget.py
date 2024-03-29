from Products.Archetypes.Widget import TypesWidget

from AccessControl import ClassSecurityInfo

from types import ListType, StringTypes

class MultiTreeWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "multitreewidget",
        'size'  : 5,
        'helper_js': ('jquery.tokeninput.js','jquery.jstree.js'),
        'singleshot_overlay': False,
        'sources': None,
        })

    security = ClassSecurityInfo()

    security.declarePublic('process_form')
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """Basic impl for form processing in a widget"""
        value = form.get(field.getName(), empty_marker)
        if value is empty_marker:
            return empty_marker
        if emptyReturnsMarker and value == '':
            return empty_marker
        if isinstance(value, StringTypes):
            values = [v.strip() for v in value.split(',')]
        elif isinstance(value, ListType):
            values = value
        else:
            values = []
        return values, {}
