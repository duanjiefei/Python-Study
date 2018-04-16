def fetch():
    print('fetch')

def delete():
    print('delete')

def change():
    print('change')




if __name__ == '__main__':
    print("hello python")
    msg = '''
    1 fetch
    2 delete
    3 change
    '''
    msg_dic = {
        '1':fetch,
        '2':delete,
        '3':change,
    }
    while True:
        print(msg)
        choice = input("请输入你的选项：")
        if not choice: continue
        if choice == '4':break

        msg_dic[choice]()