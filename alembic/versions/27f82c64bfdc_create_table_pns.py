"""create table pns

Revision ID: 27f82c64bfdc
Revises: 
Create Date: 2022-07-21 08:32:57.355107

"""
from faker import Faker
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27f82c64bfdc'
down_revision = None
branch_labels = None
depends_on = None


faker = Faker('id_ID')


def upgrade() -> None:
    pns = op.create_table(
        'pns',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nama', sa.String(255), nullable=False),
        sa.Column('nip', sa.String(255), nullable=False),
        sa.Column('tLahir', sa.String(255), nullable=False),
        sa.Column('jabatan', sa.String(255), nullable=False),
        sa.Column('bulan', sa.String(255), nullable=False),
        sa.Column('img_url', sa.String(255), unique=True, nullable=True)
    )
    op.bulk_insert(
        pns,
        [{'nama': faker.name(),
          'nip': faker.isbn13(),
          'tLahir': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%d %B %Y"),
          'jabatan': faker.company(),
          'bulan': faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=55).strftime("%B"),
          'img_url': faker.image_url()
          } for x in range(800)]
    )


def downgrade() -> None:
    op.drop_table('pns')
