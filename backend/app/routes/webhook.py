"""
Bharat Sahayak AI
Webhook Router
"""

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"],
)


@router.post("/payment")
async def payment_webhook(request: Request):
    payload = await request.json()
    return {
        "status": "received",
        "type": "payment",
        "payload": payload,
    }


@router.post("/notification")
async def notification_webhook(request: Request):
    payload = await request.json()
    return {
        "status": "received",
        "type": "notification",
        "payload": payload,
    }
