To run this project:

1. Clone the repository: git clone https://github.com/Nits-007/TeckLeap_Assgn.git
2. Move to the folder directory: cd TeckLeap_Assgn
3. Create virtual environment: python -m venv venv
4. Activate the virtual environment: venv\Scripts\activate
5. Install the libraries: pip install -r requirements.txt
6. Run the main file: uvicorn main:app --reload


API Endpoints:

1. Create Candidate (POST) : /candidates
   Request Body Type: {
                        "name": "Peter Parker",
                        "email": "peter@parker.com",
                        "skill": "Spider Sense",
                        "status": "applied"
                      }

2. Get all Candidates (GET) : /candidates

3. Get all Candidates filtered by status (GET) : /candidates?status=interview

4. Update existing Candidate status (PUT) : /candidates/{id}/status
   Request Body Type: {
                        "status": "interview"
                      }

As per given in the assignment only these 4 status are valid:  applied, interview, selected, rejected 

