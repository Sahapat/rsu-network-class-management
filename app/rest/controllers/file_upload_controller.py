import aiofiles
import os
import re
import random
import string
import logging

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    HTTPException,
)
from ..guards import api_key_guard

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

assignment_upload_api = APIRouter(
    prefix="/assignment-upload"
)

#####  UPLOAD FILES  #####
@assignment_upload_api.post("/assignment", dependencies=[Depends(api_key_guard)])
async def assignment_upload(file: UploadFile, student_id: str, assignment_name: str):
    if file is None or student_id.strip() == '' or assignment_name.strip() == '':
        raise HTTPException(status_code=400, detail="Invalid data")
    content = await file.read()
    filename_sp = os.path.splitext(file.filename)
    base_name = filename_sp[0]
    extension = filename_sp[1]
    letters = string.ascii_lowercase
    random_text = ''.join(random.choice(letters) for i in range(5))
    filename = f"{student_id}_{assignment_name}_{base_name}_{random_text}{extension}"
    filename = filename.replace(" ", "_")
    filepath = os.path.join('assignments', filename)
    async with aiofiles.open(filepath, 'wb') as out_file:
        await out_file.write(content)
    return "Success"

@assignment_upload_api.post("assignment/verify", dependencies=[Depends(api_key_guard)])
async def assignment_verify(student_id: str, assignment_name: str):
    files = os.listdir()
    for file in files:
        if file.startswith(f'{student_id}_{assignment_name.replace(" ", "_")}'):
            return 'Done'
    return 'Not found'
