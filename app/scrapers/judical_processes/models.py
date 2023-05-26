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
        """
        Create a JudicialCaseModel instance from a Pydantic JudicialCase object.

        Args:
            data: The Pydantic JudicialCase object.

        Returns:
            JudicialCaseModel: The created JudicialCaseModel instance.

        """
        return cls(**data.dict())

    @classmethod
    def to_pydantic(cls, instance):
        """
        Convert a JudicialCaseModel instance to a Pydantic JudicialCase object.

        Args:
            instance (JudicialCaseModel): The JudicialCaseModel instance.

        Returns:
            JudicialCase: The converted Pydantic JudicialCase object.

        """
        return JudicialCase(**instance.dict())

    @validator("date_of_filing", "provision_date", pre=True)
    def parse_datetime(cls, value):
        """
        Validator to parse datetime values.

        Args:
            value: The datetime value.

        Returns:
            Optional[datetime]: The parsed datetime value or None if parsing fails.

        """
        try:
            dt = datetime.fromisoformat(value)
            return dt.replace(tzinfo=None)
        except ValueError:
            return None


class Case(SQLModel, table=True):
    key_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True},
    )
    id: Optional[str]
    case_id: Optional[str]
    user_id: Optional[str]
    current_status: Optional[str]
    subject_id: Optional[int]
    province_id: Optional[str]
    canton_id: Optional[str]
    judicature_id: Optional[str]
    crime_name: Optional[str]
    entry_date: Optional[datetime]
    has_attached_document: Optional[str]
    name: Optional[str]
    id_card: Optional[str]
    case_status_id: Optional[str]
    subject_name: Optional[str]
    case_status_name: Optional[str]
    judicature_name: Optional[str]
    resolution_type_name: Optional[str]
    action_type_name: Optional[str]
    provision_date: Optional[str]
    provision_name: Optional[str]
    province_name: Optional[str]
    process: Optional[ProcessEnum] = Field(default=None, alias="proceso")

    @validator("entry_date", "provision_date", pre=True)
    def parse_datetime(cls, value):
        """
        Validator to parse datetime values.

        Args:
            value: The datetime value.

        Returns:
            Optional[datetime]: The parsed datetime value or None if parsing fails.

        """
        try:
            dt = datetime.fromisoformat(value)
            return dt.replace(tzinfo=None)
        except ValueError:
            return None
