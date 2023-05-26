from datetime import datetime
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel

from app.scrapers.judical_processes.entities import JudicialCase, ProcessEnum


class JudicialCaseModel(SQLModel, table=True):
    __tablename__ = "judicial_case"
    key_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True},
    )
    id_process: Optional[str] = Field(default=None, alias="id")
    judicial_case_id: Optional[str] = Field(default=None, alias="idJuicio")
    current_state: Optional[str] = Field(default=None, alias="estadoActual")
    matter_id: Optional[int] = Field(default=None, alias="idMateria")
    province_id: Optional[int] = Field(default=None, alias="idProvincia")
    canton_id: Optional[int] = Field(default=None, alias="idCanton")
    judicature_id: Optional[int] = Field(default=None, alias="idJudicatura")
    crime_name: Optional[str] = Field(default=None, alias="nombreDelito")
    date_of_filing: Optional[datetime] = Field(default=None, alias="fechaIngreso")
    is_document_attached: Optional[str] = Field(
        default=None, alias="iEDocumentoAdjunto"
    )
    name: Optional[str] = Field(default=None, alias="nombre")
    id_number: Optional[str] = Field(default=None, alias="cedula")
    case_status_id: Optional[int] = Field(default=None, alias="idEstadoJuicio")
    matter_name: Optional[str] = Field(default=None, alias="nombreMateria")
    case_status_name: Optional[str] = Field(default=None, alias="nombreEstadoJuicio")
    judicature_name: Optional[str] = Field(default=None, alias="nombreJudicatura")
    resolution_type_name: Optional[str] = Field(
        default=None, alias="nombreTipoResolucion"
    )
    action_type_name: Optional[str] = Field(default=None, alias="nombreTipoAccion")
    provision_date: Optional[datetime] = Field(default=None, alias="fechaProvidencia")
    provision_name: Optional[str] = Field(default=None, alias="nombreProvidencia")
    province_name: Optional[str] = Field(default=None, alias="nombreProvincia")
    process: Optional[ProcessEnum] = Field(default=None, alias="proceso")
    user_id: Optional[str] = Field(default=None, alias="idUsuario")

    @classmethod
    def from_pydantic(cls, data):
        return cls(**data.dict())

    @classmethod
    def to_pydantic(cls, instance):
        return JudicialCase(**instance.dict())

    @validator("date_of_filing", "provision_date", pre=True)
    def parse_datetime(cls, value):
        try:
            dt = datetime.fromisoformat(value)
            return dt.replace(tzinfo=None)
        except ValueError:
            return None
