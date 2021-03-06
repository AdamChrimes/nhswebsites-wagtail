from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.mixins import (
    ReviewDateMixin,
)

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CareCardBlock,
    DetailsBlock,
    DoBlock,
    DontBlock,
    ExpanderBlock,
    ExpanderGroupBlock,
    GreyPanelBlock,
    InsetTextBlock,
    ImageBlock,
    PanelBlock,
    PanelListBlock,
    WarningCalloutBlock,
    PromoBlock,
    PromoGroupBlock,
    SummaryListBlock,
)

class HomePage(ReviewDateMixin, Page):
  body = StreamField([
      ('action_link', ActionLinkBlock()),
      ('care_card', CareCardBlock()),
      ('details', DetailsBlock()),
      ('do_list', DoBlock()),
      ('dont_list', DontBlock()),
      ('expander', ExpanderBlock()),
      ('expander_group', ExpanderGroupBlock()),
      ('inset_text', InsetTextBlock()),
      ('image', ImageBlock()),
      ('panel', PanelBlock()),
      ('panel_list', PanelListBlock()),
      ('grey_panel', GreyPanelBlock()),
      ('warning_callout', WarningCalloutBlock()),
      ('summary_list', SummaryListBlock()),
  ])

  content_panels = Page.content_panels + [
      StreamFieldPanel('body'),
  ]

  settings_panels = Page.settings_panels + ReviewDateMixin.settings_panels
