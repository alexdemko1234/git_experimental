names = ["Alex", "Daria", "Oleg", "Victoria", "Oleksandra", "Dmitro"]
ages = [19, 45, 67, 80, 43, 24]
married = [True, True, False, True, False, False]


def convertor(**data):
    """
    Треба зробити так, щоб кожен елемент списку перетворився на обʼєкт з даними з сусіднього списку.
    Список, всередині якого будуть обʼєкти з даних.

    Функція приймає довільний обʼєм даних та переконвертовує їх.

    :return: [{"name": "Alex", "age": 19, "married": True}, {"name": "Daria", "age": 45, "married": True}, ...]
    """
    # return [{"name": name, "age": age, "married": married} for name, age, married in zip(names, ages, married)]
    list_data = []
    result = {}

    for (key, value) in list_data:

        for j in value:
            result[key] = j

    list_data.append(result)

    # def convertor(**data):
    #     """
    #     Треба зробити так, щоб кожен елемент списку перетворився на обʼєкт з даними з сусіднього списку;
    #     список, всередині якого будуть обʼєкти з даних
    #
    #     :return: [{"name": "Alex", "age": 19, "married": True}, {"name": "Daria", "age": 45, "married": True}, ...]
    #     """
    #     return [{key: value} for key, value in data.items()]
    #
    # print(convertor(names))

    # list.append(result)
    # word = {
    #     'name': names[i],
    #     'age': ages[i],
    #     'married': married[i]
    # }

    # list.append(word)

    # for i in range(len(names)):
    #     word = {
    #         'name': names[i],
    #         'age': ages[i],
    #         'married': married[i]
    #     }
    #
    #     list.append(word)

    return list_data


print(convertor(name=names, married=married))
