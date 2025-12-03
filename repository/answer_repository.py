from typing import Optional, List

from repository.database import database
from model.answer import Answer


async def get_answer(user_id: int, question_id: int) -> Optional[Answer]:
    query = """
    SELECT * FROM answer
    WHERE user_id = :user_id AND question_id = :question_id
    """
    row = await database.fetch_one(query=query, values={
        "user_id": user_id,
        "question_id": question_id,
    })
    return Answer(**row) if row else None


async def get_answers_by_user(user_id: int) -> List[Answer]:
    query = """
    SELECT * FROM answer
    WHERE user_id = :user_id
    """
    rows = await database.fetch_all(query=query, values={"user_id": user_id})
    return [Answer(**r) for r in rows]


async def get_answers_by_question(question_id: int) -> List[Answer]:
    query = """
    SELECT * FROM answer
    WHERE question_id = :question_id
    """
    rows = await database.fetch_all(query=query, values={"question_id": question_id})
    return [Answer(**r) for r in rows]


async def create_answer(answer: Answer) -> int:
    query = """
    INSERT INTO answer (user_id, question_id, selected_option)
    VALUES (:user_id, :question_id, :selected_option)
    """
    values = {
        "user_id": answer.user_id,
        "question_id": answer.question_id,
        "selected_option": answer.selected_option,
    }
    last_id = await database.execute(query=query, values=values)
    return last_id


async def update_answer(answer: Answer) -> None:
    query = """
    UPDATE answer
    SET selected_option = :selected_option
    WHERE user_id = :user_id AND question_id = :question_id
    """
    values = {
        "user_id": answer.user_id,
        "question_id": answer.question_id,
        "selected_option": answer.selected_option,
    }
    await database.execute(query=query, values=values)


async def delete_answers_by_user(user_id: int) -> None:
    query = "DELETE FROM answer WHERE user_id = :user_id"
    await database.execute(query=query, values={"user_id": user_id})


async def delete_answers_by_question(question_id: int) -> None:
    query = "DELETE FROM answer WHERE question_id = :question_id"
    await database.execute(query=query, values={"question_id": question_id})
