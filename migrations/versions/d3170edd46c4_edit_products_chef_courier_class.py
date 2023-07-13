"""Edit products,chef,courier class

Revision ID: d3170edd46c4
Revises: bf9f481da341
Create Date: 2023-07-13 10:35:18.893476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3170edd46c4'
down_revision = 'bf9f481da341'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chefs', sa.Column('surname', sa.String(), nullable=True))
    op.add_column('couriers', sa.Column('surname', sa.String(), nullable=True))
    op.add_column('products', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'image')
    op.drop_column('couriers', 'surname')
    op.drop_column('chefs', 'surname')
    # ### end Alembic commands ###