import aiohttp



async def create_check(url:str, api_key:str, imei:str)->dict:
    headers = {'Authorization': f'Bearer {api_key}','Content-Type': 'application/json' }
    data = {"deviceId": imei,"serviceId": 12}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            # if response.status == 200:
                result = await response.json()
                print(result)
                return result





