"""offer made not null

Revision ID: cf9bdbcc21c1
Revises: f2eccb04c033
Create Date: 2023-08-07 14:08:40.312260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf9bdbcc21c1'
down_revision = 'f2eccb04c033'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prod', schema=None) as batch_op:
        batch_op.alter_column('offer',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prod', schema=None) as batch_op:
        batch_op.alter_column('offer',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###
