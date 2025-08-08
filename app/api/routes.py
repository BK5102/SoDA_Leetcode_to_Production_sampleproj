## All route definitions and endpoints

## import request and response pydantic models that ensure input/output validation
## create database session, SQLModel table with input/output submissions and record time of API calls

from fastapi import APIRouter
from app.schema_setup.pydantic_schema import InputModel, OutputModel ## Pydantic models
from app.db_session_setup.session import get_session ## database interaction
from app.sqlmodel_setup.sqlmodel_submission import Submission

from app.core_functions.leetcode_problem import twoSum

from sqlmodel import Session
from datetime import datetime ## records the time of API calls
 

router = APIRouter() 

@router.post("/problem", response_model=OutputModel)
def problem_endpoint(problem: InputModel, session: Session = get_session):
    print(problem)
