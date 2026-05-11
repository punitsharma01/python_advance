from pydantic import BaseModel
from typing import Optional, List


class Comment(BaseModel):
    user_id: int
    comment: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    user_id=1,
    comment="First comment",
    replies=[
        Comment(user_id=2, comment="Second comment"),
        Comment(user_id=3, comment="Third comment"),
        # replies also can be nested like below
        Comment(user_id=4, comment="Fourth comment", replies=[
            Comment(user_id=5, comment="Reply on fourth comment")
        ]),
    ]
)
print(comment)