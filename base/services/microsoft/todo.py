import requests
import asyncio
import time

from dateutil import parser
from ...utils import format_time


def MicrosoftTodoService(access_token, social_google_token):
   messages = []
   
   async def fetch_microsoft_todos():
      start_time = time.time()
      
      response = requests.get('https://outlook.office.com/api/v2.0/me/tasks/myday', headers = {
          'Authorization': 'Bearer ' + access_token
        })
            
      if response.status_code == 200:  
        print(response.content)       
        # emails = response.json().get('messages', [])

        # for email in emails:
            
                        
        elapsed_time = time.time() - start_time                  
        print(f'Google Email loaded successfully ✅ - {format_time(elapsed_time)}')
        time.sleep(1)
         
      elif response.status_code == 401 or response.status_code == 403:
         raise Exception(f"Error {response.status_code}: Unauthorized or Forbidden")
         
   try:
      asyncio.run(fetch_microsoft_todos())
   except Exception as e:
      print(f"An error occurred: {str(e)}")
      return ['error', str(e)]
   
   return ['success', messages]       
   
