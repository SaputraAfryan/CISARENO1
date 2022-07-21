"""create table apbd

Revision ID: f2f0c580a6fb
Revises: c1f4af834dd0
Create Date: 2022-07-21 08:33:13.974297

"""
from faker import Faker
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f0c580a6fb'
down_revision = 'c1f4af834dd0'
branch_labels = None
depends_on = None


faker = Faker('id_ID')


def upgrade() -> None:
    apbd = op.create_table(
        'apbd',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nama', sa.String(255), nullable=False),
        sa.Column('tLahir', sa.String(255), nullable=False),
        sa.Column('jabatan', sa.String(255), nullable=False),
        sa.Column('bulan', sa.String(255), nullable=False),
        sa.Column('img_url', sa.String(255), unique=True, nullable=True)
    )
    op.bulk_insert(
        apbd,
        [{'nama': faker.name(),
          'tLahir': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%d %B %Y"),
          'jabatan': faker.company(),
          'bulan': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%B"),
          'img_url': faker.image_url()
          } for x in range(800)]
    )


def downgrade() -> None:
    op.drop_table('apbd')
