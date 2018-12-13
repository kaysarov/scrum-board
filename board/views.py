from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.utils import timezone
import datetime


@group_required('master', 'tester')
def tasks(request, pk):
    status1 = {}
    status2 = {}
    status3 = {}
    status4 = {}
    tasks = Task.objects.filter(sprint=pk)
    tasks_sum = 0
    for i in tasks:
        tasks_sum += 1
        if i.status == 1:
            status1[i.id] = {'title': i.title, 'form': TaskForm(instance=Task.objects.get(id=i.id)),
                             'priority': i.priority, 'description': i.description}
        if i.status == 2:
            status2[i.id] = {'title': i.title, 'form': TaskForm(instance=Task.objects.get(id=i.id)),
                             'priority': i.priority}
        if i.status == 3:
            status3[i.id] = {'title': i.title, 'form': TaskForm(instance=Task.objects.get(id=i.id)),
                             'priority': i.priority}
        if i.status == 4:
            status4[i.id] = {'title': i.title, 'form': TaskForm(instance=Task.objects.get(id=i.id)),
                             'priority': i.priority}
    # График
    n = 14
    tasks_dict = {}
    tasks_count = tasks_sum
    sprint = Sprint.objects.filter(id=pk)
    for i in sprint:
        base = i.begin
    date_list = [(base + datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, n)]
    delta = tasks_count / (n - 1)
    for i in date_list:
        tasks_dict[i] = {'plan': "{0:.2f}".format(tasks_count)}
        tasks_count -= delta
    for i in date_list:
        tasks_dict[i]['test'] = tasks_sum
        for j in tasks:
            if j.status == 4 and str(i) == str(j.done):
                tasks_sum -= 1
                tasks_dict[i]['test'] = tasks_sum
        if i == str(timezone.now().date()): break
    return render(request, 'board/tasks.html', {'status1': status1, 'status2': status2, 'status3': status3,
                                                'status4': status4, 'tasks_dict': tasks_dict, 'key': pk})


@group_required('master', 'tester')
def edit_task(request, pk, ck):
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=Task.objects.get(id=pk))
        if form.is_valid():
            task = form.save()
            task.done = timezone.now().date()
            task.save()
    return redirect(tasks, pk=ck)


@group_required('master', 'tester')
def home(request):
    sprints = Sprint.objects.all()
    return render(request, 'board/sprints.html', {'sprints': sprints})


