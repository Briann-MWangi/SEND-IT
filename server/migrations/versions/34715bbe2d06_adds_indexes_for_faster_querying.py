"""Adds indexes for faster querying

Revision ID: 34715bbe2d06
Revises: 656c70ea3479
Create Date: 2024-08-06 15:10:27.341034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34715bbe2d06'
down_revision = '656c70ea3479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parcels', schema=None) as batch_op:
        batch_op.drop_index('idx_parcels_tracking_number')

    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.drop_index('idx_recipients_phone_number')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('idx_users_email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('idx_users_email', ['email'], unique=False)

    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.create_index('idx_recipients_phone_number', ['phone_number'], unique=False)

    with op.batch_alter_table('parcels', schema=None) as batch_op:
        batch_op.create_index('idx_parcels_tracking_number', ['tracking_number'], unique=False)

    # ### end Alembic commands ###