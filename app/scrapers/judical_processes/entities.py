from datetime import datetime

from pydantic import BaseModel, Field, validator


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
    id: int = Field(alias="id")
    judicial_case_id: str = Field(alias="idJuicio")
    current_state: str = Field(alias="estadoActual")
    matter_id: int = Field(alias="idMateria")
    province_id: int = Field(alias="idProvincia")
    canton_id: int = Field(alias="idCanton")
    judicature_id: int = Field(alias="idJudicatura")
    crime_name: str = Field(alias="nombreDelito")
    date_of_filing: datetime = Field(alias="fechaIngreso")
    is_document_attached: str = Field(alias="iEDocumentoAdjunto")
    name: str = Field(alias="nombre")
    id_number: str = Field(alias="cedula")
    case_status_id: int = Field(alias="idEstadoJuicio")
    matter_name: str = Field(alias="nombreMateria")
    case_status_name: str = Field(alias="nombreEstadoJuicio")
    judicature_name: str = Field(alias="nombreJudicatura")
    resolution_type_name: str = Field(alias="nombreTipoResolucion")
    action_type_name: str = Field(alias="nombreTipoAccion")
    provision_date: datetime = Field(alias="fechaProvidencia")
    provision_name: str = Field(alias="nombreProvidencia")
    province_name: str = Field(alias="nombreProvincia")

    @validator("date_of_filing", "provision_date", pre=True)
    def parse_datetime(cls, value):
        return datetime.fromisoformat(value)
