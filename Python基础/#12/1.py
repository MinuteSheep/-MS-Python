quan_jv_bian_liang = 555


def func():
    jv_bu_bian_liang = 666
    global quan_jv_bian_liang
    quan_jv_bian_liang = 777
    ans = quan_jv_bian_liang + jv_bu_bian_liang
    print(ans)


func()
print(quan_jv_bian_liang)
