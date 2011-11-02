
from zope.interface import Interface

from plone.registry.field import DottedName, Dict
from zope.schema import Object


class IATTestContent(Interface):
    """
    """

class ISource(Interface):

    def get_children(node_id):
        """ """

    def search(text):
        """ """

class ISources(Interface):

    sources = Dict(
        title=u'Sources',
        key_type=DottedName(),
    )


