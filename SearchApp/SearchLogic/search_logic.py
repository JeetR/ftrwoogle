# list = ["alpha", "maal", "taal", "alpine","alabama","markal","kalara","al"]
# list_new = sorted(list, key=lambda x: x.startswith("al"))
# print(list.sort(key= lambda x:x if "alpha" in x else "0")) #to remove unwanted entry
# print(list.sort(key=lambda x: len(x),reverse=True)) # sort in increasing length
# print(list.sort(key=lambda x: x.startswith("alpha")))
# print(list.reverse())
# print(list)
import sqlite3


def search_word(word_to_search:str):
    results = _get_data_from_db(word_to_search)
    return {"success":True,"message":"Match Found", "Words":results,"total_match": len(results)}


def _get_data_from_db(word_to_search:str):
    query_search = "Select word from Words where word LIKE '%"+ word_to_search+"%' ORDER BY word_count DESC;"
    print(query_search)
    conn = sqlite3.connect("word_search.db")
    conn.row_factory = lambda cursor, row: row[0]
    result = conn.execute(query_search)
    result_list = result.fetchall()
    conn.close()
    # print(type(result_list))
    # print(result_list)
    return _post_processing(result_list)


def _post_processing(data_list:list):
    data_list.sort(key=lambda x: len(x), reverse=True)
    data_list.sort(key=lambda x: x.startswith("alpha"))
    data_list.reverse()
    return data_list[:25]

