"""empty message

Revision ID: 7b7e602e7b0d
Revises: d5df63bf429b
Create Date: 2021-05-06 16:53:27.022031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b7e602e7b0d'
down_revision = 'd5df63bf429b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.alter_column('group', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('group', 'is_superuser')
    # ### end Alembic commands ###
