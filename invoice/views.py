from django.shortcuts import render
from django.db.models import Sum
from invoice.models import Invoice
from wkhtmltopdf.views import PDFTemplateResponse


# Create your views here.

def inv(request):
    return render(request, 'invoice.html', {})


def invoice_pdf(request):
    values = Invoice.objects.get(pk=1)
    template = 'invoice.html'
    subtotal = values.project.aggregate(Sum('paid'))['paid__sum']
    total = subtotal + subtotal * .05

    context = {
        'title': 'Hello',
        'value': values,
        'subtotal': subtotal,
        'total': total,

    }
    return PDFTemplateResponse(request=request, template=template, context=context)


def quotation_pdf(request):
    values = Invoice.objects.get(pk=1)
    template = 'quotation.html'
    subtotal = values.project.aggregate(Sum('paid'))['paid__sum']
    total = subtotal + subtotal * .05

    context = {
        'title': 'Hello',
        'value': values,
        'subtotal': subtotal,
        'total': total,

    }
    return PDFTemplateResponse(request=request, template=template, context=context)
