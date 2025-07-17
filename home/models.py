# Início do arquivo home/models.py (versão 100% corrigida)

from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import (
    CharBlock,
    TextBlock,
    RichTextBlock,
    StructBlock,
    ListBlock,
    URLBlock,
    BooleanBlock,
    PageChooserBlock
)
from wagtail.images.blocks import ImageChooserBlock

class LinkStructValue(StructBlock):
    """Estrutura para links internos ou externos."""
    link_text = CharBlock(label="Texto do Link", required=True)
    internal_page = PageChooserBlock(
        required=False,
        label="Página Interna",
        help_text="Se preenchido, o link apontará para esta página."
    )
    external_url = URLBlock(
        required=False,
        label="URL Externa",
        help_text="Use se o link for para um site externo (ex: https://google.com)."
    )

class HomePage(Page):
    body = StreamField([
        ('hero', StructBlock([
            ('main_title', TextBlock(label="Título Principal", default="Internet Fibra Óptica para Empresas")),
            ('dynamic_phrases', ListBlock(CharBlock(label="Frase"), label="Frases Dinâmicas")),
            ('subtitle', TextBlock(label="Subtítulo", default="Conectividade superior para negócios que não podem parar.")),
            ('cta_button', LinkStructValue(label="Botão de Ação (CTA)"))
        ], icon='bold', label='Seção Herói')),

        ('services', StructBlock([
            ('title', CharBlock(label="Título da Seção", default="Nossos Serviços")),
            ('items', ListBlock(
                StructBlock([
                    ('icon', CharBlock(label="Nome do Ícone", help_text="Ex: rocket-outline")),
                    ('title', CharBlock(label="Título do Serviço")),
                    ('description', TextBlock(label="Descrição")),
                ], label="Item de Serviço")
            ))
        ], icon='cogs', label='Seção de Serviços')),

        ('features', StructBlock([
            ('main_title', CharBlock(label="Título Principal", default="Mais que uma Simples Conexão")),
            ('subtitle', TextBlock(label="Subtítulo")),
            ('tabs', ListBlock(StructBlock([
                ('tab_title', CharBlock(label="Título da Aba")),
                ('content_title', CharBlock(label="Título do Conteúdo")),
                ('content_description', RichTextBlock(label="Descrição do Conteúdo")),
            ]), label="Abas de Diferenciais"))
        ], icon='star', label='Seção de Diferenciais (Abas)')),

        ('process_steps', StructBlock([
            ('title', CharBlock(label="Título da Seção", default="Da Análise à Ativação em 3 Passos")),
            ('subtitle', TextBlock(label="Subtítulo")),
            ('steps', ListBlock(StructBlock([
                ('title', CharBlock(label="Título do Passo")),
                ('description', TextBlock(label="Descrição do Passo")),
            ]), label="Passos do Processo"))
        ], icon='list-ul', label='Seção de Processo')),

        ('faq', StructBlock([
            ('title', CharBlock(label="Título", default="Perguntas Frequentes")),
            ('questions', ListBlock(StructBlock([
                ('question', CharBlock(label="Pergunta")),
                ('answer', RichTextBlock(label="Resposta")),
            ]), label="Perguntas e Respostas"))
        ], icon='help', label='Seção de FAQ')),

        ('pricing_plans', StructBlock([
            ('title', CharBlock(label="Título da Seção", default="Planos Desenhados para o Futuro")),
            ('subtitle', TextBlock(label="Subtítulo")),
            ('plans', ListBlock(StructBlock([
                ('title', CharBlock(label="Nome do Plano")),
                ('speed', CharBlock(label="Velocidade", help_text="Ex: 300")),
                ('speed_unit', CharBlock(label="Unidade", default="Mbps")),
                ('features', ListBlock(CharBlock(label="Característica"))),
                ('is_popular', BooleanBlock(label="É o mais popular?", required=False)),
                ('button_link', LinkStructValue(label="Link do Botão")),
            ]), label="Planos"))
        ], icon='tag', label='Seção de Planos')),

        ('coverage', StructBlock([
            ('title', CharBlock(label="Título da Seção", default="Atendemos em toda a região")),
            ('subtitle', TextBlock(label="Subtítulo")),
            ('map_url', URLBlock(label="URL do Google Maps Embed")),
            ('cities', ListBlock(CharBlock(label="Cidade"))),
            ('contact_phone', CharBlock(label="Telefone de Contato", help_text="Ex: (99) 91234-5678")),
        ], icon='site', label='Seção de Cobertura')),

        ('final_cta', StructBlock([
            ('title', CharBlock(label="Título", default="Dê o próximo passo...")),
            ('subtitle', TextBlock(label="Subtítulo")),
            ('button_link', LinkStructValue(label="Link do Botão")),
        ], icon='call_to_action', label='CTA Final')),

    ], use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    company_name = models.CharField(max_length=255, default="TecnoServiços")
    contact_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Selecione a página de contato para o link no menu.",
    )

    settings_panels = Page.settings_panels + [
        FieldPanel('company_name'),
        FieldPanel('contact_page'),
    ]

# Fim do arquivo home/models.py