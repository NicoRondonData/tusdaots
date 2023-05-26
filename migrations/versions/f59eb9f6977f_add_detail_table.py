"""add detail table

Revision ID: f59eb9f6977f
Revises: 2691120e0960
Create Date: 2023-05-26 06:07:27.933510

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "f59eb9f6977f"
down_revision = "2691120e0960"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "case",
        sa.Column("key_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("case_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("current_status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("subject_id", sa.Integer(), nullable=True),
        sa.Column("province_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("canton_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("judicature_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("crime_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("entry_date", sa.DateTime(), nullable=True),
        sa.Column(
            "has_attached_document", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("id_card", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("case_status_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("subject_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
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
        sa.Column("provision_date", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("provision_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("province_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("key_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("case")
    # ### end Alembic commands ###