import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
# import xlwt
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Advocate'),
    (3, 'Associate'),
    (4, 'Client'),
    (5, 'SelfAdvocate'),
    (6, 'OpponentAdvocate'),
    (7, 'Others'),
    (9, "A Legal Firm or Solo Practitioner or Individual Lawyer"),
    (10, "A Real State Company or Any Authority or Similar Kind of Corporate"),
    (11, "A Financial Institution or Bank or Similar Kind of Firm")
)

CASE_STATUS_CHOICES = (
    (1, 'Running'),
    (2, 'Closed'),
    (3, 'Transferred/NOC Given'),
    (4, 'Direction Matters'),
    (5, 'Order Reserved'),
    (6, 'Sine Die')
)

ARE_YOU = ROLE_CHOICES[7:11]

PARTY_TYPE = (
    (1, "POC"),
    (2, "Opponent"),
    (3, "Opponent Advocate"),
)
YES_NO_CHOICES = (
    (0, "No"),
    (1, "YES")
)

APPEARING_AS = (
    (1, "Petitioner"),
    (1, "Respondent")
)


class CustomPaginator:
    def paginate(request, data):
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 4)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        return data


class SoftDelete:
    def delete(model, obj_id):
        model_obj = model.objects.get(id=obj_id)
        model_obj.is_delete = True
        model_obj.save()
        return True


class SoftDeleteMultiple:
    def delete_multiple(model, id_list):
        for id in id_list:
            model_obj = model.objects.get(pk=int(id))
            model_obj.deleted = True
            model_obj.save()
        return True


def is_valid_filterparam(param):
    return param != '' and param is not None


def filter_model(queryset, lookups, lookup_values):
    i = 0
    for lookup in lookups:
        if is_valid_filterparam(lookup_values[i]):
            queryset = queryset.filter(**{lookup: lookup_values[i]})
        i += 1
    return queryset.distinct()


# def export_excel(queryset, top_row, selected_fields):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="file.xls"'
#     queryset = queryset.distinct().order_by('id')
#     total_rows = len(queryset)
#     total_combination_length = len(queryset.values(*selected_fields))
#
#     y = 0
#     workbook = xlwt.Workbook(encoding='utf-8')
#     worksheet = workbook.add_sheet("Report")
#
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     for col_num in range(len(top_row)):
#         worksheet.write(y, col_num, top_row[col_num], font_style)
#
#     font_style = xlwt.XFStyle()
#     font_style.num_format_str = 'DD-MM-YYYY'
#     y += 1
#
#     backbone_index = 0
#     for i in range(1, total_rows + 1):
#         backbone_list = list(queryset.values(*selected_fields)[backbone_index].values())
#         test = queryset.values(*selected_fields)[backbone_index]
#         backbone_id = list(queryset.filter(**test).values_list('id'))[0]
#         for x in range(backbone_index + 1, total_combination_length):
#             rows = list(queryset.values(*selected_fields)[x].values())
#             test = queryset.values(*selected_fields)[x]
#             id = list(queryset.filter(**test).values_list('id'))[0]
#
#             if id == backbone_id:
#                 i = 0
#                 for value in rows:
#                     if str(value) not in str(backbone_list[i]):
#                         backbone_list[i] = str(backbone_list[i])
#                         backbone_list[i] += "," + str(value)
#                     i += 1
#             else:
#                 backbone_index = x
#                 break
#         print(backbone_list)
#
#         for index in range(len(backbone_list)):
#             worksheet.write(y, index, backbone_list[index], font_style)
#         y += 1
#     workbook.save(response)
#     return response


# def export_pdf(queryset, top_row, selected_fields):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment;filename=file.pdf'
#     queryset = queryset.distinct().order_by('id'); total_rows = len(queryset)
#     info = [top_row]
#     length = len(selected_fields)
#     total_combination_length = len(queryset.values(*selected_fields))
#
#     backbone_index = 0
#     for i in range(1, total_rows+1):
#         backbone_list = list(queryset.values(*selected_fields)[backbone_index].values())
#         for var in range(len(backbone_list)):
#             value = list(str(backbone_list[var]))
#             space_count = 1
#             for var2 in range(len(value)):
#                 if value[var2] == " ":
#                     space_count += 1
#                     if space_count % 3 == 1:
#                         value[var2] = "\n"
#             value = ''.join([item for item in value])
#             backbone_list[var] = value
#
#         test = queryset.values(*selected_fields)[backbone_index]
#         backbone_id = list(queryset.filter(**test).values_list('id'))[0]
#         for x in range(backbone_index+1, total_combination_length):
#             rows = list(queryset.values(*selected_fields)[x].values())
#             test = queryset.values(*selected_fields)[x]
#             id = list(queryset.filter(**test).values_list('id'))[0]
#
#             if id == backbone_id:
#                 ik = 0
#                 for value in rows:
#                     if isinstance(value, datetime.date):
#                         value = value.strftime('%Y-%m-%d')
#                     if value is None:
#                         value = "-"
#                     value = list(str(value))
#                     space_count = 1
#                     for ij in range(len(value)):
#                         if value[ij] == " ":
#                             space_count += 1
#                             if space_count % 3 == 1:
#                                 value[ij] = "\n"
#                     value = ''.join([item for item in value])
#
#                     if str(value) not in str(backbone_list[ik]):
#                         backbone_list[ik] = str(backbone_list[ik])
#                         backbone_list[ik] += ",\n"+str(value)
#                     ik += 1
#             else:
#                 backbone_index = x
#                 break
#
#         info.append(backbone_list)
#
#     pdf = SimpleDocTemplate(
#         response,
#         rightMargin=0, leftMargin=5, topMargin=60, bottomMargin=5,
#         pagesize=letter
#     )
#     pdf.title = "File"
#     table = Table(info)
#     table.setStyle([
#         ('FONTSIZE', (0, 0), (-1, -1), 3.2 + (0.4 * (16 - length))),
#         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#         ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
#     ])
#     elements = [table]
#     pdf.build(elements)
#     return response