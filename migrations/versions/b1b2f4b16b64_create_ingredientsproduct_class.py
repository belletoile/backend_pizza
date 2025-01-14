"""create IngredientsProduct class

Revision ID: b1b2f4b16b64
Revises: a63f302893fe
Create Date: 2023-07-07 11:50:09.600417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1b2f4b16b64'
down_revision = 'a63f302893fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredientsProduct',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=True),
    sa.Column('id_ingredient', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ingredient'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredientsProduct')
    # ### end Alembic commands ###
