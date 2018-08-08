from django.shortcuts import render_to_response, get_object_or_404
from .models import Diary,DiaryType
from django.core.paginator import Paginator
# Create your views here.

#diary列表
def diary_list(request):
    diary_list_all = Diary.objects.all()
    paginator = Paginator(diary_list_all, 1) # Show 10 contacts per page
    page_num = request.GET.get('page',1) # 获取url的页面参数
    page_of_diarys = paginator.get_page(page_num)
    currentr_page_num = page_of_diarys.number #获取当前页码
    
    #分页-开始
    #取前两页
    currentr_page_num_min = currentr_page_num - 2
    #取后两页-range在max结束
    currentr_page_num_max = currentr_page_num + 3
    #for循环-前两页小于第一页，则后加两页（保持分页为5）
    for x in range(currentr_page_num_min ,1):
        if x < 1:
            currentr_page_num_max += 1
    #for循环-后两页大于最后一页，则前加两页（保持分页为5）
    for x in range(paginator.num_pages ,currentr_page_num_max):
        if x > paginator.num_pages:
            currentr_page_num_min -= 1
    #用列表生成式筛选出5个数做分页
    page_range = [x for x in range(currentr_page_num_min, currentr_page_num_max) if x in paginator.page_range]
    #分页-结束
    
    context = {}
    context['diarys'] = page_of_diarys.object_list
    context['page_of_diarys'] = page_of_diarys
    context['page_range'] = page_range
    context['diary_types'] = DiaryType.objects.all()
    return render_to_response('diary/diary_list.html', context)

#diary具体页面
def diary_detail(request, diary_pk):
    context = {}
    diary = get_object_or_404(Diary, pk=diary_pk)
    #上一篇-取到大于当前博客时间的博客时间
    context['previous_diary'] = Diary.objects.filter(created_time__gt = diary.created_time).last()
    #下一篇-取到小于当前博客时间的博客时间
    context['next_diary'] = Diary.objects.filter(created_time__lt = diary.created_time).first()
    context['diary'] = diary
    return render_to_response('diary/diary_detail.html', context)

def diary_with_type(request, diary_type_pk):
    context = {}
    diary_type = get_object_or_404(DiaryType, pk=diary_type_pk )
    context['diarys'] = Diary.objects.filter(diary_type=diary_type)
    context['diary_type'] = diary_type
    context['diary_types'] = DiaryType.objects.all()
    return render_to_response('diary/diary_with_type.html', context)
