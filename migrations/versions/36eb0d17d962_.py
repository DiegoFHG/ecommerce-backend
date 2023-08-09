"""empty message

Revision ID: 36eb0d17d962
Revises: 8a4ae7720a8a
Create Date: 2023-08-07 18:03:58.788014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36eb0d17d962'
down_revision = '8a4ae7720a8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.BigInteger(), nullable=False))
        batch_op.add_column(sa.Column('product_id', sa.BigInteger(), nullable=False))
        batch_op.drop_constraint('order_products_order_fkey', type_='foreignkey')
        batch_op.drop_constraint('order_products_product_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'products', ['product_id'], ['id'])
        batch_op.create_foreign_key(None, 'orders', ['order_id'], ['id'])
        batch_op.drop_column('order')
        batch_op.drop_column('product')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product', sa.BIGINT(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('order', sa.BIGINT(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('order_products_product_fkey', 'products', ['product'], ['id'])
        batch_op.create_foreign_key('order_products_order_fkey', 'orders', ['order'], ['id'])
        batch_op.drop_column('product_id')
        batch_op.drop_column('order_id')

    # ### end Alembic commands ###
