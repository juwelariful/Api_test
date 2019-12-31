from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Poll, Choice
from django.http import JsonResponse
# Create your views here.
class PollView(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        print('-----------------',kwargs)
        if request.resolver_match.url_name== 'poll_list':
            poll_list= Poll.objects.all()
            data = {"results": list(poll_list.values("question", "created_by__username", "pub_date"))}
            return JsonResponse(data)


        if request.resolver_match.url_name== 'poll_details':
            poll= get_object_or_404(Poll, id=kwargs['id'])
            data = {"results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
            }}
            return JsonResponse(data)