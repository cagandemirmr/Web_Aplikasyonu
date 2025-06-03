"""phone number added

Revision ID: babbf907442b
Revises: 
Create Date: 2025-05-31 22:46:44.068548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'babbf907442b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True)) #Databasein tipi ve null kabul edip etmediğimizi belirtirim.
    pass

def downgrade() -> None:
    #op.drop_columns('users',sa.Column('phone_number',sa.String(),nullable=True))
    pass
