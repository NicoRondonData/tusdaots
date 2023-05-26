"""migrations initials

Revision ID: 2691120e0960
Revises:
Create Date: 2023-05-26 03:37:49.991654

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "2691120e0960"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "judicial_case",
        sa.Column("key_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("id_process", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "judicial_case_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("current_state", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("matter_id", sa.Integer(), nullable=True),
        sa.Column("province_id", sa.Integer(), nullable=True),
        sa.Column("canton_id", sa.Integer(), nullable=True),
        sa.Column("judicature_id", sa.Integer(), nullable=True),
        sa.Column("crime_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("date_of_filing", sa.DateTime(), nullable=True),
        sa.Column(
            "is_document_attached", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("id_number", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("case_status_id", sa.Integer(), nullable=True),
        sa.Column("matter_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "case_status_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("judicature_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "resolution_type_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "action_type_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("provision_date", sa.DateTime(), nullable=True),
        sa.Column("provision_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("province_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("process", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("user_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("key_id"),
    )
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
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_table("user")
    op.drop_table("judicial_case")
    # ### end Alembic commands ###