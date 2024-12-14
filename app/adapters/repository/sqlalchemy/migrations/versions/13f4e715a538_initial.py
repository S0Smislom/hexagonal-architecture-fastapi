"""initial

Revision ID: 13f4e715a538
Revises:
Create Date: 2024-12-09 22:53:47.396536

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "13f4e715a538"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "equipment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "factory",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "plot",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("factory_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["factory_id"],
            ["factory.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "plot_equipment",
        sa.Column("plot_id", sa.Integer(), nullable=False),
        sa.Column("equipment_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["equipment_id"],
            ["equipment.id"],
        ),
        sa.ForeignKeyConstraint(
            ["plot_id"],
            ["plot.id"],
        ),
        sa.PrimaryKeyConstraint("plot_id", "equipment_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("plot_equipment")
    op.drop_table("plot")
    op.drop_table("factory")
    op.drop_table("equipment")
    # ### end Alembic commands ###
