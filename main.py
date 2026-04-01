from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
import functions
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/candidates", response_model=schemas.CandidateResponse)
def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    if candidate.status not in schemas.VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    return functions.create_candidate(db, candidate)


@app.get("/candidates", response_model=List[schemas.CandidateResponse])
def get_candidates(status: Optional[str] = None, db: Session = Depends(get_db)):
    return functions.get_candidates(db, status)


@app.put("/candidates/{id}/status", response_model=schemas.CandidateResponse)
def update_status(id: int, update: schemas.CandidateUpdateStatus, db: Session = Depends(get_db)):
    if update.status not in schemas.VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    candidate = functions.get_candidate_by_id(db, id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return functions.update_candidate_status(db, candidate, update.status)