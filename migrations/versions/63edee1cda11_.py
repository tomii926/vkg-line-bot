"""empty message

Revision ID: 63edee1cda11
Revises: 22593f527ab0
Create Date: 2021-04-28 21:58:00.597616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63edee1cda11'
down_revision = '22593f527ab0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group')
    # ### end Alembic commands ###