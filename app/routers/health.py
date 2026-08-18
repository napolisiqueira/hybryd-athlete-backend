from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Healht"])

@router.get("/")
def health_check():
    return {"status": "ok"}
    
    