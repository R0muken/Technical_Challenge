import requests


class BoredApiWrapper:

    def __init__(self):
        self.base_url = "https://www.boredapi.com/api/activity"
        self.session = requests.Session()

    def random_activity(
            self,
            type: str = None,
            participants: int = None,
            price: float = None,
            accessibility: int = None
    ):
        params = {}
        if type:
            params["type"] = type
        if participants:
            params["participants"] = participants
        if price:
            params["price"] = price
        if accessibility:
            params["accessibility"] = accessibility

        response = self.session.get(self.base_url, params=params).json()

        return response

