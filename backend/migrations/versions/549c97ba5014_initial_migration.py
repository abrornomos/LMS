"""Initial migration.

Revision ID: 549c97ba5014
Revises: 
Create Date: 2021-12-24 10:25:13.456339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549c97ba5014'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_meta', sa.Column('key', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'student_meta', ['key'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student_meta', type_='unique')
    op.drop_column('student_meta', 'key')
    # ### end Alembic commands ###
