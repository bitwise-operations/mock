"""create table eventappflyer

Revision ID: a23a77b6e065
Revises: 
Create Date: 2021-09-24 19:12:03.230442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a23a77b6e065'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table ( 
        'event_appflyer', 
        sa.Column ('id', sa.Integer, primary_key = True), 
        sa.Column ('app_id', sa.String (200), nullable = True), 
        sa.Column ('idfa', sa.String (200), nullable = True),
        sa.Column ('idfv', sa.String (200), nullable = True),
        sa.Column ('appsflyer_id', sa.String (200), nullable = True),
        sa.Column ('customer_user_id', sa.String (200), nullable = True),
        sa.Column ('att', sa.Integer, nullable = True),
        sa.Column ('eventName', sa.String (200), nullable = True), 
        sa.Column ('eventValue', sa.String (200), nullable = True),
        sa.Column ('eventTime', sa.String (200), nullable = True),
        sa.Column ('eventCurrency', sa.String (200), nullable = True),
        sa.Column ('bundleIdentifier', sa.String (200), nullable = True),
        sa.Column ('os', sa.String (200), nullable = True),
    ) 


def downgrade():
    op.drop_table('event_appflyer')
