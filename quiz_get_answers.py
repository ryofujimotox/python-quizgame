from chatgpt import YesOrNo

# {"body": {"api_key": "sk-xxxxxx"}}


def lambda_handler(event, context):
    body = event["body"]
    api_key = body["api_key"]

    #
    xChat = XChat(api_key)

    return response


class XChat:
    Main: YesOrNo = None

    def __init__(self, api_key, answer) -> None:
        self.Main = YesOrNo(api_key, answer)

    def talk(self, message) -> dict:
        try:
            response = self.Main.talk(message)
            body = {"score": response["score"], "desc": response["description"]}
            return {"statusCode": 200, "body": body}

        except ValueError:
            body = {"score": 0, "desc": ""}
            return {"statusCode": 400, "body": body}
