"""empty message

Revision ID: 3ddd54edbc7c
Revises: 8d1978fb086d
Create Date: 2022-03-24 15:36:31.423318

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3ddd54edbc7c'
down_revision = '8d1978fb086d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('content', sa.Text(), nullable=False))
    op.drop_column('answer', 'context')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('context', mysql.TEXT(), nullable=False))
    op.drop_column('answer', 'content')
    # ### end Alembic commands ###