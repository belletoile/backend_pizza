"""Edit User

Revision ID: caecda68db57
Revises: 0baaea9a0e32
Create Date: 2023-07-07 13:03:45.119645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caecda68db57'
down_revision = '0baaea9a0e32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'middle_surname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'middle_surname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
