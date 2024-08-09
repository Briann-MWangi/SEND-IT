"""Makes association tables for user and recipient addresses

Revision ID: 41988978c8ca
Revises: 5c7d0eda6e04
Create Date: 2024-08-09 15:55:13.482996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41988978c8ca'
down_revision = '5c7d0eda6e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipient_address_association',
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['recipient_addresses.id'], name=op.f('fk_recipient_address_association_address_id_recipient_addresses')),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipients.id'], name=op.f('fk_recipient_address_association_recipient_id_recipients')),
    sa.PrimaryKeyConstraint('recipient_id', 'address_id')
    )
    op.create_table('user_address_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['user_addresses.id'], name=op.f('fk_user_address_association_address_id_user_addresses')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_address_association_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'address_id')
    )
    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.drop_constraint('fk_recipients_delivery_address_id_recipient_addresses', type_='foreignkey')
        batch_op.drop_column('delivery_address_id')

    with op.batch_alter_table('user_addresses', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_addresses_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('fk_users_user_address_id_user_addresses', type_='foreignkey')
        batch_op.drop_column('user_address_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_users_user_address_id_user_addresses', 'user_addresses', ['user_address_id'], ['id'])

    with op.batch_alter_table('user_addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_user_addresses_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('delivery_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_recipients_delivery_address_id_recipient_addresses', 'recipient_addresses', ['delivery_address_id'], ['id'])

    op.drop_table('user_address_association')
    op.drop_table('recipient_address_association')
    # ### end Alembic commands ###
