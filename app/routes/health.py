from fastapi import APIRouter

router = APIRouter(
    prefix ="/health",
    tags=["Health"]
)

@router.get("")
def health():
    return {
        "status":"200 OK"
    }