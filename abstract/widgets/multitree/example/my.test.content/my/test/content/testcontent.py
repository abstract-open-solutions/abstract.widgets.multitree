from Products.ATContentTypes import ATCTMessageFactory as _
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.base import registerATCT

from Products.Archetypes.atapi import Schema, LinesField, DisplayList
from zope.interface import implements

from my.test.content.interfaces import IATTestContent

from abstract.widgets.multitree.widget import MultiTreeWidget
from AccessControl import ClassSecurityInfo


ATTestContentSchema = ATContentTypeSchema.copy() + Schema((
    LinesField('myfield',
                widget=MultiTreeWidget(
                label=_(u'My Label'),
                description=_(u'My long description My long description My long description My long description '),
                singleshot_overlay=True,
                sources=[('my.vocabolary.source',_(u"Source1")),('my.vocabolary.source2',_(u"Source2"))])),
))


finalizeATCTSchema(ATTestContentSchema)

class ATTestContent(ATCTContent):

    """A page in the site. Can contain rich text."""

    schema         =  ATTestContentSchema

    meta_type = portal_type    = 'ATTestContent'
    archetype_name = 'ATTestContent'

    security       = ClassSecurityInfo()
    implements(IATTestContent)

registerATCT(ATTestContent, "TestContent")

