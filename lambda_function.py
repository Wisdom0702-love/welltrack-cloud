
import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    try:
        data = json.loads(event.get("body") or "{}")

        name = str(data.get("name", "")).strip()
        mood = str(data.get("mood", "")).strip()
        notes = str(data.get("notes", "")).strip()

        if not name or len(name) > 40:
            return response(400, {"error": "Invalid name"})

        if mood not in ["Great", "Good", "Okay", "Low"]:
            return response(400, {"error": "Invalid mood"})

        if len(notes) > 300:
            return response(400, {"error": "Notes too long"})

        water = int(data["waterGlasses"])
        steps = int(data["steps"])
        sleep = Decimal(str(data["sleepHours"]))

        if not (0 <= water <= 30):
            raise ValueError("Invalid water intake")

        if not (0 <= steps <= 100000):
            raise ValueError("Invalid step count")

        if not (0 <= sleep <= 24):
            raise ValueError("Invalid sleep duration")

        item = {
            "checkinId": str(uuid.uuid4()),
            "name": name,
            "mood": mood,
            "notes": notes,
            "waterGlasses": water,
            "steps": steps,
            "sleepHours": sleep,
            "createdAt": datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=item)

        return response(201, {
            "message": "Check-in saved!",
            "checkinId": item["checkinId"]
        })

    except (ValueError, KeyError, TypeError, ArithmeticError):
        return response(400, {"error": "Invalid check-in data"})
    except json.JSONDecodeError:
        return response(400, {"error": "Invalid JSON"})
    except Exception:
        print("Unexpected error while saving check-in")
        return response(500, {"error": "Server error"})
