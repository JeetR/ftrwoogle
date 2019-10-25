from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from SearchApp.SearchLogic import search_logic
# Create your views here.


def index(request):
    return render(request,'Search.html')


def search_words(request,q=None):
    # print(q)
    if not q:
        return HttpResponse("Hey there")
    else:
        return JsonResponse(search_logic.search_word(word_to_search=q))


def search_words_async(request,q=None):
    # print(q)
    if not q:
        return HttpResponse("Hey there")
    else:
        search_results = search_logic.search_word(word_to_search=q)
        return render(request,'Result_Table.html',context={"words":search_results["Words"]})