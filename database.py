import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

async def create_user(tg_id, username):
    supabase.table("users").upsert({"tg_id": tg_id, "username": username}).execute()

async def create_deal(buyer_id, seller_id, amount, description):
    res = supabase.table("deals").insert({
        "buyer_id": buyer_id,
        "seller_id": seller_id,
        "amount": amount,
        "description": description,
        "status": "created"
    }).execute()
    return res.data[0]['id']
