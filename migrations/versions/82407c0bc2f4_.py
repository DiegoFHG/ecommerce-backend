"""empty message

Revision ID: 82407c0bc2f4
Revises: e133191dfe87
Create Date: 2023-09-02 19:39:40.617553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82407c0bc2f4'
down_revision = 'e133191dfe87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status_id', sa.BigInteger(), nullable=True))
        batch_op.drop_constraint('orders_status_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'order_status', ['status_id'], ['id'])
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.BIGINT(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('orders_status_fkey', 'order_status', ['status'], ['id'])
        batch_op.drop_column('status_id')

    # ### end Alembic commands ###
