import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType


async def run(device_token):
    apns_key_client = APNs(
        key="auth_key/AuthKey_58M45W44RZ.p8",
        key_id="58M45W44RZ",
        team_id="A8X2W38P62",
        topic="com.RiverFort",  # Bundle ID
        use_sandbox=True,
    )
    request = NotificationRequest(
        device_token=device_token,
        message={
            "aps": {
                "alert": "Hello from APNs",
                "badge": "1",
            }
        },
    )
    await apns_key_client.send_notification(request)
