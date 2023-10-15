"""two column uniqueness

Revision ID: 8d24f38d84ed
Revises: cf9bdbcc21c1
Create Date: 2023-08-12 11:49:09.125781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d24f38d84ed'
down_revision = 'cf9bdbcc21c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('_uname_role_uc', ['uname', 'role'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('_uname_role_uc', type_='unique')

    # ### end Alembic commands ###