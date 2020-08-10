from django.shortcuts import render

def group_list(request):
	return render(request, 'group_list.html')
