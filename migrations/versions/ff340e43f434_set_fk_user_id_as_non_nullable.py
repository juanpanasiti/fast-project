"""Set fk user_id as non nullable

Revision ID: ff340e43f434
Revises: 205ad1ef163b
Create Date: 2024-11-05 20:21:39.305625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff340e43f434'
down_revision: Union[str, None] = '205ad1ef163b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projects', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projects', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
