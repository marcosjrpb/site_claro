# home/blocks.py
from wagtail.blocks import (
    CharBlock,
    RichTextBlock,
    StructBlock,
)

class ServiceCardBlock(StructBlock):
    """Bloco para um card de serviço com ícone, título e descrição."""
    
    icon_class = CharBlock(
        required=True, 
        max_length=100,
        label="Classe do Ícone (Font Awesome)",
        help_text="Ex: fas fa-briefcase, fas fa-wifi, fas fa-network-wired"
    )
    title = CharBlock(required=True, max_length=100, label="Título do Card")
    description = RichTextBlock(required=True, features=['bold', 'italic'], label="Descrição")

    class Meta:
        template = "blocks/service_card_block.html"
        icon = "form"
        label = "Card de Serviço"