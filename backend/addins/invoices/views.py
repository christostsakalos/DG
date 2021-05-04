import pdfkit
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from .serializers import InvoiceSerializer, ItemSerializer
from .models import Invoice,Item
from django.http import HttpResponse
from django.template.loader import get_template
from backend.pagination import CustomPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()





@api_view(['GET'])
def generate_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    template_name = 'pdf.html'

    template = get_template(template_name)
    html = template.render({'invoice': invoice})
    pdf = pdfkit.from_string(html, False, options={})

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response

# To rework this later
@api_view(['GET'])
def send_reminder(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    subject = 'Unpaid invoice'
    from_email = 'test@test'
    to = ['test@test.com']
    text_content = 'You have an unpaid invoice. Invoice number: #' + str(invoice.id)
    html_content = 'You have an unpaid invoice. Invoice number: #' + str(invoice.id)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    template = get_template('pdf.html')
    html = template.render({'invoice': invoice})
    pdf = pdfkit.from_string(html, False, options={})

    if pdf:
        name = 'invoice_%s.pdf' % invoice.id
        msg.attach(name, pdf, 'application/pdf')

    msg.send()

    print(msg)

    return Response()