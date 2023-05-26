from typing import List

from sqlmodel import Session

from app.scrapers.judical_processes.entities import JudicialCase
from app.scrapers.judical_processes.models import JudicialCaseModel


class JudicialCaseRepository:
    def __init__(self, session: Session):
        self.session = session

    async def bulk_insert(self, cases: List[JudicialCase]):
        """
        Bulk insert a list of JudicialCase objects into the database.

        Args:
            cases (List[JudicialCase]): List of JudicialCase objects to insert.

        Returns:
            None
        """
        objects = [
            JudicialCaseModel(
                id=case.id_process,
                idJuicio=case.judicial_case_id,
                estadoActual=case.current_state,
                idMateria=case.matter_id,
                idProvincia=case.province_id,
                idCanton=case.canton_id,
                idJudicatura=case.judicature_id,
                nombreDelito=case.crime_name,
                fechaIngreso=case.date_of_filing,
                iEDocumentoAdjunto=case.is_document_attached,
                nombre=case.name,
                cedula=case.id_number,
                idEstadoJuicio=case.case_status_id,
                nombreMateria=case.matter_name,
                nombreEstadoJuicio=case.case_status_name,
                nombreJudicatura=case.judicature_name,
                nombreTipoResolucion=case.resolution_type_name,
                nombreTipoAccion=case.action_type_name,
                fechaProvidencia=case.provision_date,
                nombreProvidencia=case.provision_name,
                nombreProvincia=case.province_name,
                proceso=case.process,
                idUsuario=case.user_id,
            )
            for case in cases
        ]

        self.session.add_all(objects)
        await self.session.commit()
