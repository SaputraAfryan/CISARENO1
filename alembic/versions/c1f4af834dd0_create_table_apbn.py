"""create table apbn

Revision ID: c1f4af834dd0
Revises: 27f82c64bfdc
Create Date: 2022-07-21 08:33:09.072497

"""
from faker import Faker
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1f4af834dd0'
down_revision = '27f82c64bfdc'
branch_labels = None
depends_on = None


faker = Faker('id_ID')


def upgrade() -> None:
    apbn = op.create_table(
        'apbn',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nama', sa.String(255), nullable=False),
        sa.Column('tLahir', sa.String(255), nullable=False),
        sa.Column('jabatan', sa.String(255), nullable=False),
        sa.Column('bulan', sa.String(255), nullable=False),
        sa.Column('img_url', sa.String(255), unique=True, nullable=True)
    )
    op.bulk_insert(
        apbn,
        [{'nama': faker.name(),
          'tLahir': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%d %B %Y"),
          'jabatan': faker.company(),
          'bulan': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%B"),
          'img_url': faker.image_url()
          } for x in range(800)]
    )


def downgrade() -> None:
    op.drop_table('apbn')
