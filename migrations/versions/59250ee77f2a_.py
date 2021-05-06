"""empty message

Revision ID: 59250ee77f2a
Revises: 7b7e602e7b0d
Create Date: 2021-05-06 17:01:57.065342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59250ee77f2a'
down_revision = '7b7e602e7b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('superuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('group', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('superuser')
    # ### end Alembic commands ###
