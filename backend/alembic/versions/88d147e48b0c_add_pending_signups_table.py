"""add pending signups table

Revision ID: 88d147e48b0c
Revises: 2efd79e0f5f5
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "88d147e48b0c"
down_revision: Union[str, Sequence[str], None] = "2efd79e0f5f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pending_signups",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("verification_code", sa.String(), nullable=True),
        sa.Column(
            "verification_code_expires_at",
            sa.DateTime(),
            nullable=True,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.UniqueConstraint("email"),
    )
    op.create_index(
        "ix_pending_signups_id",
        "pending_signups",
        ["id"],
        unique=False,
    )
    op.create_index(
        "ix_pending_signups_email",
        "pending_signups",
        ["email"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_pending_signups_email", table_name="pending_signups")
    op.drop_index("ix_pending_signups_id", table_name="pending_signups")
    op.drop_table("pending_signups")
