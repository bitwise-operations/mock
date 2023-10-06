"""create column for android aie

Revision ID: b0234a2a0cd4
Revises: d0a83a026b65
Create Date: 2021-10-11 16:05:12.086143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0234a2a0cd4'
down_revision = 'd0a83a026b65'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'event_appflyer',
        sa.Column('aie', sa.String (200), nullable = True),
    )


def downgrade():
    op.drop_column("event_appflyer", "aie")
