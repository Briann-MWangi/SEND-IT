"""New Migration

Revision ID: 877093ab0ec2
Revises: 
Create Date: 2024-08-11 19:13:45.717505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877093ab0ec2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=130), nullable=False),
    sa.Column('last_name', sa.String(length=130), nullable=False),
    sa.Column('email', sa.String(length=130), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('fs_uniquifier', sa.String(length=255), nullable=False),
    sa.Column('street', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fs_uniquifier')
    )
    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recipients_email'), ['email'], unique=True)

    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=130), nullable=False),
    sa.Column('last_name', sa.String(length=130), nullable=False),
    sa.Column('email', sa.String(length=130), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('fs_uniquifier', sa.String(length=255), nullable=False),
    sa.Column('street', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fs_uniquifier')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)

    op.create_table('billing_addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('street', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_billing_addresses_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parcels',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('length', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('width', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('height', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('weight', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('cost', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('tracking_number', sa.String(length=32), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipients.id'], name=op.f('fk_parcels_recipient_id_recipients')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_parcels_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('parcels', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parcels_tracking_number'), ['tracking_number'], unique=True)

    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_roles_users_role_id_roles')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_roles_users_user_id_users'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    with op.batch_alter_table('parcels', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_parcels_tracking_number'))

    op.drop_table('parcels')
    op.drop_table('billing_addresses')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    op.drop_table('roles')
    with op.batch_alter_table('recipients', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipients_email'))

    op.drop_table('recipients')
    # ### end Alembic commands ###