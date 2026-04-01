from sqlalchemy.orm import Session
from models import Candidate

def create_candidate(db: Session, candidate_data):
    candidate = Candidate(**candidate_data.dict())
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate

def get_candidates(db: Session, status=None):
    query = db.query(Candidate)
    if status:
        query = query.filter(Candidate.status == status)
    return query.all()

def get_candidate_by_id(db: Session, candidate_id: int):
    return db.query(Candidate).filter(Candidate.id == candidate_id).first()

def update_candidate_status(db: Session, candidate, status: str):
    candidate.status = status
    db.commit()
    db.refresh(candidate)
    return candidate