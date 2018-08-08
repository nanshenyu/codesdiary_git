from django.shortcuts import render_to_response, get_object_or_404
from .models import Lab,LabType

# Create your views here.

#lab列表
def lab_list(request):
    context = {}
    context['labs'] = Lab.objects.all()
    return render_to_response('lab/lab_list.html', context)

#lab具体页面
def lab_detail(request, lab_pk):
    context = {}
    context['lab'] = get_object_or_404(Lab, pk=lab_pk)
    return render_to_response('lab/lab_detail.html', context)

def lab_with_type(request, lab_type_pk):
    context = {}
    lab_type = get_object_or_404(LabType, pk=lab_type_pk )
    context['labs'] = Lab.objects.filter(lab_type=lab_type)
    context['lab_type'] = lab_type
    return render_to_response('lab/lab_with_type.html', context)