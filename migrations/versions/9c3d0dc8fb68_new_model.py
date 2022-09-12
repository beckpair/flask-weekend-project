"""new model

Revision ID: 9c3d0dc8fb68
Revises: 2f415be670f8
Create Date: 2022-09-11 19:05:01.883053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c3d0dc8fb68'
down_revision = '2f415be670f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('element', sa.String(length=30), nullable=True),
    sa.Column('arcana', sa.String(length=30), nullable=True),
    sa.Column('upright', sa.String(length=150), nullable=True),
    sa.Column('reversed_', sa.String(length=150), nullable=True),
    sa.Column('gender', sa.String(length=30), nullable=True),
    sa.Column('suit', sa.String(length=30), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    # ### end Alembic commands ###
