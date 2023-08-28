import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE+configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE+configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE+ configuration.PRODUCTS_KITS_PATH,
                         json = products_ids,
                         headers=data.headers)


product_kits = post_products_kits(data.product_ids)
#docs = get_docs()
#log =  get_logs()
#table = get_users_table()
#user = post_new_user()

print(product_kits.status_code)
print(product_kits.json())

