import pandas as pd

data = None


def read_file(file):
    return pd.read_excel(file)


def get_succes_not_success_calls_count(file):

    succes_calls_count = 0
    not_succes_calls_count = 0

    for val in read_file(file)["Successful"]:
        if val == "Yes":
            succes_calls_count += 1
        else:
            not_succes_calls_count += 1
    return succes_calls_count, not_succes_calls_count


def get_min_max_time():
    df = pd.DataFrame(data['Begin time'])
    return df.min()[0], df.max()[0]


def get_min_max_conversation():
    df = pd.DataFrame(data['Conversation(ms)'])
    return df.min()[0], df.max()[0]


def get_data_each_tg(file):

    data = read_file(file)
    data_dict = dict()

    tg_list = (data['Trunk Group'].unique())
    for tg in tg_list:
        success_cals = data[(data["Trunk Group"] == tg) & (data["Successful"] == "Yes")]["Trunk Group"].count()
        not_success_cals = data[(data["Trunk Group"] == tg) & (data["Successful"] == "No")]["Trunk Group"].count()
        data_dict[tg] = {}
        data_dict[tg]['success_cals'] = success_cals
        data_dict[tg]['not_success_cals'] = not_success_cals
        print(data_dict)


    

