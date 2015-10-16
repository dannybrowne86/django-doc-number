from django.conf.urls import patterns, url

from .views import AddDocument, AddSubDocument, DeleteDocument, ViewDocument,\
    ListDocuments, EditDocument

urlpatterns = patterns('',
    url(r'^$',
        ListDocuments.as_view(),
        name='list_documents'),
    url(r'^add/$',
        AddDocument.as_view(),
        name='add_document'),
    url(r'^(?P<root>\d+)/add/$',
        AddSubDocument.as_view(),
        name='add_sub_document'),
    url(r'^(?P<document_id>\d+)/details/$',
        ViewDocument.as_view(),
        name='view_document'),
    url(r'^(?P<document_id>\d+)/edit/$',
        EditDocument.as_view(),
        name='edit_document'),
    url(r'^(?P<document_id>\d+)/delete/$',
        DeleteDocument.as_view(),
        name='delete_document'),
)
