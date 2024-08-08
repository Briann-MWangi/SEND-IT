"""Removes active column for testing

Revision ID: 570d47fbb704
Revises: 1c88d52782de
Create Date: 2024-08-08 14:40:08.519947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '570d47fbb704'
down_revision = '1c88d52782de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###