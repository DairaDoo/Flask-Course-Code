"""empty message

Revision ID: 68220f417e0b
Revises: 25a8317d6424
Create Date: 2024-06-08 17:04:34.794300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68220f417e0b'
down_revision = '25a8317d6424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
