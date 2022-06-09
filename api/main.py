from fastapi import FastAPI
from pydantic import BaseModel
from spark_utils import get_lastest_record_fail
 
# Creating FastAPI instance
app = FastAPI()
 
# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    number_record : int

# Creating an endpoint post method to receive the data
# to get request record
@app.post('/request_record')
def request_record(data : request_body):
    # Validate data
    number_record = data.number_record
    if number_record < 0:
        return {
            "code": 400,
            "message": "The number of record request must not be negative"
        }
     
    # Get lastest record with fail desc
    result = get_lastest_record_fail(number_record)
     
    # Return the result
    return { 
            "result": result,
            "code": 200
            }

# Creating an endpoint get method to receive the data
# to get request record
@app.get('/get_record/{number_record}')
def get_record(number_record:int):
    # Validate data
    if number_record < 0:
        return {
            "code": 400,
            "message": "The number of record request must not be negative"
        }
     
    # Get lastest record with fail desc
    result = get_lastest_record_fail(number_record)
     
    # Return the result
    return { 
            "result": result,
            "code": 200
            }

