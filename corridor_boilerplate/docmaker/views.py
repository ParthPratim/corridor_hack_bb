from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from docmaker.models import ModelDetails
import json, jinja2, pdfkit, os , pypdf
from django.http import HttpResponse
from PIL import Image
from django.utils.encoding import smart_str
from charts.confusion_matrix import ConfusionMatrix
from charts.auc_roc import AUC_ROC_Score

class ModelDocGenerator(viewsets.ViewSet):

    @action(detail=False , methods=['post'])
    def generate(self, request):
        
        csv_file = request.FILES.get('file')
        

        if csv_file == None:
            return JsonResponse({
                "status" : "ERR",
                "msg" : "Error uploading the file"
            })
        
        

        model_details = ModelDetails(devname = request.data["devname"],
                                     modelname = request.data["modelname"],
                                     overview = request.data["overview"], 
                                     reason = request.data["content"])

        model_details.save()
        

        csv_data = None

        plots = [
            ConfusionMatrix,
            AUC_ROC_Score
        ]

        
            
        template_loader = jinja2.FileSystemLoader(searchpath="./templates")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = "letter_doc.html"
        template = template_env.get_template(template_file)

        
        output_text = template.render(
            dev_name = request.data["devname"],
            model_name = request.data["modelname"],
            overview  = request.data["overview"] , 
            reason = request.data["content"])
        
        
        options = {
            'page-size': 'Letter',
            'margin-top': '0.35in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': "",
        }

        pdf_file =  "./temp/%s_html.pdf" % (model_details.doc_id)

        final_file = "./temp/%s_report.pdf" % (model_details.doc_id)

        pdfs = [
            pdf_file,            
        ]

        with csv_file.open() as file:
            for cplot in plots:
                pdfs.append(cplot(file,model_details.doc_id).generate())

        
        pdfkit.from_string(output_text, pdf_file , options = options)

        merger = pypdf.PdfMerger()

        for f in pdfs: 
            pdfFile = open(f, 'rb')
            pdfReader = pypdf.PdfReader(pdfFile)
            merger.append(pdfReader)
            pdfFile.close()
        
        
        merger.write(final_file) 

        fl = open(final_file,'rb')

        response = HttpResponse( fl.read() ,content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(final_file)

        return response
    
    