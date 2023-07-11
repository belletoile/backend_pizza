"""Create СonsoleUser class

Revision ID: 96abf61bdeef
Revises: b0540639fe8f
Create Date: 2023-07-10 15:13:09.128135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96abf61bdeef'
down_revision = 'b0540639fe8f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consoleUser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('middle_surname', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('consoleUser')
    # ### end Alembic commands ###
