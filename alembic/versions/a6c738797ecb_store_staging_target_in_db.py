"""store staging target in db

Revision ID: a6c738797ecb
Revises: 7ef1e44e41b7
Create Date: 2016-11-07 14:33:10.929313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6c738797ecb'
down_revision = '7ef1e44e41b7'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staging_orders', sa.Column('staging_target', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('staging_orders', 'staging_target')
    ### end Alembic commands ###
