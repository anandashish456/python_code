from src.api_call import *

result = call_google()
print(result.status_code)

second_result = get_input()
print(second_result)
