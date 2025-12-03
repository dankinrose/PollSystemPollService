from typing import Optional, List

from repository.database import database
from model.question import Question


async def get_question_by_id(question_id: int) -> Optional[Question]:
    query = "SELECT * FROM question WHERE id = :question_id"
    row = await database.fetch_one(query=query, values={"question_id": question_id})
    return Question(**row) if row else None


async def get_all_questions() -> List[Question]:
    query = "SELECT * FROM question"
    rows = await database.fetch_all(query=query)
    return [Question(**r) for r in rows]


async def create_question(question: Question) -> int:
    query = """
    INSERT INTO question (title, option_1, option_2, option_3, option_4)
    VALUES (:title, :option_1, :option_2, :option_3, :option_4)
    """
    values = {
        "title": question.title,
        "option_1": question.option_1,
        "option_2": question.option_2,
        "option_3": question.option_3,
        "option_4": question.option_4,
    }
    last_id = await database.execute(query=query, values=values)
    return last_id


async def update_question(question: Question) -> None:
    query = """
    UPDATE question
    SET title = :title,
        option_1 = :option_1,
        option_2 = :option_2,
        option_3 = :option_3,
        option_4 = :option_4
    WHERE id = :id
    """
    values = {
        "id": question.id,
        "title": question.title,
        "option_1": question.option_1,
        "option_2": question.option_2,
        "option_3": question.option_3,
        "option_4": question.option_4,
    }
    await database.execute(query=query, values=values)


async def delete_question(question_id: int) -> None:
    query = "DELETE FROM question WHERE id = :question_id"
    await database.execute(query=query, values={"question_id": question_id})
