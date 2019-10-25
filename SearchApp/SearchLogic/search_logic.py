import sqlite3

# list = ["alpha", "maal", "taal", "alpine","alabama","markal","kalara","al"]
# list_new = sorted(list, key=lambda x: x.startswith("al"))
# print(list.sort(key= lambda x:x if "alpha" in x else "0")) #to remove unwanted entry
# print(list.sort(key=lambda x: len(x),reverse=True)) # sort in increasing length
# print(list.sort(key=lambda x: x.startswith("alpha")))
# print(list.reverse())
# print(list)


def search_word(word_to_search:str):
    """
    Search Word and return result as dictionary
    :param word_to_search: Word to Search in the Db
    :return: return dictionary
    """
    results = _get_data_from_db(word_to_search)
    return {"success": True, "message": "Match Found", "Words": results, "total_match": len(results)}


def _get_data_from_db(word_to_search: str):
    """
    Function Searches given word in db and ordered by search count in decreasing order
    :param word_to_search: Word to search in db
    :return: List of word after post processing all the constraints
    """
    try:
        query_search = "Select word from Words where word LIKE '%" + word_to_search + "%' ORDER BY word_count DESC;"
        conn = sqlite3.connect("word_search.db") # get connection for the given db
        conn.row_factory = lambda cursor, row: row[0] # change cursor to fetch result without tuples
        result = conn.execute(query_search)
        result_list = result.fetchall()
        conn.close()
        # print(type(result_list))
        # print(result_list)
        return _post_processing(result_list, word_to_search)
    except Exception as e:

        return [] # return empty list if any exception is raised


def _post_processing(data_list: list, word_to_search: str):
    """
    Function to Post Process data after it is fetched from db
    :param data_list: Searched list from the db
    :param word_to_search: Word that is to be searched
    :return: list of first 25  data based on the given constraints
    """
    data_list.sort(key=lambda x: len(x), reverse=True)  # sort smaller length words first and then  long words
    data_list.sort(key=lambda x: x.startswith(word_to_search))  # sort if the word starts with the given query
    data_list.reverse()
    return data_list[:25] # list containing first 25 results

