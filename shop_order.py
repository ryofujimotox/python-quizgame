from chatgpt import Shop


def lambda_handler(event, context):
    body = event["body"]
    api_key = body["api_key"]
    message = body["message"]

    shop_name = body["shop_name"]
    menu = body["menu"]

    #
    xChat = XChat(api_key, shop_name, menu)
    response = xChat.talk(message)
    return response


class XChat:
    def __init__(self, api_key, shop_name, menu) -> None:
        self.Main = Shop(api_key, shop_name, menu)

    def talk(self, message) -> dict:
        try:
            response = self.Main.talk(message)
            body = {
                "ordered_numbers": response["ordered_numbers"],
                "waiter_speak": response["waiter_speak"],
            }
            return {"statusCode": 200, "body": body}

        except ValueError:
            body = {"ordered_numbers": None, "waiter_speak": ""}
            return {"statusCode": 400, "body": body}

        except TypeError:
            body = {"ordered_numbers": None, "waiter_speak": ""}
            return {"statusCode": 400, "body": body}


# {"body": {"api_key": "sk-xxxxxxx", "message": "おすすめは？", "shop_name": "BBQ restaurant 'GOLD BUTCHER'", "menu": "番号,名前,価格,おすすめかどうか\n1,上ロース,10000,false"}}


def main():
    print(
        lambda_handler(
            {
                "body": {
                    "api_key": "sk-xxxxxx",
                    "message": "おすすめは？",
                    "shop_name": "BBQ restaurant 'GOLD BUTCHER'",
                    "menu": "番号,名前,価格,おすすめかどうか\n7,G上ロース,1550,false\n6,コラー,299,false\n5,チョレギサラダ,780,false\n4,Gサラダ,680,false\n2,上カルビ,1200,false\n1,牛タン,880,true\n3,山盛り肉,2999,false",
                }
            },
            None,
        )
    )


if __name__ == "__main__":
    main()
