import random
import os
import ast
def save_wrongnumber(wrongnumber):
    #this function is made by chatGPT
    # 確認資料夾存在
    folder = r"刷題系統"
    os.makedirs(folder, exist_ok=True)
    
    # 檔案路徑
    file_path = os.path.join(folder, r"wrong_question_number.txt")
    
    # 將 dict 轉成字串寫入檔案
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(str("\n".join((list(wrongnumber.keys())))))
        f.write("\n")


def load_info_list(file_path):
    #this function is made by ChatGPT
    """
    讀取檔案中的 Python list
    檔案內容必須是合法的 Python list 文字，例如：
    [1, 2, 3] 或 ["a", "b", "c"]
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        print("無法讀取檔案，請確認檔案路徑是否正確")
        print("程式結束")
        exit()

    # 將字串安全地轉成 Python list 物件
    info_list = ast.literal_eval(content)

    # 檢查是否真的是 list
    if not isinstance(info_list, list):
        raise TypeError(f"檔案內容不是 list：{type(info_list)}")

    return info_list


def load_info_dict(file_path):
    #this function is made by ChatGPT
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        print("無法讀取檔案，請確認檔案路徑是否正確")
        print("程式結束")
        exit()
    
    # 安全地把字串轉成 Python 物件（dict）
    info_dict = ast.literal_eval(content)
    return info_dict
hashtable=load_info_dict(r"刷題系統\imformation.txt")


wrongnumber={}
def cheak_why_no_yellow(ob):
    print(type(ob))
    print(dir(ob))
    #this is a normal cheak , if you are pro, you can use help() and others
    #我沒有看到黃色標示,所以要寫反射檢查

"""
.write(str(hashtable))

"""
def main():
    bot=input("新開始 1 \n接續之前題目 0\n")
    if int(bot)==1:
        number=list(hashtable.keys())
        print("新開始")
    elif int(bot)==0:
        number=list((load_info_list(r"刷題系統\did_not_finish.txt")))
        print("接續之前題目")
    else:
        print("error")
        return 0
    
    while len(number)>0:
        print("\n")
        ob=random.choice(number)
        number.remove(ob)
        print(hashtable[ob][0])
        print(hashtable[ob][1])
        print("tell me the answer \n(if you wanna stop, type 'stop') \n(if you dont know the answer,type 0)")
        userinput=input()
        if userinput=="stop":
            break
        elif userinput==hashtable[ob][2]:
            print("correct")
        else:
            print("wrong")
            print("the answer is:",hashtable[ob][2])
            wrongnumber[str(ob)]=hashtable[ob]
        print("the question is  " + str(ob))
    print(list(wrongnumber.keys()))
    save_wrongnumber(wrongnumber)#this function is made by chatGPT
    print("wrong question saved in "+r"刷題系統\wrong_question_number.txt")
    with open(r"刷題系統\did_not_finish.txt","w",encoding="utf-8") as f:
        f.write(str(number))
    print("the question you did not finish saved in "+r"刷題系統\did_not_finish.txt")

def fix_question():
    #訂正錯題
    f=open(r"刷題系統\wrong_question_number.txt","r",encoding="utf-8")
    note=open(r"刷題系統\note.txt","a",encoding="utf-8")
    wrongnumber=f.readlines()
    f.close()
    f=open(r"刷題系統\wrong_question_number.txt","w",encoding="utf-8")
    index=-1
    print(wrongnumber)
    wrongnumber=[rs for rs in wrongnumber if rs!="\n"]
    print(wrongnumber)
    for rs in wrongnumber:
        index+=1
        print("題號"+rs)
        print(hashtable[int(rs)])
        bot=input("請寫下訂正(停止訂正請輸入 stop)")
        if bot=="stop":
            f.write("".join(wrongnumber[index:]))
            break
        note.write("\n".join(hashtable[int(rs)]))
        note.write("\n")
        note.write(bot)
        note.write("\n\n")
        
    f.close()
    note.close()


def test():
    pass

def trash_will_be_put_there():
    cheak_why_no_yellow(hashtable)
    print(hashtable[1001])
    todelete=[40, 83, 125, 167, 208, 250, 291, 333, 375, 418, 461, 502, 544, 587, 629, 672, 715, 759, 801, 844, 886, 929, 972, 1014, 1057, 1100, 1142, 1185, 1228, 1270, 1313, 1356, 1398, 1441, 1483, 1525, 1568, 1611, 1652, 1695, 1737, 1779, 1822, 1865, 1908, 1951, 1994, 2037, 2068]
    mainquestion=[0, 735, 904, 1612]
    #two object was from data_get.py



def if_no_bug():
    the_user_input=int(input("主程式 1 \n訂正 2 \n系統開發測試區 3\n"))
    try:
        match the_user_input:
            case 1:
                main()
            case 2:
                fix_question()
            case 3:
                test()
            case _:
                print("error")
    except:
        print("Python 3.10以上才有match功能,建議更新 python")
        if the_user_input==1:
            main()
        elif the_user_input==2:
            fix_question()
        elif the_user_input==3:
            test()
def if_possible_bug():
    the_user_input=int(input("主程式 1 \n訂正 2 \n系統開發測試區 3\n"))
    match the_user_input:
            case 1:
                main()
            case 2:
                fix_question()
            case 3:
                test()
            case _:
                print("error")
if_no_bug()