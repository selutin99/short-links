"""empty message

Revision ID: 14870501b985
Revises: 
Create Date: 2020-10-01 08:08:24.956100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14870501b985'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long_url', sa.String(length=255), nullable=True),
    sa.Column('short_link', sa.String(length=255), nullable=True),
    sa.Column('short_postfix', sa.String(length=255), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('long_url'),
    sa.UniqueConstraint('short_link'),
    sa.UniqueConstraint('short_postfix')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    # ### end Alembic commands ###
