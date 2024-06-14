from typing import Dict


class UserRegisterSpy:
    def __init__(self) -> None:
        self.register_user = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.register_user['first_name'] = first_name
        self.register_user['last_name'] = last_name
        self.register_user['age'] = age

        return {
            "status_code":200,
            "body": {
                "type": "Users",
                "count": 1,
                "attributes": [
                    {"first_name": first_name, "last_name": last_name, "age": age}
                ]
            }
        }
