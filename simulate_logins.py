import asyncio
import aiohttp

async def simulate_five_logins():
    url = "http://127.0.0.1:7350/v2/account/authenticate/email"
    headers = {
        "Authorization": "Basic ZGVmYXVsdGtleTo="  # base64 of "defaultkey:"
    }
    session_tokens = []

    async with aiohttp.ClientSession() as session:
        for i in range(1, 51):
            email = f"user{i}@example.com"
            password = "password"
            username = f"user{i}"

            payload = {
                "email": email,
                "password": password,
                "create": True,
                "username": username
            }

            try:
                async with session.post(url, json=payload, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        token = data["token"]
                        print(f"[✓] Authenticated: {username}")
                        session_tokens.append(token)
                    else:
                        print(f"[!] Failed for {username} - Status: {resp.status}")
            except Exception as e:
                print(f"[!] Error for {username}: {str(e)}")

            await asyncio.sleep(1)

    print("\nAll tokens:")
    for token in session_tokens:
        print(token)

if __name__ == '__main__':
    asyncio.run(simulate_five_logins())
