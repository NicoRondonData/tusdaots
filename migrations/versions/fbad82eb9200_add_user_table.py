"""add user table

Revision ID: fbad82eb9200
Revises:
Create Date: 2023-05-25 02:19:21.534220

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "fbad82eb9200"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "password", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###