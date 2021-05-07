"""empty message

Revision ID: 014cbfe53dfa
Revises: 951ba47be7d0
Create Date: 2021-05-06 20:48:46.252543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '014cbfe53dfa'
down_revision = '951ba47be7d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drone',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('camera_quality', sa.String(length=120), nullable=True),
    sa.Column('flight_time', sa.String(length=100), nullable=True),
    sa.Column('max_speed', sa.String(length=100), nullable=True),
    sa.Column('dimensions', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.String(length=50), nullable=True),
    sa.Column('cost_of_prod', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('series', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drone')
    # ### end Alembic commands ###