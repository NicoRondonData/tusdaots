from typing import List

from sqlalchemy import and_
from sqlmodel import Session, select

from app.scrapers.judical_processes.entities import CaseModel, JudicialCase
from app.scrapers.judical_processes.models import Case, JudicialCaseModel


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
        existing_ids_statement = select(JudicialCaseModel.id_process)
        result = await self.session.execute(existing_ids_statement)
        existing_ids = {case.id_process for case in result}
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
            if case.id_process not in existing_ids
        ]

        self.session.add_all(objects)
        await self.session.commit()

    async def get_all(self) -> List[JudicialCaseModel]:
        """
        Retrieve all users.

        Returns:
            List[UserModel]: A list of all user records.
        """
        statement = select(JudicialCaseModel)
        results = await self.session.execute(statement)
        return results

    async def get_all_info(self) -> List[Case]:
        """
        Retrieve all users.

        Returns:
            List[UserModel]: A list of all user records.
        """
        statement = select(Case)
        results = await self.session.execute(statement)
        return results

    async def add(self, data: CaseModel):
        new_data = Case(
            id=data.id,
            case_id=data.case_id,
            current_status=data.current_status,
            subject_id=data.subject_id,
            province_id=data.province_id,
            canton_id=data.canton_id,
            judicature_id=data.judicature_id,
            crime_name=data.crime_name,
            entry_date=data.entry_date,
            has_attached_document=data.has_attached_document,
            name=data.name,
            id_card=data.id_card,
            case_status_id=data.case_status_id,
            subject_name=data.subject_name,
            case_status_name=data.case_status_name,
            judicature_name=data.judicature_name,
            resolution_type_name=data.resolution_type_name,
            action_type_name=data.action_type_name,
            provision_date=data.provision_date,
            provision_name=data.provision_name,
            province_name=data.province_name,
            user_id=data.user_id,
            proceso=data.process,
        )

        existing_case = await self.session.execute(
            select(Case).where(
                and_(
                    Case.id == new_data.id,
                    Case.case_id == new_data.case_id,
                    Case.current_status == new_data.current_status,
                    Case.subject_id == new_data.subject_id,
                    Case.province_id == new_data.province_id,
                    Case.canton_id == new_data.canton_id,
                    Case.judicature_id == new_data.judicature_id,
                    Case.crime_name == new_data.crime_name,
                    Case.entry_date == new_data.entry_date,
                    Case.has_attached_document == new_data.has_attached_document,
                    Case.name == new_data.name,
                    Case.id_card == new_data.id_card,
                    Case.case_status_id == new_data.case_status_id,
                    Case.subject_name == new_data.subject_name,
                    Case.case_status_name == new_data.case_status_name,
                    Case.judicature_name == new_data.judicature_name,
                    Case.resolution_type_name == new_data.resolution_type_name,
                    Case.action_type_name == new_data.action_type_name,
                    Case.provision_date == new_data.provision_date,
                    Case.provision_name == new_data.provision_name,
                    Case.province_name == new_data.province_name,
                    Case.user_id == new_data.user_id,
                    Case.process == new_data.process,
                )
            )
        )
        existing_case = existing_case.scalars().first()
        if existing_case is None:
            self.session.add(new_data)
            await self.session.commit()
        # self.session.add(new_data)
        # await self.session.commit()
