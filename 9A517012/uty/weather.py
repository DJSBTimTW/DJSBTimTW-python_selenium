def qrypm25(dict_temp,name):
    try:
        print("{}".format(name)+" 的 PM2.5為 "+"{}".format(dict_temp[name]))
        print("")
    except KeyError as e:
        print("查無此城市")
        print("")
