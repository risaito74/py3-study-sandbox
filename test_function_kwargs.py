def output_kwargs(**kwargs):
    """ キーワード引数を受け取る関数 """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

dict_args = {'a': 1, 'b': 2, 'c': 3}
output_kwargs(**dict_args)  # 辞書を展開してキーワード引数として渡す
output_kwargs(a=10, b=20)  # キーワード引数を直接指定
output_kwargs()  # 引数なしでもOK
