# gakumasu_member.py : 6章モジュールでimportするpy
# 学マス生徒のプロフィール情報を返す

def get_name(id):
    """ 学マスメンバーのidから名前を返す """
    dec_n = {1: "花海咲季", 2: "月村手毬", 3: "藤田ことね"}
    if id in dec_n:
        name = dec_n[id]
    else:
        name = None

    return name

def get_weight(id):
    """ 学マスメンバーのidから体重を返す """
    dec_a = {1: 45, 2: 51, 3: 40}
    if id in dec_a:
        weight = dec_a[id]
    else:
        weight = None
    
    return weight
