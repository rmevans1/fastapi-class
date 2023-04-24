from fastapi import APIRouter

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']
@router.get('/all')
def get_all_products():
    return products