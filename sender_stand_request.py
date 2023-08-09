import configuration
import requests
import data

# создаем заказ
post_creat_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                                 json=data.create_order_body,
                                 headers=data.headers)

# объект, который содержит номер отслеживания (track)
order_body = post_creat_order.json()

# выделение номера объекта в переменную
current_track_number = order_body["track"]

# получение заказа по номеру отслеживания (track)
get_order_on_number = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_ON_NUMBER_PATH
                                   + str(current_track_number))