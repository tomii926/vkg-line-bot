"""empty message

Revision ID: 1482651823b9
Revises: ad77df288bf7
Create Date: 2021-04-28 20:34:58.590444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1482651823b9'
down_revision = 'ad77df288bf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cancelation', 'day_of_the_week_dummy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cancelation', sa.Column('day_of_the_week_dummy', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
