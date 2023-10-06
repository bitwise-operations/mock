"""create column for android

Revision ID: d0a83a026b65
Revises: a23a77b6e065
Create Date: 2021-10-11 15:44:28.238343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a83a026b65'
down_revision = 'a23a77b6e065'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'event_appflyer',
        sa.Column('advertising_id', sa.String (200), nullable = True),
    )


def downgrade():
    op.drop_column("event_appflyer", "advertising_id")
