import uuid


class Id:
    @staticmethod
    def generate_hash() -> str:
        return str(uuid.uuid4())
