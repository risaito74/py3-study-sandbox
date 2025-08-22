# PyQ模擬試験
# 28. 次のコードを実⾏した結果として表⽰されるエラーを選択してください（1つ選択）

# 変数の未定義：NameError
try:
    print(python_version)
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'python_version' is not defined

type_str = "nice string"

# 変数名のスペルミス：NameError
try:
    print(typo_str)
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'typo_str' is not defined

# 大文字小文字の違い：NameError
try:
    print(Type_str)
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'Type_str' is not defined

# 関数の未定義：NameError
try:
    my_function()
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'my_function' is not defined

# import文の忘れ：NameError
try:
    result = math.sqrt(16)
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'math' is not defined

# 文字列の引用符忘れ：NameError
try:
    str = hello_python
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'hello_python' is not defined

# ローカル変数のスコープ外からの参照：NameError
def function_for_local_scope():
    local_arg = "hoge"

try:
    print(local_arg)
except Exception as e:
    print("例外：", type(e), e)
# <class 'NameError'> name 'local_arg' is not defined
