from typing import List

from fastapi import APIRouter
from model.answer import Answer
from service import answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"]
)


@router.post("", response_model=Answer)
async def answer_question(answer: Answer) -> Answer:
    return await answer_service.answer_question(answer)


@router.put("/update", response_model=Answer)
async def update_answer(answer: Answer) -> Answer:
    return await answer_service.update_answer(answer)


@router.get("/user/{user_id}", response_model=List[Answer])
async def get_user_answers(user_id: int) -> List[Answer]:
    return await answer_service.get_answers_by_user(user_id)


@router.get("/question/{question_id}", response_model=List[Answer])
async def get_question_answers(question_id: int) -> List[Answer]:
    return await answer_service.get_answers_by_question(question_id)


@router.delete("/user/{user_id}")
async def delete_user_answers(user_id: int):
    await answer_service.delete_answers_by_user(user_id)
    return {"detail": f"Answers for user {user_id} deleted"}


@router.delete("/question/{question_id}")
async def delete_question_answers(question_id: int):
    await answer_service.delete_answers_by_question(question_id)
    return {"detail": f"Answers for question {question_id} deleted"}
