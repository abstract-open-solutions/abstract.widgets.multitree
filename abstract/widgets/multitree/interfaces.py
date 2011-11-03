from zope.interface import Interface

from plone.registry.field import DottedName, Dict
from zope.schema import Object

class ISource(Interface):
    """ Interface for a source of data for the widget """

    def get_info(node_id):
        """Returns a dict who contains id, label and full_label of a node,
        identified by node_id """

    def get_children(node_id):
         """Returns a list of dictionaries representing the direct children of the
        element whose id is 'node_id'. If 'node_id' is None returns the children
        of the root.

        The result will be in the form:
        [
            { 'id': 'example_unique_id_1',
              'label': u'Item 2-1',
              'full_label': u'Item 2 ‣ Item 2-1' },
            { 'id': 'example_unique_id_2',
              'label': u'Item 2-2',
              'full_label': u'Item 2 ‣ Item 2-2' }
        ]
        """

    def search(text):
        """Returns the items whose 'full_label' contains 'text'.
        The result type is similar to that of 'get_children'.
        """


class ISources(Interface):

    sources = Dict(
        title=u'Sources',
        key_type=DottedName(),
    )
