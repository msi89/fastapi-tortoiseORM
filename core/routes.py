from fastapi import APIRouter

api = APIRouter()


@api.get('/')
def test():
    data = []
    for n in range(10):
        data.append({
            "id": n+1,
            "name": 'item {}'.format(n+1)
        })
    return data
