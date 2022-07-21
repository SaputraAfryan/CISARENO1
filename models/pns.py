from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)

metadata = MetaData()
Pns = Table(
    "pns", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("nama", String(255), nullable=False),
    Column("nip", String(255), nullable=False),
    Column("tLahir", String(255), nullable=False),
    Column("jabatan", String(255), nullable=False),
    Column("bulan", String(255), nullable=False),
    Column('img_url', String(255), unique=True, nullable=True)
)
