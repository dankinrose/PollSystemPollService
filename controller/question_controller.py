from typing import Optional, List

from fastapi import APIRouter, HTTPException
from starlette import status

from model.question import Question
from service import question_service

router = APIRouter(
    prefix="/question",
    tags=["question"]
)

@router.get("/all", response_model=List[Question])
async def get_all_questions() -> List[Question]:
    return await question_service.get_all_questions()


@router.get("/{question_id}", response_model=Question)
async def get_question(question_id: int) -> Optional[Question]:
    question = await question_service.get_question_by_id(question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return question


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Question)
async def create_question(question: Question) -> Question:
    return await question_service.create_question(question)


@router.put("/update", response_model=Question)
async def update_question(question: Question) -> Question:
    updated = await question_service.update_question(question)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question.id} not found"
        )
    return updated


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(question_id: int):
    success = await question_service.delete_question(question_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found"
        )
    return
