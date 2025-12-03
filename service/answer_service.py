from typing import List

from fastapi import HTTPException
from starlette import status

from model.answer import Answer
from repository import answer_repository, question_repository
from api.internal_api.user_service.user_service_api import get_user_by_id


async def answer_question(answer: Answer) -> Answer:
    user = await get_user_by_id(answer.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {answer.user_id} not found"
        )
    if not user.is_registered:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User must be registered to submit answers"
        )

    question = await question_repository.get_question_by_id(answer.question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {answer.question_id} not found"
        )

    existing = await answer_repository.get_answer(
        user_id=answer.user_id,
        question_id=answer.question_id
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {answer.user_id} already answered question {answer.question_id}. "
                   f"Use the update answer endpoint instead."
        )

    new_id = await answer_repository.create_answer(answer)
    answer.id = new_id
    return answer

async def update_answer(answer: Answer) -> Answer:
    user = await get_user_by_id(answer.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {answer.user_id} not found"
        )
    if not user.is_registered:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User must be registered to update answers"
        )

    question = await question_repository.get_question_by_id(answer.question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {answer.question_id} not found"
        )

    existing = await answer_repository.get_answer(
        user_id=answer.user_id,
        question_id=answer.question_id
    )
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Answer for user {answer.user_id} and question {answer.question_id} not found"
        )

    await answer_repository.update_answer(answer)
    updated = await answer_repository.get_answer(
        user_id=answer.user_id,
        question_id=answer.question_id
    )
    return updated


async def get_answers_by_user(user_id: int) -> List[Answer]:
    return await answer_repository.get_answers_by_user(user_id)


async def get_answers_by_question(question_id: int) -> List[Answer]:
    return await answer_repository.get_answers_by_question(question_id)


async def delete_answers_by_user(user_id: int) -> None:
    await answer_repository.delete_answers_by_user(user_id)


async def delete_answers_by_question(question_id: int) -> None:
    await answer_repository.delete_answers_by_question(question_id)
