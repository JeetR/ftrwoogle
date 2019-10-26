from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from SearchApp.SearchLogic import search_logic
from m_logger import do_logging
# Template File Names


search_page_template = 'Search.html'
result_table_template = 'Result_Table.html'
error_page_template = 'Error.html'


def index(request):
    """
    View Function to return Search page
    :param request: request object
    :return: rendered Html response
    """
    try:
        return render(request, search_page_template)
    except Exception as ex:
        do_logging(ex)
        return render(request, error_page_template, context={"message": str(ex)})


def search_words(request, q=None):
    """
    Search Words Within the db and return the list in a json response
    :param request: request from client
    :param q: word to search
    :return: Json response containing the search results or containing error information

    """

    try:
        if not q:
            return JsonResponse({"success": False, "message": "The Search parameter was not defined", "total_match": 0})
        else:
            return JsonResponse(search_logic.search_word(word_to_search=q))
    except Exception as ex:
        do_logging(ex)
        return  JsonResponse({"success": False, "message": str(ex), "total_match": 0})


def search_words_async(request, q=None):
    """
        Search Words Within the db and return the list in a Html response
        :param request: request object
        :param q: word to search
        :return: Json response containing the search results or containing error information
    """
    try:
        if not q:
            return render(request, error_page_template, context={"message": "The Search Parameter is not provided"})
        else:
            search_results = search_logic.search_word(word_to_search=q)
            return render(request, result_table_template, context={"words": search_results["Words"]})
    except Exception as ex:
        do_logging(ex)
        return render(request, error_page_template, context={"message": str(ex)})
