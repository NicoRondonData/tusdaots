from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, validator


class ProcessEnum(str, Enum):
    plaintiff = "demandante"
    defendant = "demandado"


class Person(BaseModel):
    id_number: str = Field(alias="cedulaActor")
    name: str = Field(alias="nombreActor")


class Defendant(BaseModel):
    id_number: str = Field(alias="cedulaDemandado")
    name: str = Field(alias="nombreDemandado")


class Case(BaseModel):
    case_number: str = Field(alias="numeroCausa")
    plaintiff: Person = Field(alias="actor")
    defendant: Defendant = Field(alias="demandado")
    province: str = Field(alias="provincia")
    prosecutor_office_number: str = Field(alias="numeroFiscalia")
    recaptcha: str = Field(alias="recaptcha")


class JudicialCase(BaseModel):
    id_process: str = Field(alias="id")
    judicial_case_id: Optional[str] = Field(alias="idJuicio")
    current_state: Optional[str] = Field(alias="estadoActual")
    matter_id: Optional[int] = Field(alias="idMateria")
    province_id: Optional[int] = Field(alias="idProvincia")
    canton_id: Optional[int] = Field(alias="idCanton")
    judicature_id: Optional[int] = Field(alias="idJudicatura")
    crime_name: Optional[str] = Field(alias="nombreDelito")
    date_of_filing: Optional[datetime] = Field(alias="fechaIngreso")
    is_document_attached: Optional[str] = Field(alias="iEDocumentoAdjunto")
    name: Optional[str] = Field(alias="nombre")
    id_number: Optional[str] = Field(alias="cedula")
    case_status_id: Optional[int] = Field(alias="idEstadoJuicio")
    matter_name: Optional[str] = Field(alias="nombreMateria")
    case_status_name: Optional[str] = Field(alias="nombreEstadoJuicio")
    judicature_name: Optional[str] = Field(alias="nombreJudicatura")
    resolution_type_name: Optional[str] = Field(alias="nombreTipoResolucion")
    action_type_name: Optional[str] = Field(alias="nombreTipoAccion")
    provision_date: Optional[datetime] = Field(alias="fechaProvidencia")
    provision_name: Optional[str] = Field(alias="nombreProvidencia")
    province_name: Optional[str] = Field(alias="nombreProvincia")
    process: Optional[ProcessEnum] = Field(alias="proceso")
    user_id: Optional[str] = Field(alias="idUsuario")

    @validator("date_of_filing", "provision_date", pre=True)
    def parse_datetime(cls, value):
        if value is not None:
            return datetime.fromisoformat(value)
