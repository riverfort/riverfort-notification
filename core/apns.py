import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType

apns = APNs(
    key="auth_key/AuthKey_58M45W44RZ.p8",
    key_id="58M45W44RZ",
    team_id="A8X2W38P62",
    topic="com.RiverFort",  # Bundle ID
    use_sandbox=True,
)

payload = {
    "aps": {
        "alert": "Hello from APNs",
        "badge": "1",
    }
}


async def run(device_token):
    apns_key_client = apns
    request = NotificationRequest(
        device_token=device_token,
        message=payload,
    )
    await apns_key_client.send_notification(request)
