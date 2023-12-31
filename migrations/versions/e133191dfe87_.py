"""empty message

Revision ID: e133191dfe87
Revises: dd517aca70a3
Create Date: 2023-09-01 18:58:38.396749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e133191dfe87'
down_revision = 'dd517aca70a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['token'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('token')

    # ### end Alembic commands ###
