from chatgpt import Shop

# {"body": {"api_key": "sk-xxxxxx", "message": "おすすめは？"}}


def lambda_handler(event, context):
    body = event["body"]
    api_key = body["api_key"]
    message = body["message"]

    #
    xChat = XChat(api_key)
    response = xChat.talk(message)
    return response


class XChat:
    shopname = """BBQ restaurant 'GOLD BUTCHER'"""
    menu = """番号,名前,価格,おすすめかどうか
1,上ロース,10000,false
2,牛タン,5000,true
3,超柔らかい肉X,20000,true
4,コーラ,100,false
5,オレンジジュース,200,false"""

    def __init__(self, api_key) -> None:
        self.Main = Shop(api_key, self.shopname, self.menu)

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


def main():
    print(
        lambda_handler(
            {
                "body": {
                    "api_key": "sk-xxxxx",
                    "message": "おすすめは？",
                },
            },
            None,
        )
    )


if __name__ == "__main__":
    main()
