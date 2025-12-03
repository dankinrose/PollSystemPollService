from typing import Optional, List

from model.question import Question
from repository import question_repository, answer_repository


async def get_question_by_id(question_id: int) -> Optional[Question]:
    return await question_repository.get_question_by_id(question_id)


async def get_all_questions() -> List[Question]:
    return await question_repository.get_all_questions()


async def create_question(question: Question) -> Question:
    new_id = await question_repository.create_question(question)
    created = await question_repository.get_question_by_id(new_id)
    return created


async def update_question(question: Question) -> Optional[Question]:
    if question.id is None:
        return None
    
    existing = await question_repository.get_question_by_id(question.id)
    if not existing:
        return None

    await question_repository.update_question(question)
    updated = await question_repository.get_question_by_id(question.id)
    return updated


async def delete_question(question_id: int) -> bool:
    existing_question = await question_repository.get_question_by_id(question_id)
    if not existing_question:
        return False

    await answer_repository.delete_answers_by_question(question_id)
    await question_repository.delete_question(question_id)
    return True
