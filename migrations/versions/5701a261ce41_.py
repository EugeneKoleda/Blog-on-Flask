"""empty message

Revision ID: 5701a261ce41
Revises: 351feab38902
Create Date: 2019-05-12 01:12:49.988240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5701a261ce41'
down_revision = '351feab38902'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('user')
    op.drop_constraint('roles_users_user_id_fkey', 'roles_users', type_='foreignkey')
    op.create_foreign_key(None, 'roles_users', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles_users', type_='foreignkey')
    op.create_foreign_key('roles_users_user_id_fkey', 'roles_users', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###