from django.shortcuts import render
from .models import Group
from .forms import GroupForm


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups.html', {'groups': groups})


def new_group(request):
    form = GroupForm(request.POST)
    if form.is_valid():
        group = form.save(commit=False)
        group.save()
    return render(request, 'groups/new_group.html', {'form': form})
