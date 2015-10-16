from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (CreateView, DeleteView, DetailView, View, UpdateView)

from timepiece.utils.csv import CSVViewMixin
from timepiece.utils.search import SearchListView
from timepiece.utils.views import cbv_decorator

from .forms import AddDocument, DocumentSearchForm, EditDocument
from .models import Document

@cbv_decorator(permission_required('doc_number.add_document'))
class AddDocument(CreateView):
    model = Document
    form_class = AddDocument
    template_name = 'doc_number/add.html'

@cbv_decorator(permission_required('doc_number.add_document'))
class AddSubDocument(View):
    
    def get(request, *args, **kwargs):
        root = Document.objects.get(id=kwargs['root'])
        doc = root.create_sub_document()
        return HttpResponseRedirect(reverse_lazy('view_document', args=(root.id,)))

@cbv_decorator(permission_required('doc_numer.delete_document'))
class DeleteDocument(DeleteView):
    model = Document
    success_url = reverse_lazy('list_documents')
    pk_url_kwarg = 'document_id'
    template_name = 'timepiece/delete_object.html'


@cbv_decorator(permission_required('doc_number.change_document'))
class EditDocument(UpdateView):
    model = Document
    form_class = EditDocument
    pk_url_kwarg = 'document_id'
    template_name = 'doc_number/edit.html'

    def get_success_url(self):
        return reverse_lazy('view_document',
            args=(self.kwargs['document_id'],))


@cbv_decorator(permission_required('doc_number.view_document'))
class ViewDocument(DetailView):
    model = Document
    pk_url_kwarg = 'document_id'
    template_name = 'doc_number/view.html'

    def get(self, request, *args, **kwargs):
        """We only want to see the root/parent document (where serial number
        is 1), so if that is not the case, redirect.
        """
        doc = self.get_object()
        if doc.serial_number != 1:
            base_id = doc.document_id[:-3] + '001'
            base = Document.objects.get(document_id=base_id)
            return HttpResponseRedirect(reverse_lazy('view_document',
                args=(base.id,)))
        else:
            return super(ViewDocument, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewDocument, self).get_context_data(**kwargs)
        context['related_docs'] = Document.objects.filter(
            document_id__startswith=self.object.document_id[:-3]
            ).order_by('document_id')
        return context

@cbv_decorator(permission_required('doc_number.view_document'))
class ListDocuments(SearchListView, CSVViewMixin):
    model = Document
    form_class = DocumentSearchForm
    redirect_if_one_result = False
    search_fields = ['document_id__icontains']
    template_name = 'doc_number/list.html'

    def get(self, request, *args, **kwargs):
        self.export_document_list = request.GET.get('export_document_list', False)
        if self.export_document_list:
            kls = CSVViewMixin

            form_class = self.get_form_class()
            self.form = self.get_form(form_class)
            self.object_list = self.get_queryset()
            self.object_list = self.filter_results(self.form, self.object_list)

            allow_empty = self.get_allow_empty()
            if not allow_empty and len(self.object_list) == 0:
                raise Http404("No results found.")

            context = self.get_context_data(form=self.form,
                object_list=self.object_list)

            return kls.render_to_response(self, context)
        else:
            return super(ListDocuments, self).get(request, *args, **kwargs)

    def filter_form_valid(self, form, queryset):
        queryset = super(ListDocuments, self).filter_form_valid(form, queryset)
        industry = form.cleaned_data['industry']
        business = form.cleaned_data['business']
        discipline = form.cleaned_data['discipline']
        if industry:
            queryset = queryset.filter(industry=industry)
        if business:
            queryset = queryset.filter(business=business)
        if discipline:
            queryset = queryset.filter(discipline=discipline)
        return queryset

    def get_filename(self, context):
        request = self.request.GET.copy()
        search = request.get('search', '(empty)')
        return 'documents_search_{0}'.format(search)

    def convert_context_to_csv(self, context):
        """Convert the context dictionary into a CSV file."""
        content = []
        document_list = context['object_list']
        if self.export_document_list:
            headers = ['Document ID', 'Industry', 'Business', 'ATA Code',
                'Discipline', 'Part Designator', 'Serial Number']
            content.append(headers)
            for doc in document_list:
                row = [doc.document_id, doc.get_industry_display(),
                str(doc.business), str(doc.ata), doc.get_discipline_display(),
                '%04d' % doc.part_designator, '%03d' % doc.serial_number]
                content.append(row)
        return content
