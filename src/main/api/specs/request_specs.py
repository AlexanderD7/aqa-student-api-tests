class RequestSpecs:
    @staticmethod
    def base_headers() -> dict:
        return {
            "Content-Type": "application/json",
            "accept": "application/json"
        }