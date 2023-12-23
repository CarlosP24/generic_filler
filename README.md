# generic_filler
Generic list and form filler for group activities with minors.

# USAGE
1. Setup main data in "config.json". Databases (input_data and database) must be .csv files. Templates for authorizations and lists must be .docx with mail-merge fields as specified in "writers.py".
2. Set up the email text in "email_aux.py".
3. Set up "renamer.py", matching the fields in the input .csv (left, in Spanish) with the standard names in the pandas df (right, english)
4. Run "run_inscripciones.py" + SO (linux or macos). This script takes new data from "input_data" (from "last_time" onwards) and writes it in "database", fills the authorization and sends the confirmation email to the family.
