"""empty message

Revision ID: 22593f527ab0
Revises: f5eb0133eed7
Create Date: 2021-04-28 21:54:45.117712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22593f527ab0'
down_revision = 'f5eb0133eed7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('group', 'p_id')
    op.drop_column('group', 'group_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('group_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('group', sa.Column('p_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('group', 'id')
    # ### end Alembic commands ###
